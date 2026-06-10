#!/usr/bin/env python3
"""Replace placeholder codes in CSV files with alias names."""

import argparse
import json
import re
from pathlib import Path


def load_aliases(alias_path: Path) -> dict[str, str]:
    """Load placeholder-to-alias mapping from JSON file."""
    with open(alias_path, encoding="utf-8") as f:
        return json.load(f)


def replace_placeholders(content: str, aliases: dict[str, str]) -> tuple[str, int]:
    """Replace placeholder codes with alias names.

    Keys are sorted by length descending to prevent partial matches
    (e.g., [SERVICE_A10] must be replaced before [SERVICE_A1]).

    Returns the replaced content and total replacement count.
    """
    sorted_keys = sorted(aliases.keys(), key=len, reverse=True)
    total = 0
    for key in sorted_keys:
        count = content.count(key)
        if count > 0:
            content = content.replace(key, aliases[key])
            total += count
    return content, total


def check_remaining(content: str) -> list[str]:
    """Check for any remaining unreplaced placeholder patterns."""
    pattern = r"\[(BANK|SERVICE|APP|BRAND)_[A-Z]\d+\]"
    return re.findall(pattern, content)


def main():
    parser = argparse.ArgumentParser(
        description="Replace placeholder codes in CSV files with alias names."
    )
    parser.add_argument(
        "--alias",
        type=Path,
        default=Path("placeholder/placeholder_alias.json"),
        help="Path to alias JSON file (default: placeholder/placeholder_alias.json)",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("csv"),
        help="Input directory containing CSV files (default: csv)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("csv_alias"),
        help="Output directory for replaced CSV files (default: csv_alias)",
    )
    args = parser.parse_args()

    aliases = load_aliases(args.alias)
    print(f"Loaded {len(aliases)} alias mappings from {args.alias}")

    args.output_dir.mkdir(parents=True, exist_ok=True)

    csv_files = sorted(args.input_dir.glob("*.csv"))
    if not csv_files:
        print(f"No CSV files found in {args.input_dir}")
        return

    for csv_file in csv_files:
        with open(csv_file, encoding="utf-8") as f:
            content = f.read()

        replaced, count = replace_placeholders(content, aliases)

        remaining = check_remaining(replaced)
        if remaining:
            print(f"  WARNING: {len(remaining)} unmapped placeholders in {csv_file.name}: {remaining}")

        output_path = args.output_dir / csv_file.name
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(replaced)

        print(f"  {csv_file.name} -> {output_path} ({count} replacements)")

    print("Done.")


if __name__ == "__main__":
    main()
