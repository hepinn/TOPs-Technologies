import React from 'react';
import { Routes, Route } from 'react-router-dom';

const UserProfile = () => <div>User Profile Page</div>;

const User = () => {
  return (
    <div>
      <h1>User Dashboard</h1>
      <Routes>
        <Route path="/user/profile" element={<UserProfile />} />
        {/* Other user routes */}
      </Routes>
    </div>
  );
};

export default User;
