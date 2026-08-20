from pathlib import Path
import re

ROOT=Path('/home/ubuntu/cssbuy')

def slugify(title):
    title=title.lower().replace('&',' and ')
    title=re.sub(r"['’]",'',title)
    title=re.sub(r'[^a-z0-9]+','-',title)
    return re.sub(r'-+','-',title).strip('-')

mismatch=[]
missing_keywords=[]
for path in sorted((ROOT/'blog').glob('*.md')):
    text=path.read_text(encoding='utf-8',errors='ignore')
    front=text.split('---',2)[1] if text.startswith('---') and len(text.split('---',2))==3 else ''
    m=re.search(r"^title:\s*['\"]?(.*?)['\"]?\s*$",front,re.M)
    title=m.group(1).strip().strip("'\"") if m else ''
    expected=slugify(title)
    if path.stem != expected and not path.stem.startswith(expected+'-'):
        mismatch.append((path.name,title,expected))
    if not re.search(r'^keywords:',front,re.M):
        missing_keywords.append(path.name)
print('articles',len(list((ROOT/'blog').glob('*.md'))))
print('title_slug_mismatches',len(mismatch))
print('missing_keyword_metadata',len(missing_keywords))
for x in mismatch[:20]: print('MISMATCH',x)
