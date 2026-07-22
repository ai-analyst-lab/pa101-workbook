# NovaMart definitions

Synthetic e-commerce dataset, generated for teaching. No real people, no real company.

`users.csv`, one row per user, 50,000 rows.

| Column | Meaning |
|---|---|
| `user_id` | Unique user |
| `signup_date` | When they joined |
| `days_since_signup` | Tenure in days, as of 2026-05-01 |
| `acquisition_channel`, `country`, `device_primary` | Fixed at signup |
| `used_save_for_later` | 1 if the user has ever used Save for Later |
| `product_views`, `sessions` | Lifetime totals, measured across the user's whole history |
| `ever_purchased` | 1 if the user has ever placed an order, any status |

## Metric definitions of record

- **buyer** = `ever_purchased = 1`. At least one order, any status, ever. **Cumulative**: no time
  window, so longer-tenured users have had more opportunity to qualify.
- **saver** = `used_save_for_later = 1`.
- **tenure** = `days_since_signup`. Fixed at signup, so it is a valid pre-behaviour variable.
- **purchase impact** of a feature = the effect it *causes*, not the raw difference between users
  who used it and users who did not.

## Cautions

- `product_views` and `sessions` are lifetime totals. They include activity that happened *after* a
  user first saved something, so they cannot be used to argue savers were more active beforehand.
- There is no randomized experiment in this dataset. Nothing here can establish causality on its
  own.
