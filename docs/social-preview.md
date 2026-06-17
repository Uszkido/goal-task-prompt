# Social Preview Asset

GitHub lets repository owners upload a PNG, JPG, or GIF social preview image in repository settings. The recommended high-quality size is 1280x640.

This repo includes a ready-to-upload PNG and a source SVG:

```text
assets/social-preview.png
assets/social-preview.svg
```

Upload the PNG in GitHub:

```text
Repository Settings -> Social preview -> Edit -> Upload an image
```

Regenerate it when the visual changes:

```bash
python3 scripts/generate_social_preview.py
```

Suggested caption:

```text
Goal Task Prompt: turn fuzzy agent requests into verifiable /goal prompts.
```
