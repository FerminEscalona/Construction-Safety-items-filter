# Model sharing and Colab setup

This project uses Google Colab for YOLO training and demo inference. Model weights are not committed to the repository. Share them through Google Drive so every team member can run the notebook without retraining.

## Recommended Drive folder

Create and share this folder in Google Drive:

```text
construction-safety-ppe/
  yolo_runs/
    ppe_yolov8s_recall_focus/
      weights/
        best.pt
        last.pt
      results.csv
      results.png
      confusion_matrix.png
      PR_curve.png
      F1_curve.png
  yolo/
    ppe_data.yaml
  baseline_initial_artifacts/
  predictions/
```

Only `best.pt` is required to run inference and the Gradio demo. The other files are useful for reporting, validation, and review.

## How teammates should connect the shared folder

1. Open the shared `construction-safety-ppe` folder in Google Drive.
2. Add it as a shortcut to `My Drive`.
3. Open `ppe_object_detection_yolo.ipynb` in Google Colab.
4. Use a GPU runtime.
5. Keep this setting in the first notebook cell:

```python
USE_GOOGLE_DRIVE = True
```

The notebook expects the improved model at:

```text
/content/drive/MyDrive/construction-safety-ppe/yolo_runs/ppe_yolov8s_recall_focus/weights/best.pt
```

## Verification cell

Run this in Colab after mounting Drive:

```python
from pathlib import Path

model_path = Path(
    "/content/drive/MyDrive/construction-safety-ppe/"
    "yolo_runs/ppe_yolov8s_recall_focus/weights/best.pt"
)

print("Model exists:", model_path.exists())
print("Model path:", model_path)
```

If it prints `True`, the notebook can run evaluation, inference, and the Gradio demo without retraining.

## What the notebook downloads automatically

The notebook downloads the image dataset with `kagglehub`, so teammates do not need to manually share the dataset.

The notebook installs the minimum Colab dependencies:

```text
ultralytics
kagglehub
pyyaml
gradio
```

## What not to share

Do not share or commit:

- `.venv/`
- local cache folders
- temporary Colab runtime folders outside Drive
- large unneeded training artifacts
- private datasets or credentials

## Troubleshooting

If `best.pt` is not found:

- Confirm the shared folder was added as a shortcut to `My Drive`.
- Confirm the folder name is exactly `construction-safety-ppe`.
- Confirm the file is under `yolo_runs/ppe_yolov8s_recall_focus/weights/best.pt`.
- Re-run the first notebook cell to mount Google Drive.

If the Gradio demo starts but predictions look empty:

- Lower the confidence threshold to `0.15`.
- Confirm the selected model is `ppe_yolov8s_recall_focus/weights/best.pt`.
- Try one of the included test examples before using a new image.

If the notebook loses variables such as `OUTPUT_BASE`:

- Re-run the environment setup cell.
- Re-run the dataset preparation cell.
- Then run the evaluation, inference, or demo cells again.
