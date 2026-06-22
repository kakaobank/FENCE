# Building the Dataset Step by Step

The full pipeline is also available as individual steps, so you can run (or re-run) any stage on its own.

```bash
# Step 1: Download raw Pixabay images to raw/
uv run poe download-images

# Step 2 (optional): Replace placeholders with aliases → csv_alias/
uv run poe replace-placeholder

# Step 3: Generate dataset images to imgs/
uv run poe generate-dataset
```

`uv run poe download-images` downloads images concurrently. Failed downloads are skipped and reported at the end. Re-run the command to retry any failures.

> **Note:** Pixabay API has rate limits, so some downloads may fail with `429 Too Many Requests`. This is normal — see [Pixabay Images](pixabay.md) for details and retry instructions.

## All Tasks

| Command | Description |
|---------|-------------|
| `uv run poe all` | Full pipeline: download + replace-placeholder + generate |
| `uv run poe dataset` | Quick pipeline: download + generate (no placeholder) |
| `uv run poe download-images` | Download Pixabay images to `raw/` |
| `uv run poe list-missing` | Export missing images to `missing_images.csv` |
| `uv run poe replace-placeholder` | Replace placeholders with aliases → `csv_alias/` |
| `uv run poe generate-dataset` | Generate all image types to `imgs/` |
| `uv run poe clean-alias` | Remove the `csv_alias/` directory |
| `uv run poe` | Show available tasks |
