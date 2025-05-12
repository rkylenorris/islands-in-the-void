from .schema import PsycheBase
from sqlalchemy import Column, Integer, Text, DateTime, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship


class Aspect(PsycheBase):
    __tablename__ = "aspects"
    id = Column(Integer, primary_key=True)      
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    presence = Column(Integer, nullable=False)
    visible = Column(Boolean, nullable=False)
    
    primary_conflicts = relationship("Conflict", foreign_keys="Conflict.aspect_id", back_populates="aspect")
    opposing_conflicts = relationship("Conflict", foreign_keys="Conflict.opposes_id", back_populates="opposes")
    
    
class Conflict(PsycheBase):
    __tablename__ = "conflicts"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    strength = Column(Float)
    
    aspect_id = Column(Integer, ForeignKey('psyche.aspects.id'), nullable=False)
    opposes_id = Column(Integer, ForeignKey('psyche.aspects.id'), nullable=False)
    
    aspect = relationship('Aspect', foreign_keys=[aspect_id], back_populates="primary_conflicts")
    opposes = relationship("Aspect", foreign_keys=[opposes_id], back_populates="opposing_conflicts")
    

class ThresholdEvent(PsycheBase):
    __tablename___ = "threshold_events"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    threshold_value = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    dialogue_prompt_id = Column(Integer, ForeignKey('story.dialogue_prompts.id'))
    
    