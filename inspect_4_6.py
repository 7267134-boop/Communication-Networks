import re

for fname in ['4.html', '6.html']:
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    print(f"=== {fname} ===")
    
    # Find all h2, h3 or sub-chapter titles
    h2s = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', c, re.DOTALL)
    seen = set()
    for h in h2s:
        clean = re.sub(r'<[^>]+>', '', h).strip()
        clean = ' '.join(clean.split())
        if clean and clean not in seen and len(clean) > 5:
            seen.add(clean)
            if any(char.isdigit() for char in clean[:5]):
                print(" ", clean[:90])

