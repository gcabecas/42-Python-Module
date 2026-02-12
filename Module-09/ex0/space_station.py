from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def display_station(station: SpaceStation) -> None:
    status = "Operational" if station.is_operational else "Not operational"
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}\n")


def main() -> None:
    data = [{
        'station_id': 'LGW125',
        'name': 'Titan Mining Outpost',
        'crew_size': 6,
        'power_level': 76.4,
        'oxygen_level': 95.5,
        'last_maintenance': '2023-07-11T00:00:00',
        'is_operational': True,
        'notes': None
    },
        {
        'station_id': 'QCH189',
        'name': 'Deep Space Observatory',
        'crew_size': 21,
        'power_level': 70.8,
        'oxygen_level': 88.1,
        'last_maintenance': '2023-08-24T00:00:00',
        'is_operational': False,
        'notes': 'System diagnostics required'
    }]
    print("Space Station Data Validation")
    for station_data in data:
        try:
            print("========================================")
            station = SpaceStation(**station_data)
            display_station(station)
        except ValidationError as e:
            print(f"Error creating station: {e}")


if __name__ == "__main__":
    main()
