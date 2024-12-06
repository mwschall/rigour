import re
from typing import Optional
from rigour.ids.common import IdentifierFormat

UEI_RE = re.compile(r"\b([0-9ABCDEFGHJKLMNPQRSTUVWXYZ]{12})\b", re.I)


class UEI(IdentifierFormat):
    """US GSA Unique Entity ID."""

    TITLE: str = "NPI"
    STRONG: bool = True
    # https://www.gsa.gov/about-us/organization/federal-acquisition-service/integrated-award-environment-iae/iae-systems-information-kit/uei-technical-specifications-and-api-information

    @classmethod
    def is_valid(cls, text: str) -> bool:
        """Determine if the given string is a valid NPI."""
        print("XXX", text)
        if UEI_RE.match(text) is None:
            return False

        if text.startswith("0"):
            return False

        # TODO: Figure out checksum scheme
        return True

    @classmethod
    def normalize(cls, text: str) -> Optional[str]:
        """Normalize the given string to a valid NPI."""
        match = UEI_RE.search(text)
        if match is None:
            return None
        value = match.group(1)
        if not cls.is_valid(value):
            return None
        return value.upper()

    @classmethod
    def format(cls, value: str) -> str:
        return value.upper()
