#!/usr/bin/env python3
"""Test script to validate Docker setup and database connection."""

import asyncio
import sys

from sqlalchemy import text

from app.core.config import settings
from app.db.base import AsyncSessionLocal, init_db


async def test_database_connection() -> None:
    """Test database connection and basic operations."""
    print("🔍 Testing database connection...")

    try:
        # Test database initialization
        await init_db()
        print("✅ Database initialization successful")

        # Test session creation
        async with AsyncSessionLocal() as session:
            # Test basic query
            await session.execute(text("SELECT 1"))
            print("✅ Database query successful")

            # Test User model
            user_count = await session.execute(text("SELECT COUNT(*) FROM users"))
            count = user_count.scalar()
            print(f"✅ User table accessible, current count: {count}")

    except Exception as e:
        print(f"❌ Database test failed: {e}")
        sys.exit(1)


async def test_user_crud() -> None:
    """Test user CRUD operations."""
    print("\n🔍 Testing User CRUD operations...")

    try:
        from app.crud.user import user

        async with AsyncSessionLocal() as session:
            # Test user creation
            user_data = {
                "email": "test@example.com",
                "password": "testpassword123",
                "full_name": "Test User",
                "is_active": True,
            }

            created_user = await user.create(session, obj_in=user_data)
            print(f"✅ User created: {created_user.email}")

            # Test user retrieval
            retrieved_user = await user.get(session, id=created_user.id)
            if retrieved_user:
                print(f"✅ User retrieved: {retrieved_user.email}")
            else:
                print("❌ User retrieval failed")
                return

            # Test user update
            update_data = {"full_name": "Updated Test User"}
            updated_user = await user.update(
                session, db_obj=retrieved_user, obj_in=update_data
            )
            print(f"✅ User updated: {updated_user.full_name}")

            # Test user deletion
            await user.remove(session, id=created_user.id)
            print("✅ User deleted")

    except Exception as e:
        print(f"❌ User CRUD test failed: {e}")
        sys.exit(1)


async def main() -> None:
    """Main test function."""
    print("🚀 Starting Docker setup validation...")
    print(f"📊 Database URL: {settings.DATABASE_URL}")
    print(f"🌍 Environment: {settings.ENVIRONMENT}")

    await test_database_connection()
    await test_user_crud()

    print("\n🎉 All tests passed! Docker setup is working correctly.")


if __name__ == "__main__":
    asyncio.run(main())
