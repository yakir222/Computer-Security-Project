import React, { useState, useEffect } from 'react';
import '../style/ChangePasswordPage.css';

const ChangePasswordPage = () => {
  const [username, setUsername] = useState('');
  const [old_password, setOldPassword] = useState('');
  const [new_password, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState(null);

  useEffect(() => {
    
  }, []);


  const handleChangePassword = async () => {
    try {

      // Send request to change password
      const response = await fetch('http://localhost:8000/base/user/updatePassword', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username,
          new_password,
          old_password
        }),
      });

      if (response.ok) {
        // Password changed successfully
        alert('Password changed successfully');
        // You may want to redirect the user to a success page or update UI accordingly
      } else {
        // Handle error response from the backend
        const errorResponse = await response.json();
        setError(errorResponse.message);
      }
    } catch (error) {
      console.error('Error changing password:', error);
      // Handle error as needed
    }
  };

  return (
    <div>
      <h2>Change Password</h2>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <div>
        <label>Username:</label>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <div>
        <label>Current Password:</label>
        <input
          type="password"
          value={old_password}
          onChange={(e) => setOldPassword(e.target.value)}
        />
      </div>
      <div>
        <label>New Password:</label>
        <input
          type="password"
          value={new_password}
          onChange={(e) => setNewPassword(e.target.value)}
        />
      </div>
      <div>
        <label>Confirm New Password:</label>
        <input
          type="password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />
      </div>
      <button onClick={handleChangePassword}>Submit</button>
    </div>
  );
};

export default ChangePasswordPage;
