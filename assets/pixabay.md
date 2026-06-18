# Pixabay Images

Some images are sourced from [Pixabay](https://pixabay.com/) under the **Pixabay License** and are **not included** in this repository. Run `uv run poe download-images` to fetch or resume them.

| | Rows | Unique Images |
|---|:---:|:---:|
| Pixabay (download required) | 600 | 567 |
| Local (included in repo) | 400 | 400 |
| **Total** | **1,000** | **967** |

- Already-downloaded files are skipped; duplicates are deduplicated automatically
- The downloader handles rate limits (`429`) with automatic retries
- If some downloads fail, use `uv run poe list-missing` to check remaining images, then re-run `uv run poe download-images`

> **Note:** Pixabay API has rate limits, so some downloads may fail with `429 Too Many Requests`. This is normal — just re-run the download command to retry any failures.
