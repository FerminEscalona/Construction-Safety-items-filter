from src.ppe_compliance import Detection, generate_ppe_compliance_report


def test_reports_violation_associated_to_person():
    detections = [
        Detection("Person", 0.95, (0, 0, 100, 200)),
        Detection("NO-Hardhat", 0.88, (30, 10, 60, 40)),
        Detection("Safety Vest", 0.76, (20, 80, 80, 150)),
    ]

    report = generate_ppe_compliance_report(detections)

    assert report.status == "inseguro"
    assert report.person_count == 1
    assert report.violation_count == 1
    assert report.persons[0].status == "inseguro"
    assert report.persons[0].violations == ("NO-Hardhat",)
    assert report.persons[0].detected_ppe == ("Safety Vest",)


def test_ignores_low_confidence_detections():
    detections = [
        Detection("Person", 0.95, (0, 0, 100, 200)),
        Detection("NO-Safety Vest", 0.10, (20, 80, 80, 150)),
    ]

    report = generate_ppe_compliance_report(detections, min_confidence=0.25)

    assert report.status == "sin_violaciones_detectadas"
    assert report.violation_count == 0
    assert report.persons[0].violations == ()


def test_keeps_unassigned_violations_for_manual_review():
    detections = [
        Detection("Person", 0.95, (0, 0, 100, 200)),
        Detection("NO-Mask", 0.90, (150, 20, 180, 50)),
    ]

    report = generate_ppe_compliance_report(detections)

    assert report.status == "inseguro"
    assert report.violation_count == 1
    assert report.unassigned_violations == ("NO-Mask",)
