import pathlib, sys

def replace_nbsp(path: pathlib.Path):
    try:
        txt = path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)
        return
    if '\u00a0' in txt:
        new_txt = txt.replace('\u00a0', ' ')
        try:
            path.write_text(new_txt, encoding='utf-8')
            print(f"Cleaned NBSP in {path}")
        except Exception as e:
            print(f"Error writing {path}: {e}", file=sys.stderr)

def main():
    root = pathlib.Path('.')
    for p in root.rglob('*'):
        if p.suffix.lower() in {'.md', '.tex', '.yml'}:
            replace_nbsp(p)

if __name__ == '__main__':
    main()
