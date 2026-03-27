import requests
from sqlalchemy.orm import Session
from models.customer import Customer

FLASK_API_URL = "http://mock-server:5000/api/customers"


def fetch_all_customers():
    page = 1
    limit = 10
    all_data = []

    while True:
        response = requests.get(
            f"{FLASK_API_URL}?page={page}&limit={limit}"
        )

        data = response.json()

        customers = data.get("data", [])

        if not customers:
            break

        all_data.extend(customers)
        page += 1

    return all_data


def upsert_customers(db: Session, customers):
    count = 0

    for c in customers:
        existing = db.query(Customer).filter_by(
            customer_id=c["customer_id"]
        ).first()

        if existing:
            # Update
            for key, value in c.items():
                setattr(existing, key, value)
        else:
            # Insert
            new_customer = Customer(**c)
            db.add(new_customer)

        count += 1

    db.commit()
    return count