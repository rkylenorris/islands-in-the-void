from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

DISPLAY_NAME_RANGES = {"Falling": -10, "Rising": 10}

@dataclass
class AspectAbility(ABC):
    """
    Class representing an ability associated with an aspect.
    """
    name: str
    description: str
    effect: str
    unlock_level: int
    
    def __init__(self, name: str, description: str, effect: str, unlock_level: int):
        self.name = name
        self.description = description
        self.effect = effect
        self.unlock_level = unlock_level
    
        
    @abstractmethod
    def apply_effect(self, target: Any) -> None:
        """
        Apply the effect of the ability to the target.
        """
        pass

    


class Aspect(ABC):
    """
    Abstract base class for all aspects in the Psyche framework.
    """

    def __init__(self, name: str, description: str, ability: Optional[AspectAbility] = None):
        self.name = name
        self.description = description
        self.presence: int = 0
        self.hidden: bool = False
        self.ability: Optional[AspectAbility] = ability
    
    @property
    def polarity(self) -> str:
        """
        Returns the polarity of the aspect.
        """
        polarity = "positive" if self.presence > 0 else "negative"
        if self.presence == 0:
            polarity = "neutral"
        return polarity
    
    @property
    def display_name(self) -> str:
        """
        Returns the display name of the aspect.
        """
        adjective = ""
        for key, val in DISPLAY_NAME_RANGES.items():
            if val > 0:
                if self.presence > val:
                    adjective = key
                    break
            elif val < 0:
                if self.presence < val:
                    adjective = key
                    break
        else:
            adjective = "Neutral"
        
        if self.hidden:
            adjective = "Hidden"
            
        return f"{adjective} {self.name}"
    
    def __str__(self) -> str:
        return f"{self.display_name}: {self.presence}"
    

    def modify_presence(self, amount: int) -> None:
        self.presence += amount