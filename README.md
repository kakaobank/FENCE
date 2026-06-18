<h1 align="center">FENCE: A Financial and Multimodal Jailbreak Detection Dataset</h1>

<p align="center">
  A benchmark dataset of 1,000 multimodal queries (500 harmful / 500 benign) across 5 image types for evaluating VLM safety against jailbreak attacks in the financial domain.
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2602.18154"><img src="https://img.shields.io/badge/arXiv-2602.18154-b31b1b?logo=arxiv&logoColor=white" alt="arXiv"></a>
  <a href="https://lrec2026.info/"><img src="https://img.shields.io/badge/LREC%202026-Accepted-orange" alt="LREC 2026"></a>
  <a href="#"><img src="https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=white" alt="Python 3.12+"></a>
  <a href="https://pixabay.com/service/license-summary/"><img src="https://img.shields.io/badge/images-Pixabay%20License-green" alt="Pixabay License"></a>
</p>

<p align="center">
  <a href="https://lrec.elra.info/lrec2026-main-712"><b>[Paper]</b></a> &ensp;
  <a href="http://www.lrec-conf.org/proceedings/lrec2026/pdf/2026.lrec2026-1.712.pdf"><b>[PDF]</b></a>
</p>

---

## Overview

**FENCE** is a benchmark dataset for evaluating the safety of VLMs against multimodal jailbreak attacks in the financial domain.

- **1,000 queries** — 500 harmful and 500 benign
- **967 unique images** spanning 5 types: `baseimg`, `textimg`, `eng_textimg`, `figstep`, and `eng_figstep`
- **Multimodal** inputs combining text and image
- Built-in **placeholder system** for anonymizing financial entities

## Repository Structure

See [Repository Structure](assets/structure.md) for the full directory layout.

## Quick Start

### 1. Clone & Navigate

```bash
git clone https://github.com/kakaobank/FENCE.git
cd FENCE
```

### 2. Prerequisites

Install [uv](https://docs.astral.sh/uv/) (the only required tool):

<details>
<summary><b>macOS</b></summary>

```bash
brew install uv
```
</details>

<details>
<summary><b>Linux (Debian/Ubuntu)</b></summary>

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
</details>

### 3. Install Dependencies

```bash
uv sync
```

### 4. Configure Environment

```bash
cp .env.example .env
```

Set the following keys in `.env`:

| Key | Description | Required |
|-----|-------------|:--------:|
| `PIXABAY_API_KEY` | API key for downloading Pixabay images | Yes |

### 5. Build Dataset

Tasks are defined in `pyproject.toml` and run via [`poe`](https://poethepoet.natn.io/) (`uv run poe <task>`).

**Full pipeline** (with placeholder replacement):

```bash
uv run poe all
```

**Quick pipeline** (without placeholder replacement):

```bash
uv run poe dataset
```

To run each stage individually, see the [full task list](assets/build.md)

## Examples

Sample images from each of the 5 image types (benign queries shown).

<table>
<tr>
<td align="center" colspan="2"><h3><code>baseimg</code></h3></td>
</tr>
<tr>
<td align="center" colspan="2">
<img src="assets/examples/baseimg.jpg" width="400">
</td>
</tr>
<tr>
<td align="center" colspan="2"><b>Korean</b></td>
</tr>
<tr>
<td align="center" width="50%"><h3><code>textimg</code></h3></td>
<td align="center" width="50%"><h3><code>figstep</code></h3></td>
</tr>
<tr>
<td align="center"><img src="assets/examples/textimg.jpg" width="380"></td>
<td align="center"><img src="assets/examples/figstep.jpg" width="380"></td>
</tr>
<tr>
<td align="center" colspan="2"><b>English</b></td>
</tr>
<tr>
<td align="center"><h3><code>eng_textimg</code></h3></td>
<td align="center"><h3><code>eng_figstep</code></h3></td>
</tr>
<tr>
<td align="center"><img src="assets/examples/eng_textimg.jpg" width="380"></td>
<td align="center"><img src="assets/examples/eng_figstep.jpg" width="380"></td>
</tr>
</table>

## Documentation

| Topic | Description |
|-------|-------------|
| [Dataset Reference](assets/dataset.md) | CSV columns, `input_query` vs `query`, and the image types |
| [Pixabay Images](assets/pixabay.md) | Which images to download and how to fetch them |
| [Placeholder System](assets/placeholder.md) | Anonymizing entity names and replacing placeholders |

## Citation

If you find this dataset useful, please cite our paper:

```bibtex
@inproceedings{kim2026fence,
    title     = {FENCE: A Financial and Multimodal Jailbreak Detection Dataset},
    author    = {Kim, Mirae and Jeong, Seonghun and Kwak, Youngjun},
    booktitle = {Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)},
    year      = {2026},
    doi       = {10.63317/4a35sc6sgwwv},
    url       = {https://lrec.elra.info/lrec2026-main-712}
}
```

## License

Dataset annotations and non-Pixabay images are provided under the [CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.

Pixabay-sourced images are subject to the [Pixabay License](https://pixabay.com/service/license-summary/).
