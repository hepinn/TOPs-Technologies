// SearchComponent.js
import React from 'react';

const SearchComponent = ({ handleSearch }) => {
  return (
    <div>
      <input
        type="text"
        placeholder="Search by name"
        onChange={(e) => handleSearch(e.target.value)}
      />
    </div>
  );
};

export default SearchComponent;
