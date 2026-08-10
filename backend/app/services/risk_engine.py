def calculate_risk(
    cvss_score: float | None,
    epss_score: float | None,
    kev: bool,
    asset_criticality: int,
    internet_exposed: bool,
) -> dict:
    """
    Calculate an explainable cybersecurity risk score.

    Maximum score = 100.

    Factors:
    - CVSS: 30 points
    - EPSS: 25 points
    - KEV: 20 points
    - Asset criticality: 15 points
    - Internet exposure: 10 points
    """

    cvss_score = cvss_score or 0.0
    epss_score = epss_score or 0.0

    # Keep values inside their expected ranges.
    cvss_score = max(0.0, min(cvss_score, 10.0))
    epss_score = max(0.0, min(epss_score, 1.0))
    asset_criticality = max(1, min(asset_criticality, 5))

    # Individual risk contributions.
    cvss_points = (cvss_score / 10.0) * 30.0
    epss_points = epss_score * 25.0
    kev_points = 20.0 if kev else 0.0
    criticality_points = (asset_criticality / 5.0) * 15.0
    exposure_points = 10.0 if internet_exposed else 0.0

    total_score = (
        cvss_points
        + epss_points
        + kev_points
        + criticality_points
        + exposure_points
    )

    total_score = round(min(total_score, 100.0), 2)

    if total_score >= 80:
        risk_level = "CRITICAL"
    elif total_score >= 60:
        risk_level = "HIGH"
    elif total_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_score": total_score,
        "risk_level": risk_level,
        "breakdown": {
            "cvss_points": round(cvss_points, 2),
            "epss_points": round(epss_points, 2),
            "kev_points": round(kev_points, 2),
            "asset_criticality_points": round(criticality_points, 2),
            "internet_exposure_points": round(exposure_points, 2),
        },
    }