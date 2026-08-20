from pathlib import Path
import re

ROOT=Path('/home/ubuntu/cssbuy')
paths=[*ROOT.glob('*.md'),*(ROOT/'blog').glob('*.md'),*ROOT.glob('.vitepress/**/*.vue'),*ROOT.glob('.vitepress/**/*.js'),*ROOT.glob('.vitepress/**/*.mjs')]
changed=0
for path in paths:
    if not path.is_file(): continue
    try: text=path.read_text(encoding='utf-8')
    except UnicodeDecodeError: continue
    original=text
    # Close single-quoted blog paths when a comma, object close, or newline follows the path.
    text=re.sub(r"('/blog/[a-z0-9-]+)(?=\s*[,}])", r"\1'", text, flags=re.I)
    text=re.sub(r"('/blog/[a-z0-9-]+)(?=\s*\n)", r"\1'", text, flags=re.I)
    text=re.sub(r'("/blog/[a-z0-9-]+)(?=\s*[,}])', r'\1"', text, flags=re.I)
    text=re.sub(r'("/blog/[a-z0-9-]+)(?=\s*\n)', r'\1"', text, flags=re.I)
    if text!=original:
        path.write_text(text,encoding='utf-8'); changed+=1
print(f'files_changed={changed}')
