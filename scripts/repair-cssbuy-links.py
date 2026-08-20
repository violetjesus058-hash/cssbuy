from pathlib import Path
import re

ROOT = Path('/home/ubuntu/cssbuy')
BLOG = ROOT / 'blog'
slugs = sorted((p.stem for p in BLOG.glob('*.md')), key=len, reverse=True)
changed = 0
repaired = []
for path in [*ROOT.glob('*.md'), *BLOG.glob('*.md'), *ROOT.glob('.vitepress/**/*.vue'), *ROOT.glob('.vitepress/**/*.js'), *ROOT.glob('.vitepress/**/*.mjs')]:
    if not path.is_file():
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue
    original = text
    def replace(match):
        slug = match.group(1).strip('/')
        if slug in slugs:
            return match.group(0)
        for candidate in slugs:
            if slug.startswith(candidate + '-'):
                repaired.append((slug, candidate))
                return match.group(0).replace(slug, candidate)
        return match.group(0)
    text = re.sub(r'\]\(/blog/([^\)#]+)', replace, text)
    if text != original:
        path.write_text(text, encoding='utf-8')
        changed += 1
print(f'files_changed={changed}')
print(f'links_repaired={len(repaired)}')
for old, new in repaired[:30]:
    print(f'{old} -> {new}')
