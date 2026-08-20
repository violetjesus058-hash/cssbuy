from pathlib import Path
import csv
import re
from urllib.parse import quote_plus

ROOT = Path('/home/ubuntu/cssbuy')
BLOG = ROOT / 'blog'
BASE = 'https://repsootd.com/products/'

# Brand matches are evaluated against title/description/keywords before categories.
BRANDS = [
    'Vivienne Westwood', 'Ralph Lauren', 'Louis Vuitton', 'Stone Island', 'Palm Angels',
    'Canada Goose', 'Calvin Klein', 'Gallery Dept', 'C.P. Company', 'Air Jordan',
    'AMI Paris', 'Off-White', 'Moncler', 'Balenciaga', 'Burberry', 'Corteiz',
    'Essentials', 'Trapstar', 'Casablanca', 'Lacoste', 'Rolex', 'Goyard', 'Gucci',
    'Nike', 'Amiri', 'Dior', 'BAPE', 'Bape', 'Hellstar', 'Vlone', 'Stussy', 'Stüssy',
    'A Bathing Ape',
]

CATEGORIES = [
    ('underwear', 'Underwear & Socks'), ('socks', 'Underwear & Socks'),
    ('hoodie', 'Hoodies & Sweatshirts'), ('sweatshirt', 'Hoodies & Sweatshirts'),
    ('sweater', 'Sweaters'), ('cardigan', 'Sweaters'),
    ('outerwear', 'Outerwear'), ('jacket', 'Outerwear'), ('coat', 'Outerwear'),
    ('windbreaker', 'Outerwear'), ('puffer', 'Outerwear'),
    ('t-shirt', 'T-Shirts'), ('t shirt', 'T-Shirts'), ('tee', 'T-Shirts'),
    ('polo', 'Polos'), ('shirt', 'T-Shirts'),
    ('shorts', 'Shorts'), ('jeans', 'Pants'), ('trousers', 'Pants'),
    ('pants', 'Pants'), ('sweatpants', 'Pants'), ('cargo', 'Pants'),
    ('tracksuit', 'Sets'), ('track suit', 'Sets'), ('set', 'Sets'),
    ('jersey', 'Jerseys'), ('football shirt', 'Jerseys'),
    ('sneaker', 'Shoes & Sneakers'), ('sneakers', 'Shoes & Sneakers'),
    ('shoe', 'Shoes & Sneakers'), ('shoes', 'Shoes & Sneakers'), ('boot', 'Shoes & Sneakers'),
    ('footwear', 'Shoes & Sneakers'), ('trainer', 'Shoes & Sneakers'),
    ('hat', 'Hats & Scarves'), ('cap', 'Hats & Scarves'), ('beanie', 'Hats & Scarves'),
    ('scarf', 'Hats & Scarves'),
    ('belt', 'Belts'), ('fragrance', 'Fragrances'), ('perfume', 'Fragrances'),
    ('watch', 'Mechanical Watches'), ('timepiece', 'Mechanical Watches'),
    ('sunglasses', 'Eyewear'), ('eyewear', 'Eyewear'), ('glasses', 'Eyewear'),
    ('backpack', 'Bags'), ('crossbody', 'Bags'), ('handbag', 'Bags'), ('bag', 'Bags'),
    ('iphone', 'Electronics'), ('macbook', 'Electronics'), ('laptop', 'Electronics'),
    ('phone', 'Electronics'), ('gpu', 'Electronics'), ('graphics card', 'Electronics'),
    ('electronics', 'Electronics'), ('gaming', 'Electronics'), ('console', 'Electronics'),
    ('lego', 'Electronics'), ('hot wheels', 'Electronics'),
]

# Avoid using generic words from long article bodies; title and metadata are the intent signal.
def parse_frontmatter(text):
    if not text.startswith('---'):
        return {}
    end = text.find('\n---', 3)
    if end < 0:
        return {}
    block = text[3:end]
    result = {}
    for line in block.splitlines():
        m = re.match(r'^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$', line)
        if m:
            result[m.group(1).lower()] = m.group(2).strip().strip("'\"")
    return result

