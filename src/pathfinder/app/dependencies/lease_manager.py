from app.internal.lease_manager import LeaseManager, Lease
from typing import Dict


def get_lease_manager() -> LeaseManager:
    return LeaseManager()
