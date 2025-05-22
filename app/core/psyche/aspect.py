from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple

DISPLAY_NAME_RANGES = {"Falling": -10, "Rising": 10}

class Aspect(ABC):
    """
    Abstract base class for all aspects in the Psyche framework.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.presence: int = 0
        self.hidden: bool = False
    
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
    

    @abstractmethod
    def get_aspect_type(self) -> str:
        """
        Returns the type of the aspect.
        """
        pass

    @abstractmethod
    def get_aspect_data(self) -> Dict[str, Any]:
        """
        Returns the data associated with the aspect.
        """
        pass

    @abstractmethod
    def set_aspect_data(self, data: Dict[str, Any]) -> None:
        """
        Sets the data associated with the aspect.
        """
        pass