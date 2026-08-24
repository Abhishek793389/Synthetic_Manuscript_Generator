# Synthetic_Manuscript_Generator

# Synthetic Manuscript Generator

An automated Python pipeline for generating realistic synthetic historical Indic manuscript folios with synchronized ground-truth annotations.

The project generates manuscript-style images from raw Indic-script text and produces a corresponding Markdown (`.md`) annotation file for every image.

The pipeline currently supports:

- Sharada
- Devanagari
- Modi

Each script can generate 100 synthetic manuscript images, producing a total dataset of 300 images.

---

## Project Overview

The goal of this project is to create synthetic historical manuscript data suitable for OCR research and training.

The pipeline combines:

1. Aged handmade-paper backgrounds
2. Historical manuscript-style text layouts
3. Indic script rendering
4. Ink/color variation
5. Text alignment irregularities
6. Manuscript highlights
7. Marginal annotations
8. Section markers and punctuation
9. Paper stains and aging
10. Ink bleeding and fading
11. Folds and physical wear
12. Synchronized text bounding boxes
13. Markdown ground-truth annotations

Each generated manuscript image has a matching `.md` annotation file containing the source text, metadata, and bounding boxes.

---

# Supported Scripts

| Script | Font | Images |
|---|---|---:|
| Sharada | Noto Sans Sharada | 100 |
| Devanagari | Noto Sans Devanagari | 100 |
| Modi | Noto Sans Modi | 100 |
| **Total** | | **300** |

The architecture is configurable and can be extended to additional Indic scripts by adding the appropriate input text and font.

---

# Dataset

The synthetic dataset contains:

- **300 manuscript images**
- **300 corresponding Markdown annotation files**
- **100 images per script**

For each script:

- 85 training images
- 10 validation images
- 5 test images

### Dataset Distribution

| Script | Train | Validation | Test | Total |
|---|---:|---:|---:|---:|
| Sharada | 85 | 10 | 5 | 100 |
| Devanagari | 85 | 10 | 5 | 100 |
| Modi | 85 | 10 | 5 | 100 |
| **Total** | **255** | **30** | **15** | **300** |

---

# Hugging Face Dataset

The generated dataset is hosted separately from the source code on Hugging Face.

**Dataset name:**

`YOUR_HF_DATASET_NAME`

**Hugging Face repository:**

`https://huggingface.co/datasets/YOUR_USERNAME/YOUR_HF_DATASET_NAME`

The dataset contains three script subsets:

```text
sharada
devanagari
modi
