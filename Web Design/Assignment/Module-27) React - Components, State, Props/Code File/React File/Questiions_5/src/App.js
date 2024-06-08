import React, { useState } from 'react';
import TableComponent from './TableComponent';
import SearchComponent from './SearchComponent';

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredData, setFilteredData] = useState([]);

  const data = [
    { name: 'Hepin', age: 21, email: 'hepin@example.com' },
    { name: 'Mihir', age: 21, email: 'mihir@example.com' },
    { name: 'Aditya', age: 25, email: 'aditya@example.com' },
    { name: 'Dhruv', age: 20, email: 'dhruv@example.com' },
    { name: 'Hasya', age: 23, email: 'hasya@example.com' },
    { name: 'Raj', age: 23, email: 'raj@example.com' },
    { name: 'Trushal', age: 23, email: 'trushal@example.com' },
    { name: 'Gautam', age: 24, email: 'gautam@example.com' },
  ];

  const handleSearch = (searchTerm) => {
    setSearchTerm(searchTerm);
    const filteredData = data.filter((item) =>
      item.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredData(filteredData);
  };

  return (
    <div>
      <h1>Table with Search</h1>
      <SearchComponent handleSearch={handleSearch} />
      <TableComponent data={searchTerm ? filteredData : data} />
    </div>
  );
};

export default App;