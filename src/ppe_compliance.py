from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Detection:
    class_name: str
    confidence: float
    box_xyxy: tuple[float, float, float, float]


@dataclass(frozen=True)
class PersonCompliance:
    person_index: int
    person_box_xyxy: tuple[float, float, float, float]
    detected_ppe: tuple[str, ...]
    violations: tuple[str, ...]
    status: str


@dataclass(frozen=True)
class ComplianceReport:
    status: str
    person_count: int
    violation_count: int
    persons: tuple[PersonCompliance, ...]
    unassigned_violations: tuple[str, ...]


VIOLATION_TO_REQUIRED_PPE = {
    "NO-Hardhat": "Hardhat",
    "NO-Mask": "Mask",
    "NO-Safety Vest": "Safety Vest",
}


def generate_ppe_compliance_report(
    detections: Iterable[Detection],
    *,
    person_class: str = "Person",
    ppe_classes: tuple[str, ...] = ("Hardhat", "Mask", "Safety Vest"),
    required_ppe_classes: tuple[str, ...] = ("Hardhat", "Safety Vest"),
    violation_classes: tuple[str, ...] = tuple(VIOLATION_TO_REQUIRED_PPE),
    min_confidence: float = 0.25,
) -> ComplianceReport:
    filtered = [det for det in detections if det.confidence >= min_confidence]
    persons = [det for det in filtered if det.class_name == person_class]
    ppe_items = [det for det in filtered if det.class_name in ppe_classes]
    violations = [det for det in filtered if det.class_name in violation_classes]

    person_reports: list[PersonCompliance] = []
    assigned_violation_ids: set[int] = set()

    for person_index, person in enumerate(persons, start=1):
        person_ppe = tuple(
            sorted(
                {
                    item.class_name
                    for item in ppe_items
                    if _center_inside(item.box_xyxy, person.box_xyxy)
                }
            )
        )
        person_violations = tuple(
            sorted(
                {
                    violation.class_name
                    for violation in violations
                    if _center_inside(violation.box_xyxy, person.box_xyxy)
                }
            )
        )

        for violation_id, violation in enumerate(violations):
            if violation.class_name in person_violations and _center_inside(
                violation.box_xyxy, person.box_xyxy
            ):
                assigned_violation_ids.add(violation_id)

        if person_violations:
            person_status = "inseguro"
        elif all(required_ppe in person_ppe for required_ppe in required_ppe_classes):
            person_status = "cumple_epp_basico"
        else:
            person_status = "requiere_revision"

        person_reports.append(
            PersonCompliance(
                person_index=person_index,
                person_box_xyxy=person.box_xyxy,
                detected_ppe=person_ppe,
                violations=person_violations,
                status=person_status,
            )
        )

    unassigned_violations = tuple(
        sorted(
            violations[index].class_name
            for index in range(len(violations))
            if index not in assigned_violation_ids
        )
    )

    violation_count = sum(len(person.violations) for person in person_reports) + len(
        unassigned_violations
    )
    if violation_count:
        status = "inseguro"
    elif person_reports and all(
        person.status == "cumple_epp_basico" for person in person_reports
    ):
        status = "cumple_epp_basico"
    else:
        status = "requiere_revision" if person_reports else "sin_personas_detectadas"

    return ComplianceReport(
        status=status,
        person_count=len(person_reports),
        violation_count=violation_count,
        persons=tuple(person_reports),
        unassigned_violations=unassigned_violations,
    )


def _center_inside(
    item_box: tuple[float, float, float, float],
    container_box: tuple[float, float, float, float],
) -> bool:
    x1, y1, x2, y2 = item_box
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    left, top, right, bottom = container_box
    return left <= cx <= right and top <= cy <= bottom
