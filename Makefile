.PHONY: help download-images list-missing replace-placeholder generate-dataset clean-alias all dataset

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  all                  Full pipeline (download + replace-placeholder + generate)"
	@echo "  dataset              Quick pipeline (download + generate, no placeholder)"
	@echo "  download-images      Download Pixabay images to raw/"
	@echo "  list-missing         Export missing images to missing_images.csv"
	@echo "  replace-placeholder  Replace anonymized placeholders in CSVs"
	@echo "  generate-dataset     Generate all image types to imgs/"
	@echo "  clean-alias          Remove csv_alias/"

download-images:
	chmod +x scripts/download_pixabay_images.py
	uv run python scripts/download_pixabay_images.py

list-missing:
	uv run python scripts/download_pixabay_images.py --list-missing

replace-placeholder:
	chmod +x scripts/replace_placeholder.py
	uv run python scripts/replace_placeholder.py

generate-dataset:
	chmod +x scripts/generate_dataset.py
	uv run python scripts/generate_dataset.py

clean-alias:
	rm -rf csv_alias/

all: download-images replace-placeholder generate-dataset

dataset: download-images generate-dataset
