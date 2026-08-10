from backend.app.services.risk_engine import calculate_risk


def main():
    test_cases = [
        {
            "name": "Critical Internet-Exposed Vulnerability",
            "cvss_score": 9.0,
            "epss_score": 0.81,
            "kev": True,
            "asset_criticality": 5,
            "internet_exposed": True,
        },
        {
            "name": "Medium Internal Vulnerability",
            "cvss_score": 6.5,
            "epss_score": 0.18,
            "kev": False,
            "asset_criticality": 5,
            "internet_exposed": False,
        },
        {
            "name": "Low Risk Endpoint Vulnerability",
            "cvss_score": 3.0,
            "epss_score": 0.05,
            "kev": False,
            "asset_criticality": 2,
            "internet_exposed": False,
        },
    ]

    for test in test_cases:
        result = calculate_risk(
            cvss_score=test["cvss_score"],
            epss_score=test["epss_score"],
            kev=test["kev"],
            asset_criticality=test["asset_criticality"],
            internet_exposed=test["internet_exposed"],
        )

        print("\n" + "=" * 55)
        print(test["name"])
        print("=" * 55)

        print(f"Risk Score : {result['risk_score']}")
        print(f"Risk Level : {result['risk_level']}")

        print("\nBreakdown:")
        for factor, points in result["breakdown"].items():
            print(f"  {factor}: {points}")


if __name__ == "__main__":
    main()