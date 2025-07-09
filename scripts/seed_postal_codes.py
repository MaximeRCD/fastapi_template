"""Seed Parisian postal codes data."""

import asyncio

from app.crud.postal_code import postal_code
from app.db.base import get_db


async def seed_postal_codes() -> None:
    """Seed the database with Parisian postal codes."""
    # Parisian postal codes data
    parisian_postal_codes = [
        {"postal_code": "75001", "city_name": "Paris 1er"},
        {"postal_code": "75002", "city_name": "Paris 2e"},
        {"postal_code": "75003", "city_name": "Paris 3e"},
        {"postal_code": "75004", "city_name": "Paris 4e"},
        {"postal_code": "75005", "city_name": "Paris 5e"},
        {"postal_code": "75006", "city_name": "Paris 6e"},
        {"postal_code": "75007", "city_name": "Paris 7e"},
        {"postal_code": "75008", "city_name": "Paris 8e"},
        {"postal_code": "75009", "city_name": "Paris 9e"},
        {"postal_code": "75010", "city_name": "Paris 10e"},
        {"postal_code": "75011", "city_name": "Paris 11e"},
        {"postal_code": "75012", "city_name": "Paris 12e"},
        {"postal_code": "75013", "city_name": "Paris 13e"},
        {"postal_code": "75014", "city_name": "Paris 14e"},
        {"postal_code": "75015", "city_name": "Paris 15e"},
        {"postal_code": "75016", "city_name": "Paris 16e"},
        {"postal_code": "75017", "city_name": "Paris 17e"},
        {"postal_code": "75018", "city_name": "Paris 18e"},
        {"postal_code": "75019", "city_name": "Paris 19e"},
        {"postal_code": "75020", "city_name": "Paris 20e"},
    ]

    async for db in get_db():
        print("Seeding Parisian postal codes...")

        for postal_code_data in parisian_postal_codes:
            # Check if postal code already exists
            existing = await postal_code.get_by_postal_code(
                db, postal_code=postal_code_data["postal_code"]
            )
            if not existing:
                await postal_code.create(db, obj_in=postal_code_data)
                print(
                    f"Added: {postal_code_data['postal_code']} - {postal_code_data['city_name']}"
                )
            else:
                print(
                    f"Already exists: {postal_code_data['postal_code']} - {postal_code_data['city_name']}"
                )

        print("Postal codes seeding completed!")
        break


if __name__ == "__main__":
    asyncio.run(seed_postal_codes())
