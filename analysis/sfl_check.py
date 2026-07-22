"""Save for Later vs buyer rate: raw gap + comparability check (NovaMart definitions.md)."""
import csv
from collections import defaultdict

rows = []
with open('datasets/novamart/users.csv') as f:
    for r in csv.DictReader(f):
        rows.append({
            'tenure': int(r['days_since_signup']),
            'channel': r['acquisition_channel'],
            'country': r['country'],
            'device': r['device_primary'],
            'saver': int(r['used_save_for_later']),
            'buyer': int(r['ever_purchased']),
        })

savers = [r for r in rows if r['saver']]
nons = [r for r in rows if not r['saver']]

def rate(g):
    return sum(r['buyer'] for r in g) / len(g) if g else float('nan')

def mean(g, k):
    return sum(r[k] for r in g) / len(g)

print(f"n={len(rows)}  savers={len(savers)}  non-savers={len(nons)}")
print(f"buyer rate | savers:     {rate(savers):.3f}")
print(f"buyer rate | non-savers: {rate(nons):.3f}")
print(f"raw gap: {(rate(savers) - rate(nons)) * 100:+.1f} pts")

print("\n-- Pre-behaviour balance --")
print(f"mean tenure | savers: {mean(savers, 'tenure'):.0f} d   non-savers: {mean(nons, 'tenure'):.0f} d")
for var in ('channel', 'country', 'device'):
    def dist(g):
        d = defaultdict(int)
        for r in g:
            d[r[var]] += 1
        return {k: v / len(g) for k, v in d.items()}
    ds, dn = dist(savers), dist(nons)
    keys = sorted(set(ds) | set(dn))
    print(var + ':  ' + '  '.join(f"{k} {ds.get(k, 0):.2f}/{dn.get(k, 0):.2f}" for k in keys))

print("\n-- Buyer rate within tenure buckets (saver / non-saver / gap) --")
qs = sorted(r['tenure'] for r in rows)
cuts = [qs[len(qs) // 4], qs[len(qs) // 2], qs[3 * len(qs) // 4]]

def bucket(t):
    for i, c in enumerate(cuts):
        if t <= c:
            return i
    return len(cuts)

labels = [f"<= {cuts[0]}d", f"{cuts[0]+1}-{cuts[1]}d", f"{cuts[1]+1}-{cuts[2]}d", f"> {cuts[2]}d"]
gaps = []
for i, lab in enumerate(labels):
    s = [r for r in rows if r['saver'] and bucket(r['tenure']) == i]
    n = [r for r in rows if not r['saver'] and bucket(r['tenure']) == i]
    g = (rate(s) - rate(n)) * 100
    gaps.append((g, len(s) + len(n)))
    print(f"{lab:>12}:  {rate(s):.3f} (n={len(s)})  /  {rate(n):.3f} (n={len(n)})  /  {g:+.1f} pts")

w = sum(g * n for g, n in gaps) / sum(n for _, n in gaps)
print(f"\nraw gap: {(rate(savers) - rate(nons)) * 100:+.1f} pts   within-tenure-bucket gap (weighted): {w:+.1f} pts")

print("\n-- Saver share by tenure bucket --")
for i, lab in enumerate(labels):
    b = [r for r in rows if bucket(r['tenure']) == i]
    print(f"{lab:>12}:  saver share {sum(r['saver'] for r in b) / len(b):.2f},  buyer rate {rate(b):.3f}")
