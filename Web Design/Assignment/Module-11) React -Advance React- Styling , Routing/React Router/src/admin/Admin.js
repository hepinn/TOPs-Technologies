import React from 'react';
import { Routes, Route } from 'react-router-dom';

const Users = () => <div>Admin Users Page</div>;

const Admin = () => {
  return (
    <div>
      <h1>Admin Dashboard</h1>
      <Routes>
        <Route path="/admin/users" element={<Users />} />
        {/* Other admin routes */}
      </Routes>
    </div>
  );
};

export default Admin;
