import json
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load the JSON file
with open('tree.json', 'r') as f:
    file_content = json.load(f)
    documents = file_content['data']['content']['docs']

# Create a SQLAlchemy model to represent the tree
Base = declarative_base()


class TreeNode(Base):
    __tablename__ = 'tree_nodes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)
    parent_id = Column(Integer, ForeignKey('tree_nodes.id'))


# Create a SQLite database and add the tree data
engine = create_engine('sqlite:///tree.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

for document in documents:
    # create the node
    db_node = TreeNode(name=document['name'], level=document['level'])
    session.add(db_node)
    session.commit()
    # Get parent of the current node
    parent_node = session.query(TreeNode).filter_by(level=document['level']-1).first()
    # If parent exist
    if parent_node:
        # set the parent_id
        db_node.parent_id = parent_node.id
        session.commit()
