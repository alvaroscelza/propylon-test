from flask import Flask, jsonify

from database_importer import TreeNode, session

app = Flask(__name__)


@app.route('/api/tree/<int:element_id>', methods=['GET'])
def get_tree(element_id):
    # retrieve children of the passed element_id
    children_nodes = session.query(TreeNode).filter_by(parent_id=element_id).limit(20)
    # create response
    response = []
    for child in children_nodes:
        response.append({'name': child.name, 'level': child.level})
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
