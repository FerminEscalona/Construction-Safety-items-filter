# Guía para compartir el modelo y ejecutar en Colab

Este proyecto usa Google Colab para entrenar YOLO y ejecutar la demo interactiva. Los pesos del modelo no deben subirse al repositorio. La forma recomendada de compartirlos con el equipo es mediante Google Drive.

## Carpeta recomendada en Drive

Crea y comparte esta carpeta en Google Drive:

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

Para ejecutar inferencia y la demo de Gradio solo es obligatorio compartir:

```text
yolo_runs/ppe_yolov8s_recall_focus/weights/best.pt
```

Los demás archivos son útiles para revisar resultados, métricas, curvas y artefactos visuales.

## Cómo conectar la carpeta compartida

Cada integrante del equipo debe:

1. Abrir la carpeta compartida `construction-safety-ppe` en Google Drive.
2. Agregarla como acceso directo a `Mi unidad`.
3. Abrir `ppe_object_detection_yolo.ipynb` en Google Colab.
4. Seleccionar un entorno de ejecución con GPU.
5. Mantener esta configuración en la primera celda del notebook:

```python
USE_GOOGLE_DRIVE = True
```

El notebook espera encontrar el modelo mejorado en:

```text
/content/drive/MyDrive/construction-safety-ppe/yolo_runs/ppe_yolov8s_recall_focus/weights/best.pt
```

## Celda de verificación

Ejecuta esto en Colab después de montar Drive:

```python
from pathlib import Path

model_path = Path(
    "/content/drive/MyDrive/construction-safety-ppe/"
    "yolo_runs/ppe_yolov8s_recall_focus/weights/best.pt"
)

print("Existe el modelo:", model_path.exists())
print("Ruta del modelo:", model_path)
```

Si imprime `True`, el notebook puede ejecutar evaluación, inferencia y la demo de Gradio sin reentrenar.

## Qué descarga automáticamente el notebook

El notebook descarga el dataset con `kagglehub`, así que no es necesario compartir manualmente las imágenes.

También instala las dependencias mínimas de Colab:

```text
ultralytics
kagglehub
pyyaml
gradio
```

## Qué no se debe compartir ni subir al repositorio

No compartas ni confirmes en Git:

- `.venv/`
- carpetas de caché locales
- carpetas temporales de Colab fuera de Drive
- artefactos grandes que no sean necesarios
- datasets privados
- credenciales o tokens

## Solución de problemas

Si `best.pt` no aparece:

- Confirma que la carpeta compartida fue agregada como acceso directo a `Mi unidad`.
- Confirma que el nombre sea exactamente `construction-safety-ppe`.
- Confirma que el archivo esté en `yolo_runs/ppe_yolov8s_recall_focus/weights/best.pt`.
- Ejecuta de nuevo la primera celda del notebook para montar Google Drive.

Si la demo de Gradio abre, pero no muestra detecciones:

- Baja el umbral de confianza a `0.15`.
- Confirma que el modelo seleccionado sea `ppe_yolov8s_recall_focus/weights/best.pt`.
- Prueba primero con uno de los ejemplos incluidos en el notebook.

Si el notebook pierde variables como `OUTPUT_BASE`:

- Ejecuta de nuevo la celda de configuración del entorno.
- Ejecuta de nuevo la celda de preparación del dataset.
- Luego ejecuta evaluación, inferencia o demo otra vez.
