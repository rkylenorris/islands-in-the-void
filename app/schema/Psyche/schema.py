from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

player_metadata = MetaData(schema="psyche")
PsycheBase = declarative_base(metadata=player_metadata)