def norm(text):
    return re.sub(r'[^a-z0-9+&. -]+', ' ', text.lower()).replace('&', ' and ')

def has_term(text, term):
    t = norm(text)
    termn = norm(term)
    return bool(re.search(r'(?<![a-z0-9])' + re.escape(termn) + r'(?![a-z0-9])', t))

def target_for(meta, body):
    intent = ' '.join(meta.get(k, '') for k in ('title', 'description', 'keywords', 'tags'))
    # Brand intent is more commercially specific than a generic category.
    for brand in BRANDS:
        if has_term(intent, brand):
            return f'{BASE}?q={quote_plus(brand)}', 'brand', brand
    # Apply category mappings from most specific to broadest.
    for term, category in CATEGORIES:
        if has_term(intent, term):
            return f'{BASE}?q={quote_plus(category)}', 'category', category
    return BASE, 'all-products', 'All Products'

def update_rel(tag):
    m = re.search(r'\brel=["\']([^"\']*)["\']', tag, re.I)
    tokens = set(m.group(1).lower().split()) if m else set()
    tokens.update(['nofollow', 'sponsored', 'noopener', 'noreferrer'])
    value = 'rel="' + ' '.join(sorted(tokens)) + '"'
    if m:
        return tag[:m.start()] + value + tag[m.end():]
    return tag[:-1] + ' ' + value + '>'

rows=[]
for path in sorted(BLOG.glob('*.md')):
    original = path.read_text(encoding='utf-8', errors='ignore')
    meta = parse_frontmatter(original)
    target, kind, matched = target_for(meta, original)
    # Update raw HTML anchors and Markdown links that point at the generic store root.
    text = original
    text = re.sub(r'(href=["\'])https://repsootd\.com/(?:\?[^"\']*)?(["\'])', lambda m: m.group(1)+target+m.group(2), text, flags=re.I)
    text = re.sub(r'(\]\()https://repsootd\.com/(?:\?[^) ]*)?(\))', lambda m: m.group(1)+target+m.group(2), text, flags=re.I)
    # Add a contextual CTA to articles that have no existing RepsOotd link.
    if 'https://repsootd.com/' not in text:
        if kind == 'brand':
            label = f'Browse {matched} products on RepsOotd'
        elif kind == 'category':
            label = f'Browse {matched} on RepsOotd'
        else:
            label = 'Browse all products on RepsOotd'
        cta = (f'\n\n## Explore related products\n\n'
               f'For readers who want to continue exploring relevant products, '
               f'<a href="{target}" rel="nofollow sponsored noopener noreferrer">{label}</a>. '
               f'Product availability and search results can change, so verify the current listing before ordering.\n')
        marker = '\n## How this guide was prepared'
        if marker in text:
            text = text.replace(marker, cta + marker, 1)
        else:
            text = text.rstrip() + cta
    # Add the no-weight policy to every updated repsootd anchor.
    text = re.sub(r'<a\b[^>]*href=["\']' + re.escape(target) + r'["\'][^>]*>', lambda m: update_rel(m.group(0)), text, flags=re.I)
    if text != original:
        path.write_text(text, encoding='utf-8')
    rows.append({'file': str(path.relative_to(ROOT)), 'title': meta.get('title',''), 'kind': kind, 'match': matched, 'target': target, 'changed': text != original})

with (ROOT/'blog-repssootd-link-map.csv').open('w', newline='', encoding='utf-8') as f:
    w=csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader(); w.writerows(rows)

from collections import Counter
print(f'articles={len(rows)}')
print('changed=' + str(sum(r['changed'] for r in rows)))
print('by_kind=' + repr(dict(Counter(r['kind'] for r in rows))))
print('top_targets=')
for target,count in Counter(r['target'] for r in rows).most_common(20): print(count, target)
