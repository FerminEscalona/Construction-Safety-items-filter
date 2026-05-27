# Guía del repositorio

## Estructura del proyecto y organización de módulos

Este repositorio contiene la documentación y los notebooks de un proyecto de detección de EPP en seguridad para construcción. La descripción principal está en `README.md`; la normalización de texto del repositorio está configurada en `.gitattributes`.

Mantén una estructura predecible:

- `src/` para código de aplicación, lógica reutilizable y pipelines del modelo.
- `tests/` para pruebas automatizadas que reflejen los módulos de `src/`.
- `data/` solo para metadatos pequeños de muestra; no comprometas datasets grandes.
- `assets/` o `docs/` para diagramas, imágenes de muestra y documentación de apoyo.
- `models/` para configuración del modelo o metadatos livianos, no para pesos entrenados grandes.

## Comandos de configuración, pruebas y desarrollo

El entorno local usa Python y notebooks. Antes de entregar cambios, revisa el estado del repositorio:

```sh
git status --short
```

Para validar la lógica reutilizable, ejecuta:

```sh
python -m pytest
```

Cuando agregues nuevos flujos, documenta en `README.md` los comandos exactos de instalación, ejecución y validación.

## Estilo de código y convenciones de nombres

Usa nombres claros y específicos del dominio de seguridad en construcción y detección de EPP, como `helmet_detector`, `vest_compliance` o `ppe_violation_report`. Prefiere módulos pequeños con una sola responsabilidad.

Para Markdown, usa títulos en español, párrafos concisos y listas con guiones. Mantén las líneas legibles y evita comprometer archivos generados salvo que sean artefactos necesarios del proyecto. El repositorio usa normalización LF mediante `.gitattributes`.

## Lineamientos de pruebas

Las pruebas deben vivir en `tests/` y nombrarse según el comportamiento o módulo verificado, por ejemplo `test_ppe_labels.py` o `test_detection_pipeline.py`.

Para visión por computador, incluye pruebas de parseo de datos, mapeo de etiquetas, umbrales de confianza y casos límite como clases de EPP faltantes o detecciones vacías. Evita pruebas que requieran datasets locales grandes, salvo que uses fixtures pequeños comprometidos de forma intencional.

## Lineamientos de commits y pull requests

Los commits existentes usan mensajes cortos e imperativos, por ejemplo `Add README with project overview and objectives`. Mantén ese estilo: empieza con un verbo, conserva el asunto conciso y describe un cambio lógico por commit.

Los pull requests deben incluir un resumen breve, la razón del cambio, la validación realizada y cualquier supuesto sobre datos o modelo. Para cambios visuales o de comportamiento del modelo, incluye ejemplos representativos, métricas o capturas cuando sea práctico.

## Seguridad y configuración

No comprometas credenciales, datasets privados de imágenes, binarios de modelos entrenados ni rutas específicas del entorno local. Usa archivos de configuración locales ignorados para secretos y documenta las variables requeridas en `README.md` cuando aparezcan.
