import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.data_structures import Base, TreeNode

# Load the JSON file
with open('tree.json', 'r') as f:
    file_content = json.load(f)
    documents = file_content['data']['content']['docs']

# Create a SQLite database and add the tree data
engine = create_engine('sqlite:///tree.db', connect_args={'check_same_thread': False})
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
