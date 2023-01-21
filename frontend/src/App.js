import React, { useState, useEffect } from 'react';

function TreeView() {
  const [treeData, setTreeData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch('http://127.0.0.1:5000/api/tree/1');
      const data = await response.json();
      setTreeData(data);
    }
    fetchData();
  }, []);

  return (
    <ul>
      {treeData.map((node) => (
        <li key={node.id}>
          {node.name}
          {node.children && (
            <TreeView data={node.children} />
          )}
        </li>
      ))}
    </ul>
  );
}

export default TreeView;
