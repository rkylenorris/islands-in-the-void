from dataclasses import dataclass

@dataclass
class Item:
    name: str
    description: str
    hidden: bool
    aspect_effect: dict[str, int]
    
    def __init__(self, name: str, description: str, hidden: bool, aspect_effect: dict[str, int]):
        self.name = name
        self.description = description
        self.hidden = hidden
        self.aspect_effect = aspect_effect if len(aspect_effect) > 0 else {}
        
    def touch_item(self) -> str:
        return f"You touched the {self.name}.\n{self.description}" if not self.hidden else f"The {self.name} is hidden. You can't touch it."


@dataclass
class Room:
    title: str
    theme: str
    description: str
    items: list[Item]
    
    def __init__(self, title: str, theme: str, description: str, items: list[dict]):
        self.title = title
        self.theme = theme
        self.description = description
        self.items = [Item(**item) for item in items] if len(items) > 0 else []
        
    def __str__(self) -> str:
        return f"The {self.title}: {self.theme} theme\n{self.description}\nItems: {', '.join([item.name for item in self.items if not item.hidden])}" if len(self.items) > 0 else f"The {self.title}: {self.theme} theme\n{self.description}\nNo items in this room."
    
    
@dataclass
class RoomAction:
    name: str
    description: str
    effect: str
    def __init__(self, name: str, description: str, effect: str):
        self.name = name
        self.description = description
        self.effect = effect