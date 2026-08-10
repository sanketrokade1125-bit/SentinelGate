from datetime import datetime, timedelta, UTC

from backend.app.database import SessionLocal, init_db
from backend.app.models.asset import Asset
from backend.app.models.security_event import SecurityEvent


def seed_security_events():
    init_db()

    db = SessionLocal()

    try:
        existing_events = db.query(SecurityEvent).count()

        if existing_events > 0:
            print("Security events already exist. No new events were added.")
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

        if not all([
            web_server,
            database_server,
            employee_laptop,
            cloud_vm
        ]):
            print("Required assets were not found.")
            print("Run the asset seed script first.")
            return

        base_time = datetime.now(UTC)

        events = [
            # Normal activity
            SecurityEvent(
                timestamp=base_time,
                event_type="Successful Login",
                source_ip="192.168.1.20",
                destination_ip=employee_laptop.ip_address,
                severity="LOW",
                description="Normal employee login.",
                asset_id=employee_laptop.id,
            ),

            # Brute-force sequence
            SecurityEvent(
                timestamp=base_time + timedelta(seconds=10),
                event_type="Failed Login",
                source_ip="203.0.113.50",
                destination_ip=web_server.ip_address,
                severity="LOW",
                description="Failed authentication attempt.",
                asset_id=web_server.id,
            ),

            SecurityEvent(
                timestamp=base_time + timedelta(seconds=20),
                event_type="Failed Login",
                source_ip="203.0.113.50",
                destination_ip=web_server.ip_address,
                severity="LOW",
                description="Repeated failed authentication attempt.",
                asset_id=web_server.id,
            ),

            SecurityEvent(
                timestamp=base_time + timedelta(seconds=30),
                event_type="Failed Login",
                source_ip="203.0.113.50",
                destination_ip=web_server.ip_address,
                severity="MEDIUM",
                description="Multiple failed authentication attempts detected.",
                asset_id=web_server.id,
            ),

            SecurityEvent(
                timestamp=base_time + timedelta(seconds=40),
                event_type="Failed Login",
                source_ip="203.0.113.50",
                destination_ip=web_server.ip_address,
                severity="MEDIUM",
                description="Continued authentication failures.",
                asset_id=web_server.id,
            ),

            SecurityEvent(
                timestamp=base_time + timedelta(seconds=50),
                event_type="Failed Login",
                source_ip="203.0.113.50",
                destination_ip=web_server.ip_address,
                severity="HIGH",
                description="High frequency of failed login attempts.",
                asset_id=web_server.id,
            ),

            SecurityEvent(
                timestamp=base_time + timedelta(seconds=60),
                event_type="Successful Login",
                source_ip="203.0.113.50",
                destination_ip=web_server.ip_address,
                severity="HIGH",
                description="Successful login following repeated failures.",
                asset_id=web_server.id,
            ),

            # Port scanning
            SecurityEvent(
                timestamp=base_time + timedelta(minutes=2),
                event_type="Port Scan",
                source_ip="198.51.100.25",
                destination_ip=cloud_vm.ip_address,
                severity="MEDIUM",
                description="Multiple network ports probed.",
                asset_id=cloud_vm.id,
            ),

            SecurityEvent(
                timestamp=base_time + timedelta(minutes=2, seconds=5),
                event_type="Port Scan",
                source_ip="198.51.100.25",
                destination_ip=cloud_vm.ip_address,
                severity="MEDIUM",
                description="Repeated port probing activity.",
                asset_id=cloud_vm.id,
            ),

            SecurityEvent(
                timestamp=base_time + timedelta(minutes=2, seconds=10),
                event_type="Port Scan",
                source_ip="198.51.100.25",
                destination_ip=cloud_vm.ip_address,
                severity="HIGH",
                description="Continued network reconnaissance activity.",
                asset_id=cloud_vm.id,
            ),

            # Suspicious web activity
            SecurityEvent(
                timestamp=base_time + timedelta(minutes=3),
                event_type="Suspicious HTTP Request",
                source_ip="198.51.100.80",
                destination_ip=web_server.ip_address,
                severity="HIGH",
                description="Potentially malicious HTTP request detected.",
                asset_id=web_server.id,
            ),

            # Database activity
            SecurityEvent(
                timestamp=base_time + timedelta(minutes=4),
                event_type="Database Authentication Failure",
                source_ip="10.0.0.101",
                destination_ip=database_server.ip_address,
                severity="MEDIUM",
                description="Database authentication failed.",
                asset_id=database_server.id,
            ),
        ]

        db.add_all(events)
        db.commit()

        print(f"Successfully added {len(events)} development security events.")

        for event in events:
            print(
                f"  [{event.id}] "
                f"{event.event_type} | "
                f"Severity: {event.severity} | "
                f"Asset ID: {event.asset_id}"
            )

    except Exception as error:
        db.rollback()
        print(f"Error while seeding security events: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_security_events()