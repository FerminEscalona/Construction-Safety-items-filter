# Detección de EPP para seguridad en construcción

## Contexto del negocio

Las obras de construcción son entornos de alto riesgo. Los trabajadores están expuestos a caída de objetos, maquinaria pesada, vehículos en movimiento, polvo, escombros y condiciones de visibilidad limitadas. Para reducir accidentes, las empresas exigen el uso de elementos de protección personal (EPP), como cascos, chalecos de seguridad, mascarillas y otros equipos.

Aun con políticas de seguridad definidas, monitorear el cumplimiento del uso de EPP sigue siendo difícil. La supervisión manual depende de inspectores, recorridos periódicos y disponibilidad humana. Esto puede ser costoso, inconsistente y poco escalable en obras grandes o múltiples sedes.

Este proyecto explora el uso de visión por computador para apoyar a los equipos de seguridad en la detección de EPP e incumplimientos visibles en imágenes de obras.

## Problema de negocio

Las empresas constructoras necesitan reducir accidentes y mejorar el cumplimiento de normas de seguridad ocupacional. Sin embargo, la supervisión manual puede verse limitada por disponibilidad, visibilidad y dinamismo del entorno.

Un sistema capaz de detectar EPP e incumplimientos desde imágenes puede ayudar a identificar riesgos de manera más rápida y consistente.

## Objetivo del negocio

El objetivo es construir un flujo de detección de objetos que identifique personas, elementos de EPP y posibles incumplimientos en imágenes de construcción.

El sistema busca detectar clases como `Person`, `Hardhat`, `Safety Vest`, `Mask`, `NO-Hardhat`, `NO-Mask` y `NO-Safety Vest`, y convertir esas detecciones en un reporte operativo de cumplimiento.

## Valor esperado

El proyecto puede aportar valor mediante:

- Identificación más rápida de posibles incumplimientos.
- Mayor visibilidad del cumplimiento de EPP en zonas de obra.
- Apoyo a auditorías de seguridad.
- Reducción de dependencia de inspecciones completamente manuales.
- Priorización de casos que requieren revisión humana.
- Trazabilidad para decisiones de seguridad ocupacional.

## Usuarios potenciales

Los usuarios principales podrían ser:

- Responsables de seguridad y salud en el trabajo.
- Supervisores de obra.
- Equipos de cumplimiento y auditoría.
- Gerentes de operaciones.
- Equipos de gestión de riesgo.

## Caso de uso

Una empresa constructora podría cargar imágenes o capturar fotografías de una obra para detectar trabajadores, EPP visible e incumplimientos. Cuando el sistema identifica una posible condición insegura, genera un reporte con la causa y la ubicación aproximada en la imagen.

El objetivo no es reemplazar la supervisión humana, sino proporcionar una capa adicional de apoyo para mejorar velocidad, consistencia y cobertura.

## Alcance

El proyecto se enfoca en detección de objetos y análisis de cumplimiento visible en imágenes. No implementa todavía monitoreo continuo en video, despliegue productivo, integración con cámaras reales ni alertas automáticas en obra.

## Estado del proyecto

El proyecto está en etapa de prototipo avanzado. Incluye:

- Análisis exploratorio inicial del dataset.
- Notebook de clasificación binaria como línea base histórica.
- Notebook principal de detección multiclase con YOLO.
- Entrenamiento y evaluación de `yolov8n` y `yolov8s`.
- Demo interactiva con Gradio para cargar imagen o usar cámara.
- Reglas de cumplimiento por persona en `src/ppe_compliance.py`.
- Pruebas unitarias para la lógica de cumplimiento.
- Guía para compartir pesos del modelo por Google Drive.

El clasificador binario queda como referencia, pero el enfoque recomendado para uso real es detección multiclase más reglas de cumplimiento.

## Configuración local

Usa Python 3.11 o 3.12. En esta máquina Windows, el entorno local se configuró con `.venv`.

En PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name construction-safety-ppe --display-name "Construction Safety PPE"
```

Después abre los notebooks y selecciona el kernel `Construction Safety PPE`.

## Flujo de trabajo en Google Colab

Para entrenar YOLO se recomienda Google Colab con GPU.

1. Abre `ppe_object_detection_yolo.ipynb` con la extensión de Google Colab o directamente en Colab.
2. Selecciona un entorno de ejecución con GPU.
3. Ejecuta la primera celda de entorno; en Colab instala `ultralytics`, `kagglehub`, `pyyaml` y `gradio`.
4. Mantén `USE_GOOGLE_DRIVE = True` para conservar pesos, resultados y artefactos en Drive.
5. Verifica que exista el modelo en la ruta descrita en `MODEL_SHARING.md`.

Las dependencias mínimas de Colab están en `requirements-colab.txt`.

## Flujo recomendado

1. Ejecuta `eda_initial_dataset_analysis.ipynb` para inspeccionar el dataset bajo `css-data`.
2. Ejecuta `ppe_object_detection_yolo.ipynb` para entrenar, evaluar y comentar el detector YOLO.
3. Usa `src/ppe_compliance.py` para convertir detecciones en reportes de cumplimiento.
4. Usa la sección de demo interactiva para mostrar el modelo con imágenes cargadas o cámara.
5. Consulta `MODEL_SHARING.md` para compartir los pesos con el equipo.

## Impacto del negocio

Una solución exitosa puede contribuir a obras más seguras al detectar condiciones de riesgo de manera temprana. También puede apoyar auditorías, reducir tiempos de revisión y mejorar la cultura de prevención.

El sistema debe usarse como apoyo a la supervisión humana, no como mecanismo automático de sanción.
