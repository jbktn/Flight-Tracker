import React, { useEffect, useState } from 'react';
import '../App.css';

let data = require('../Mock_Balice_incoming.json');
for (let i = 0; i < data.length; i++) {
    data[i] = JSON.parse(data[i]);
}
console.log(data[0]);
console.log(typeof data[0]);

const Table: React.FC = () => { 
    const [tableData, setTableData] = useState<any[]>([]);

    useEffect(() => {
        setTableData(data);
    }, []);

    return (
        <div>
            <table className='Table_v1' id='Table'>
                <tbody>
                {tableData.map((row, index) => (
                <tr key={index}>
                    <td>{row.Time}</td>
                    <td>{row.Destination}</td>
                    <td>{row.Airline}</td>
                    <td>{row.Code}</td>
                    <td>{row.Status}</td>
                    <td><a href={row.Link}>Link</a></td>
                </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}

export default Table;