# Storefront definitions

Synthetic dataset, generated for teaching. No real people, no real company.

`visitors.csv`, one row per visitor, 50,000 rows.

| Column | Meaning | Fixed when |
|---|---|---|
| `user_id` | Unique visitor | signup |
| `primary_device` | The device they mostly use: web, ios, android | signup |
| `platform` | `primary_device` collapsed to desktop or mobile | signup |
| `acquired_via` | Marketing channel they arrived through | signup |
| `market` | Country | signup |
| `joined_on` | Date they first signed up | signup |
| `orders_placed` | Count of orders over their whole history | after |
| `has_ordered` | 1 if they have ever placed an order | after |

## Metric definitions of record

- **orderer** = `has_ordered = 1`. At least one order, ever. **Cumulative**: no time window, so it
  accrues with how long someone has been around.
- **order rate** = share of a group with `has_ordered = 1`.
- **platform effect** = the difference a platform *causes*, not the raw gap between people who happen
  to use one and people who happen to use the other.

## Cautions

- `orders_placed` and `has_ordered` are measured over the visitor's whole history, so neither can be
  used as evidence about what was true before they chose a platform.
- Visitors are not randomly assigned to a platform. They choose. Nothing here can establish a causal
  platform effect on its own.
- Pre-behaviour variables available for a comparability check: `acquired_via`, `market`, `joined_on`.
