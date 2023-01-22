import React, {useState} from 'react';

function TreeView({data = [], level = 0}) {
    const [treeData, setTreeData] = useState(data);
    const [elementId, setElementId] = useState(1);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch(`http://127.0.0.1:5000/api/tree/${elementId}`);
        const data = await response.json();
        setTreeData(data);
    };

    return (<div>
        <form onSubmit={handleSubmit}>
            <label>
                Element Id:
                <input
                    type="number"
                    value={elementId}
                    onChange={e => setElementId(e.target.value)}
                />
            </label>
            <button type="submit">Submit</button>
        </form>
        <ul>
            {treeData.map(node => (
                <li key={node.id}>
                    {"\t".repeat(node.level)} {node.name}
                </li>
            ))}
        </ul>
    </div>);
}

export default TreeView;
