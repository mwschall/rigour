import re
from typing import Optional
from stdnum import luhn  # type: ignore

from rigour.ids.common import IdentifierFormat

NPI_RE = re.compile(r"\b(\d{10}|\d{15})\b")


class NPI(IdentifierFormat):
    """National Provider Identifier."""

    TITLE: str = "NPI"

    # cf. https://www.johndcook.com/blog/2024/06/26/npi-number/

    @classmethod
    def is_valid(cls, text: str) -> bool:
        """Determine if the given string is a valid NPI."""
        if NPI_RE.match(text) is None:
            return False

        if len(text) == 10:
            text = "80840" + text

        return bool(luhn.is_valid(text))

    @classmethod
    def normalize(cls, text: str) -> Optional[str]:
        """Normalize the given string to a valid NPI."""
        match = NPI_RE.search(text)
        if match is None:
            return None
        value = match.group(1)
        if cls.is_valid(value):
            return value
        return None
