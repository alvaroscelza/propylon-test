from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.data_structures import TreeNode

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

# Create a SQLAlchemy model to represent the tree
Base = declarative_base()

# Create a SQLite database and add the tree data
engine = create_engine('sqlite:///tree.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/api/tree/<int:element_id>', methods=['GET'])
def get_tree(element_id):
    element = session.query(TreeNode).filter_by(id=element_id).first()
    parent_chapter_number = '.'.join(element.chapter_number.split('.'))
    children_nodes = session.query(TreeNode).filter(
        TreeNode.chapter_number.like(f"{parent_chapter_number}%")
    ).limit(20)
    # create response
    response = []
    for child in children_nodes:
        response.append({'name': child.name, 'level': child.level})
    return response


if __name__ == '__main__':
    app.run(debug=True)
