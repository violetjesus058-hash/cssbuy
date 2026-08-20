from pathlib import Path
import re

ROOT=Path('/home/ubuntu/cssbuy')
BLOG=ROOT/'blog'
slugs={p.stem for p in BLOG.glob('*.md')}
choices={
 'hoodies':'cssbuy-hoodies-2026-complete-hoodie-sourcing-guide',
 'hoodie':'cssbuy-hoodie-guide-2026-complete-buying-guide-for-streetwear-hoodies',
 't-shirts':'cssbuy-t-shirts-2026-complete-t-shirt-sourcing-guide',
 't-shirts':'cssbuy-t-shirts-2026-complete-t-shirt-sourcing-guide',
 'jackets':'cssbuy-jackets-2026-premium-outerwear-collection',
 'clothes':'cssbuy-clothes-2026-latest-trends-and-new-arrivals',
 'jeans':'cssbuy-jeans-2026-complete-guide-to-denim-and-work-pants',
 'sneakers':'cssbuy-sneakers-2026-complete-sneaker-sourcing-guide',
 'hats':'cssbuy-hats-2026-complete-guide-to-verified-headwear-collection',
 'accessories':'cssbuy-accessories-2026-complete-guide-to-hats-jewelry-and-more',
 'pants':'cssbuy-pants-2026-complete-guide-to-all-styles-and-brands',
 'bags':'cssbuy-bags-2026-complete-bag-sourcing-guide',
}
changed=0
count=0
for path in [*ROOT.glob('*.md'),*BLOG.glob('*.md'),*ROOT.glob('.vitepress/**/*.vue'),*ROOT.glob('.vitepress/**/*.js'),*ROOT.glob('.vitepress/**/*.mjs')]:
 if not path.is_file(): continue
 try: text=path.read_text(encoding='utf-8')
 except UnicodeDecodeError: continue
 original=text
 def repl(m):
  label=re.sub(r'[^a-z0-9 -]','',m.group(1).lower()).strip()
  target=None
  for key,value in choices.items():
   if key in label:
    target=value; break
  if target and target in slugs:
   global count
   count+=1
   return m.group(0).replace('/blog/cssbuy/', '/blog/'+target+'/')
  return m.group(0)
 text=re.sub(r'\[([^\]]+)\]\(/blog/cssbuy/', repl, text)
 if text!=original:
  path.write_text(text,encoding='utf-8'); changed+=1
print(f'files_changed={changed}')
print(f'links_repaired={count}')
