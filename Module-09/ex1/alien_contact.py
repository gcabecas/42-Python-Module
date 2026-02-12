from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type is ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals require a received message")
        return self


def display_contact(contact: AlienContact) -> None:
    print("Valid contact created:")
    print(f"ID: {contact.contact_id}")
    print(f"Timestamp: {contact.timestamp}")
    print(f"Location: {contact.location}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Signal Strength: {contact.signal_strength}")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: {contact.message_received}")
    print(f"Verified: {'Yes' if contact.is_verified else 'No'}\n")


def main() -> None:
    data = [
        {
            'contact_id': 'AC_2024_001',
            'timestamp': '2024-01-20T00:00:00',
            'location': 'Atacama Desert, Chile',
            'contact_type': 'visual',
            'signal_strength': 9.6,
            'duration_minutes': 99,
            'witness_count': 11,
            'message_received': 'Greetings from Zeta Reticuli',
            'is_verified': False
        },
        {
            'contact_id': 'AC_2024_002',
            'timestamp': '2024-08-20T00:00:00',
            'location': 'Mauna Kea Observatory, Hawaii',
            'contact_type': 'telepathic',
            'signal_strength': 5.6,
            'duration_minutes': 152,
            'witness_count': 1,
            'message_received': None,
            'is_verified': False
        }]

    print("Alien Contact Log Validation")

    for contact_data in data:
        try:
            print("========================================")
            display_contact(AlienContact(**contact_data))
        except ValidationError as e:
            print(f"Error creating contact: {e}")


if __name__ == "__main__":
    main()
