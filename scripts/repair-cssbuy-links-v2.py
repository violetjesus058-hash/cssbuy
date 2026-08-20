from pathlib import Path
import re
import subprocess
from difflib import SequenceMatcher

ROOT = Path('/home/ubuntu/cssbuy')
actual = sorted((p.stem for p in (ROOT/'blog').glob('*.md') if len(p.stem) > 8), key=len, reverse=True)

def extract_slug(s):
    m = re.search(r'/blog/([^\s)\"\']+)', s)
    return m.group(1).strip('/') if m else None

def score(old, candidate):
    old_tokens = old.split('-')
    cand_tokens = candidate.split('-')
    common = len(set(old_tokens) & set(cand_tokens))
    token_score = common / max(1, len(set(cand_tokens)))
    seq = SequenceMatcher(None, old, candidate).ratio()
    return token_score * 0.65 + seq * 0.35

# Recover the pre-v1-repair slug from the diff lines and infer its actual title-based slug.
diff = subprocess.check_output(['git','diff','--unified=0','--','*.md','*.vue','*.js','*.mjs'], cwd=ROOT, text=True, errors='ignore')
old_to_new = {}
removed = None
for line in diff.splitlines():
    if line.startswith('---') or line.startswith('+++'):
        continue
    if line.startswith('-') and '/blog/' in line:
        removed = line
    elif line.startswith('+') and '/blog/' in line and removed:
        old = extract_slug(removed)
        new = extract_slug(line)
        if old and new == 'cssbuy':
            old_to_new[old] = max(actual, key=lambda c: score(old, c))
        removed = None

# Also repair any current missing target by similarity, never allowing the bare cssbuy slug.
slugs = set(actual)
changed_files=0
changes=0
for path in [*ROOT.glob('*.md'), * (ROOT/'blog').glob('*.md'), *ROOT.glob('.vitepress/**/*.vue'), *ROOT.glob('.vitepress/**/*.js'), *ROOT.glob('.vitepress/**/*.mjs')]:
    if not path.is_file(): continue
    try: text=path.read_text(encoding='utf-8')
    except UnicodeDecodeError: continue
    original=text
    def replace(m):
        slug=m.group(1).strip('/')
        if slug == 'cssbuy':
            return m.group(0).replace('/blog/cssbuy', '/blog/' + (old_to_new.get(slug) or 'cssbuy'))
        if slug in slugs: return m.group(0)
        target=old_to_new.get(slug)
        if not target:
            candidates=[c for c in actual if c != 'cssbuy' and score(slug,c) >= 0.52]
            if candidates: target=max(candidates, key=lambda c: score(slug,c))
        return m.group(0).replace('/blog/'+slug, '/blog/'+target) if target else m.group(0)
    text=re.sub(r'/blog/([^\)#\s]+)', replace, text)
    if text != original:
        path.write_text(text,encoding='utf-8'); changed_files+=1
        changes += 1
print(f'diff_recovered_mappings={len(old_to_new)}')
print(f'files_changed={changed_files}')
print(f'link_replacements={changes}')
