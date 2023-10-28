import React, { useState, useEffect } from 'react';
import axios from 'axios';
import IoTDataTable from './IoTDataTable';



function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Effectuez la requête API pour récupérer les données IoTData
    axios.get('/api/admin/data')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Erreur lors de la requête API :', error);
      });
  }, []);

  return (
    <div className="App">
      <IoTDataTable data={data} />     
      
    </div>
  );
}

export default App;
