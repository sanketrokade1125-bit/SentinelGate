from backend.app.database import SessionLocal, init_db
from backend.app.models.asset import Asset


def seed_assets():
    init_db()

    db = SessionLocal()

    try:
        # Prevent duplicate seed data
        existing_assets = db.query(Asset).count()

        if existing_assets > 0:
            print("Assets already exist. No new assets were added.")
            return

        assets = [
            Asset(
                name="Web Server 01",
                asset_type="Server",
                ip_address="10.0.0.10",
                criticality=5,
                internet_exposed=True,
                owner="Web Team",
            ),
            Asset(
                name="Database Server 01",
                asset_type="Database",
                ip_address="10.0.0.20",
                criticality=5,
                internet_exposed=False,
                owner="Database Team",
            ),
            Asset(
                name="Employee Laptop 01",
                asset_type="Laptop",
                ip_address="10.0.0.101",
                criticality=3,
                internet_exposed=False,
                owner="IT Team",
            ),
            Asset(
                name="Cloud VM 01",
                asset_type="Cloud VM",
                ip_address="10.0.0.30",
                criticality=4,
                internet_exposed=True,
                owner="Cloud Team",
            ),
        ]

        db.add_all(assets)
        db.commit()

        print("Successfully added 4 assets.")

        for asset in assets:
            print(
                f"  [{asset.id}] {asset.name} "
                f"| Criticality: {asset.criticality} "
                f"| Internet Exposed: {asset.internet_exposed}"
            )

    except Exception as error:
        db.rollback()
        print(f"Error while seeding assets: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_assets()