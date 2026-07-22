# NovaMart definitions

Synthetic e-commerce dataset, generated for teaching. No real people, no real company.

`users.csv`, one row per user, 50,000 rows.

| Column | Meaning |
|---|---|
| `user_id` | Unique user |
| `signup_date` | Date the account was created |
| `days_since_signup` | Days from `signup_date` to 2026-05-01 |
| `acquisition_channel` | Marketing channel, recorded at signup |
| `country` | Country, recorded at signup |
| `device_primary` | Main device, recorded at signup |
| `used_save_for_later` | 1 if the user has ever used the Save for Later feature |
| `product_views` | Total product views across the user's whole history |
| `sessions` | Total sessions across the user's whole history |
| `ever_purchased` | 1 if the user has ever placed an order, any status |

## Metric definitions of record

- **buyer**: `ever_purchased = 1`.
- **saver**: `used_save_for_later = 1`.
- **tenure**: `days_since_signup`.
- **purchase impact** of a feature: the effect the feature causes. Decisions about promoting,
  building, or funding a feature are made on purchase impact.
