from pathlib import Path
import re

ROOT = Path('/home/ubuntu/cssbuy')
blog = ROOT / 'blog'
articles = sorted(blog.glob('*.md'))
slugs = {p.stem for p in articles}
source_files = [p for p in [*ROOT.glob('*.md'), *blog.glob('*.md'), *ROOT.glob('.vitepress/**/*.vue'), *ROOT.glob('.vitepress/**/*.js'), *ROOT.glob('.vitepress/**/*.mjs')] if p.is_file()]
legacy = []
missing = []
links = 0
for path in source_files:
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue
    if re.search(r'(?i)spreadsheet|usfans|google\s*sheets?|docs\.google', text):
        legacy.append(str(path.relative_to(ROOT)))
    for match in re.finditer(r'\]\(/blog/([^\)#]+)', text):
        links += 1
        slug = match.group(1).strip('/')
        if slug not in slugs:
            missing.append((str(path.relative_to(ROOT)), slug))
redirects = (ROOT / 'public' / '_redirects').read_text(encoding='utf-8', errors='ignore').splitlines()
print(f'articles={len(articles)}')
print(f'articles_with_title={sum(bool(re.search(r"^title:", p.read_text(encoding="utf-8", errors="ignore"), re.M)) for p in articles)}')
print(f'articles_with_keywords={sum(bool(re.search(r"^keywords:", p.read_text(encoding="utf-8", errors="ignore"), re.M)) for p in articles)}')
print(f'legacy_source_files={len(legacy)}')
print(f'legacy_redirect_lines={sum(bool(re.search(r"(?i)spreadsheet|usfans", x)) for x in redirects)}')
print(f'redirect_301_lines={sum(x.strip().endswith("301") for x in redirects)}')
print(f'internal_article_links={links}')
print(f'missing_internal_article_links={len(missing)}')
for item in legacy[:20]: print('LEGACY', item)
for item in missing[:20]: print('MISSING', item)
