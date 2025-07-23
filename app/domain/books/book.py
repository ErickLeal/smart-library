from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Book:
    id: Optional[int]
    title: str
    author: str
    year: int
    pages: int = 0
    is_old: bool = field(default=False)
    is_big: bool = field(default=False)

    def process_extra_info(self):
        self.is_old = self.year < 2000
        self.is_big = self.pages > 1000
