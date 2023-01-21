from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TreeNode(Base):
    __tablename__ = 'tree_nodes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)
    parent_id = Column(Integer, ForeignKey('tree_nodes.id'))
