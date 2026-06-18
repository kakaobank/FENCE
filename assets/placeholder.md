# Placeholder System

The dataset provides 93 placeholder mappings for anonymizing financial entity names.

| Placeholder | Example |
|-------------|---------|
| `[BANK_X]` | Haneul Bank, Byeolbit Bank, Dasom Bank |
| `[SERVICE_X]` | Banking service names (KR/EN) |
| `[APP_X]` | Mobile app names |
| `[BRAND_X]` | Brand names |

```bash
# Run placeholder replacement
uv run poe replace-placeholder

# Check the output
ls csv_alias/
```
