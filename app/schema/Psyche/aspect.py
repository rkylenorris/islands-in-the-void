from .schema import PsycheBase
from sqlalchemy import Column, Integer, Text, DateTime, String, Boolean, ForeignKey, Float, CheckConstraint, Enum as enm
from sqlalchemy.orm import relationship
from enum import Enum

MAX_PRESENCE: int = 50
MIN_PRESENCE: int = -50


class Aspect(PsycheBase):
    __tablename__ = "aspects"
    id = Column(Integer, primary_key=True)      
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    presence = Column(Integer, nullable=False)
    visible = Column(Boolean, nullable=False)
    
    primary_conflicts = relationship("Conflict", foreign_keys="psyche.conflicts.aspect_id", back_populates="aspect")
    opposing_conflicts = relationship("Conflict", foreign_keys="psyche.conflicts.opposes_id", back_populates="opposes")
    threshold_events = relationship('ThresholdEvent', foreign_keys="psyche.threshold_events.aspect_id", back_populates="aspect")
    
    __table_args__ = (
        CheckConstraint(f'presence BETWEEN {MIN_PRESENCE} AND {MAX_PRESENCE}', name='presence_range_check'),
    )
    
    
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
    
    
class ThresholdPolarity(Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    

class ThresholdEvent(PsycheBase):
    __tablename___ = "threshold_events"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    threshold_value = Column(Integer, nullable=False)
    threshold_polarity = Column(enm(ThresholdPolarity), nullable=False)
    
    dialogue_prompt_id = Column(Integer, ForeignKey('story.dialogue_prompts.id'))
    aspect_id = Column(Integer, ForeignKey('psyche.aspects.id'), nullable=False)
    
    aspect = relationship('Aspect', foreign_keys=[aspect_id], back_populates='threshold_events')
    
    __table_args__ = (
        CheckConstraint(f'threshold_value BETWEEN {MIN_PRESENCE} AND {MAX_PRESENCE}', name='threshold_value_range_check'),
    )
    

class Effect(PsycheBase):
    __tablename__ = 'effects'
    id = Column(Integer, primary_key=True)
    event_type = Column(String, nullable=False)
    event_id = Column(Integer, nullable=False)