from backend.app.database import SessionLocal, init_db
from backend.app.models.asset import Asset
from backend.app.models.vulnerability import Vulnerability


def seed_vulnerabilities():
    init_db()

    db = SessionLocal()

    try:
        existing_vulnerabilities = db.query(Vulnerability).count()

        if existing_vulnerabilities > 0:
            print("Vulnerabilities already exist. No new vulnerabilities were added.")
            return

        web_server = (
            db.query(Asset)
            .filter(Asset.name == "Web Server 01")
            .first()
        )

        database_server = (
            db.query(Asset)
            .filter(Asset.name == "Database Server 01")
            .first()
        )

        employee_laptop = (
            db.query(Asset)
            .filter(Asset.name == "Employee Laptop 01")
            .first()
        )

        cloud_vm = (
            db.query(Asset)
            .filter(Asset.name == "Cloud VM 01")
            .first()
        )

        if not all([web_server, database_server, employee_laptop, cloud_vm]):
            print("Required assets were not found.")
            print("Run the asset seed script first.")
            return

        vulnerabilities = [
            Vulnerability(
                cve_id="CVE-DEV-0001",
                description="Development vulnerability affecting the public web server.",
                cvss_score=9.8,
                epss_score=0.91,
                kev=True,
                risk_score=95.0,
                asset_id=web_server.id,
            ),
            Vulnerability(
                cve_id="CVE-DEV-0002",
                description="Development vulnerability affecting the public web server.",
                cvss_score=7.5,
                epss_score=0.32,
                kev=False,
                risk_score=65.0,
                asset_id=web_server.id,
            ),
            Vulnerability(
                cve_id="CVE-DEV-0003",
                description="Development vulnerability affecting the database server.",
                cvss_score=8.8,
                epss_score=0.74,
                kev=True,
                risk_score=88.0,
                asset_id=database_server.id,
            ),
            Vulnerability(
                cve_id="CVE-DEV-0004",
                description="Development vulnerability affecting the database server.",
                cvss_score=6.5,
                epss_score=0.18,
                kev=False,
                risk_score=48.0,
                asset_id=database_server.id,
            ),
            Vulnerability(
                cve_id="CVE-DEV-0005",
                description="Development vulnerability affecting an employee endpoint.",
                cvss_score=7.2,
                epss_score=0.27,
                kev=False,
                risk_score=55.0,
                asset_id=employee_laptop.id,
            ),
            Vulnerability(
                cve_id="CVE-DEV-0006",
                description="Development vulnerability affecting an internet-exposed cloud VM.",
                cvss_score=9.0,
                epss_score=0.81,
                kev=True,
                risk_score=91.0,
                asset_id=cloud_vm.id,
            ),
        ]

        db.add_all(vulnerabilities)
        db.commit()

        print("Successfully added 6 development vulnerabilities.")

        for vulnerability in vulnerabilities:
            print(
                f"  [{vulnerability.id}] "
                f"{vulnerability.cve_id} | "
                f"CVSS: {vulnerability.cvss_score} | "
                f"EPSS: {vulnerability.epss_score} | "
                f"KEV: {vulnerability.kev} | "
                f"Risk: {vulnerability.risk_score}"
            )

    except Exception as error:
        db.rollback()
        print(f"Error while seeding vulnerabilities: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_vulnerabilities()