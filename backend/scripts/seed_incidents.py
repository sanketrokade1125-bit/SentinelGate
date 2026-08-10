from datetime import datetime, UTC

from backend.app.database import SessionLocal, init_db
from backend.app.models.asset import Asset
from backend.app.models.incident import Incident


def seed_incidents():
    init_db()

    db = SessionLocal()

    try:
        existing_incidents = db.query(Incident).count()

        if existing_incidents > 0:
            print("Incidents already exist. No new incidents were added.")
            return

        web_server = (
            db.query(Asset)
            .filter(Asset.name == "Web Server 01")
            .first()
        )

        cloud_vm = (
            db.query(Asset)
            .filter(Asset.name == "Cloud VM 01")
            .first()
        )

        database_server = (
            db.query(Asset)
            .filter(Asset.name == "Database Server 01")
            .first()
        )

        if not all([web_server, cloud_vm, database_server]):
            print("Required assets were not found.")
            print("Run the asset seed script first.")
            return

        now = datetime.now(UTC)

        incidents = [
            Incident(
                title="Possible Brute Force Attack",
                attack_type="Brute Force",
                severity="HIGH",
                risk_score=91.0,
                status="OPEN",
                description=(
                    "Multiple failed login attempts from the same source "
                    "were followed by a successful login."
                ),
                asset_id=web_server.id,
                created_at=now,
            ),

            Incident(
                title="Network Reconnaissance Detected",
                attack_type="Port Scan",
                severity="MEDIUM",
                risk_score=68.0,
                status="INVESTIGATING",
                description=(
                    "Repeated port scanning activity was detected "
                    "against an internet-exposed cloud VM."
                ),
                asset_id=cloud_vm.id,
                created_at=now,
            ),

            Incident(
                title="Suspicious Web Activity",
                attack_type="Web Attack",
                severity="HIGH",
                risk_score=82.0,
                status="OPEN",
                description=(
                    "A potentially malicious HTTP request was detected "
                    "against the public web server."
                ),
                asset_id=web_server.id,
                created_at=now,
            ),

            Incident(
                title="Database Authentication Anomaly",
                attack_type="Authentication Anomaly",
                severity="MEDIUM",
                risk_score=61.0,
                status="OPEN",
                description=(
                    "A database authentication failure was detected "
                    "and requires investigation."
                ),
                asset_id=database_server.id,
                created_at=now,
            ),
        ]

        db.add_all(incidents)
        db.commit()

        print(f"Successfully added {len(incidents)} development incidents.")

        for incident in incidents:
            print(
                f"  [{incident.id}] "
                f"{incident.title} | "
                f"Type: {incident.attack_type} | "
                f"Severity: {incident.severity} | "
                f"Risk: {incident.risk_score} | "
                f"Status: {incident.status}"
            )

    except Exception as error:
        db.rollback()
        print(f"Error while seeding incidents: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_incidents()