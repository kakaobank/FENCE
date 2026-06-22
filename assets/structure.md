# Repository Structure

```
FENCE/
├── csv/                          # Benchmark CSV files
│   ├── FENCE_benchmark.csv           # Harmful queries (500 rows)
│   └── FENCE_benchmark_benign.csv    # Benign queries (500 rows)
├── csv_alias/                    # Generated: anonymized CSV output
├── raw/                          # Downloaded: raw Pixabay images
├── imgs/                         # Generated: final dataset images
│   ├── baseimg/                      # Base images (copied from raw)
│   │   └── harmful/                  # Harmful context base images
│   ├── figstep/                      # Korean screenshot-style images
│   ├── eng_figstep/                  # English screenshot-style images
│   ├── textimg/                      # Korean text-overlay images
│   └── eng_textimg/                  # English text-overlay images
├── templates/                    # Template images for figstep generation
│   ├── template1.png / template3.png     # Korean templates
│   └── template2.png / template4.png     # English templates
├── fonts/                        # Font files
│   └── NanumGothic-Regular.ttf       # Korean font
├── scripts/                      # Utility scripts
│   ├── download_pixabay_images.py    # Pixabay image downloader
│   ├── generate_dataset.py          # Dataset image generator
│   └── replace_placeholder.py       # Placeholder replacement script
├── placeholder/                  # Anonymization mapping files
│   └── placeholder_alias.json       # Alias mappings (82 entries)
├── assets/                       # Example images and supplementary docs
├── pyproject.toml
└── .env.example
```
