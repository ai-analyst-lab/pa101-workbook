# Storefront definitions

Synthetic dataset, generated for teaching. No real people, no real company.

`visitors.csv`, one row per visitor, 50,000 rows.

| Column | Meaning |
|---|---|
| `user_id` | Unique visitor |
| `primary_device` | The device they mostly use: web, ios, android |
| `platform` | `primary_device` grouped into desktop or mobile |
| `acquired_via` | Marketing channel, recorded at signup |
| `market` | Country, recorded at signup |
| `joined_on` | Date they first signed up |
| `orders_placed` | Total orders across the visitor's whole history |
| `has_ordered` | 1 if the visitor has ever placed an order |

## Metric definitions of record

- **orderer**: `has_ordered = 1`.
- **order rate**: share of a group with `has_ordered = 1`.
- **platform effect**: the difference a platform causes. Decisions about platform investment are
  made on platform effect.
