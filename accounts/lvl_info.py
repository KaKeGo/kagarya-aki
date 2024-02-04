from enum import Enum


class LevelInfo(Enum):
    NEW_MEMBER = (1, 10, '#E0FFFF', 'Nowy Użytkownik')

    def __init__(self, min_level, max_level, color, title):
        self.min_level = min_level
        self.max_level = max_level
        self.color = color
        self.title = title

    @classmethod
    def get_info_for_level(cls, level):
        for level_info in cls:
            if level_info.min_level <= level <= level_info.max_level:
                return level_info.color, level_info.title
        return None, None
