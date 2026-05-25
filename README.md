# PPE Detection for Construction Safety

## Business Context

Construction sites are high-risk environments where workers are constantly exposed to hazards such as falling objects, heavy machinery, moving vehicles, dust, debris, and restricted visibility. To reduce the likelihood of injuries and accidents, companies require workers to use Personal Protective Equipment (PPE), including helmets, safety vests, masks, and other protective gear.

Despite established safety policies, ensuring consistent PPE compliance remains a challenge. Traditional supervision depends heavily on manual inspections, safety officers, and periodic audits. These methods can be time-consuming, inconsistent, and difficult to scale across large or multiple construction sites.

This project addresses the need for a more efficient and automated way to monitor PPE compliance in construction environments. By using computer vision, the solution aims to support safety teams in identifying whether workers are properly equipped or if potential safety violations are present.

## Business Problem

Construction companies need to reduce workplace accidents and improve compliance with occupational safety standards. However, manual monitoring of PPE usage can be limited by human availability, visibility constraints, and the dynamic nature of construction sites.

A system capable of automatically identifying PPE usage from images can help organizations detect non-compliance more quickly and support preventive safety actions before incidents occur.

## Business Objective

The objective of this project is to explore the use of computer vision to detect PPE compliance in construction site images.

The system is intended to help identify whether workers are wearing required safety equipment such as helmets, masks, and safety vests, as well as detect cases where PPE may be missing.

## Expected Business Value

This project can provide value by supporting:

- Faster identification of potential safety violations.
- Improved visibility into PPE compliance across construction areas.
- Reduced dependency on fully manual safety inspections.
- Better support for safety audits and incident prevention.
- Increased awareness of unsafe working conditions.
- Data-driven decision-making for occupational health and safety teams.

## Potential Users

The main users of this type of solution could include:

- Safety managers.
- Construction site supervisors.
- Occupational health and safety teams.
- Compliance and audit teams.
- Operations managers.
- Risk management teams.

## Use Case

A construction company could use this solution to analyze images from construction sites and identify whether workers are using the required PPE. When a possible non-compliance case is detected, the system could support alerts, reports, or manual review by the safety team.

The goal is not to replace human supervision, but to provide an additional layer of support that improves the speed, consistency, and scalability of safety monitoring.

## Scope

This project focuses on the business problem of PPE compliance detection in construction environments. The initial scope includes identifying workers and visual indicators related to safety equipment usage.

The project can be extended in the future to support real-time monitoring, dashboard reporting, alert systems, compliance trends, and integration with existing safety management platforms.

## Project Status

This repository is currently in the exploratory/prototype stage. It includes:

- A business overview and project scope.
- An initial exploratory data analysis notebook.
- A binary image classification notebook for safe/unsafe PPE usage.
- A YOLO object-detection notebook for multiclase PPE detection and compliance reporting.
- A Python requirements file for notebook-based development.

The binary classifier is a baseline only. The recommended path for real-world use is object detection plus compliance rules by person.

The project does not yet include a production API, persisted trained weights, deployment configuration, or monitoring.

## Setup

Use Python 3.11 or 3.12 for this project. TensorFlow does not currently support the Python 3.14 interpreter installed on this Windows machine.

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name construction-safety-ppe --display-name "Construction Safety PPE"
```

Then open the notebooks and select the `Construction Safety PPE` kernel.

## Google Colab workflow

For YOLO training, Colab is preferred over the local Windows CPU environment.

1. Open `ppe_object_detection_yolo.ipynb` with the Google Colab extension or in Colab.
2. Select a GPU runtime.
3. Run the first environment cell; it installs `ultralytics`, `kagglehub`, and `pyyaml` when running in Colab.
4. Keep `USE_GOOGLE_DRIVE = False` for quick experiments, or set it to `True` to persist trained weights under `MyDrive/construction-safety-ppe`.

The minimal Colab dependencies are listed in `requirements-colab.txt`. The local `requirements.txt` remains useful for Windows/VS Code development.

## Recommended workflow

1. Run `eda_initial_dataset_analysis.ipynb` to inspect the YOLO dataset under `css-data`.
2. Use `ppe_object_detection_yolo.ipynb` to train and evaluate a YOLO detector over the 10 PPE classes.
3. Convert detections into a practical safety report with `src/ppe_compliance.py`.

The older `ppe_binary_classification_pipeline.ipynb` is useful as a baseline, but it compresses a multi-object detection problem into one image-level label and is not the preferred approach for field use.

## Business Impact

A successful PPE detection solution can contribute to safer construction sites by helping organizations detect unsafe conditions earlier. This can reduce operational risk, support regulatory compliance, improve safety culture, and potentially lower costs associated with workplace accidents, delays, and penalties.
