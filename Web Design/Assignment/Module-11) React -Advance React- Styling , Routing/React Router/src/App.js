import React, { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

const Admin = lazy(() => import('./admin/Admin'));
const User = lazy(() => import('./user/User'));

const App = () => {
  return (
    <Router>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/*" element={<Admin />} />
          <Route path="/user/*" element={<User />} />
          {/* Other routes */}
        </Routes>
      </Suspense>
    </Router>
  );
};

export default App;
