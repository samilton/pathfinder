from datetime import datetime, timedelta
from typing import Dict

from pydantic import BaseModel


class Lease(BaseModel):
    hostname: str
    token: str
    expiration: datetime


class LeaseManager(BaseModel):
    _leases: Dict[str, Lease]

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls._leases = dict()
            cls.instance = super(LeaseManager, cls).__new__(cls)
        return cls.instance

    def calculate_expiration(self):
        return datetime.now() + timedelta(hours=2)

    def renew(self, hostname: str):
        if hostname in self.leases:
            lease = self.leases[hostname]
            self.calculate_expiration()
            self.leases[hostname] = lease
            return lease
