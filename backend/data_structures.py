from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TreeNode(Base):
    __tablename__ = 'tree_nodes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    chapter_number = Column(String)
    level = Column(Integer)
