import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginPage from './pages/layout/LoginPage';
import ResetPasswordPage from './pages/layout/ResetPasswordPage';
import NewCustomerForm from './pages/layout/NewCustomerPage';
import CustomerDetails from './pages/layout/GetCustomer';
import ChangePasswordPage from './pages/layout/ChangePasswordPage';
import NewUserPage from './pages/layout/NewUserPage';

const AppRoutes = () => {
  return (
    <Router>
        <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/reset-password" element={<ResetPasswordPage />} />
        <Route path="/new-customer" element={<NewCustomerForm />} />
        <Route path="/get-customer" element={<CustomerDetails />} />
        <Route path="/change-password" element={<ChangePasswordPage />} />
        <Route path="/new-user" element={<NewUserPage />} />
        </Routes>
    </Router>
  );
};

export default AppRoutes;
