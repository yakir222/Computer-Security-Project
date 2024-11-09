import React, { useState, useEffect } from 'react';
import styles from '../style/NewUserPage.module.css';

const NewUserPage = () => {
  const [userName, setUserName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [passwordPolicy, setPasswordPolicy] = useState({});
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  useEffect(() => {
    // Fetch password policy from the backend when the page loads
    fetchPasswordPolicy();
  }, []);

  const fetchPasswordPolicy = async () => {
    try {
      // Replace 'YOUR_BACKEND_API/password-policy' with your actual API endpoint
      const response = await fetch('YOUR_BACKEND_API/password-policy');
      const data = await response.json();
      setPasswordPolicy(data);
    } catch (error) {
      console.error('Error fetching password policy', error);
    }
  };

  const validatePassword = () => {
    // Implement your password validation logic based on the password policy
    // Compare the entered password with the rules in passwordPolicy
    return true;
    // if (/* your validation logic here */) {

    // } else {
    //   setError('Password does not meet the policy requirements.');
    //   return false;
    // }
  };

  const handleSubmit = async () => {
    // Validate password before making the API call
    if (!validatePassword()) {
      return;
    }

    try {
      // Replace 'YOUR_BACKEND_API/create-user' with your actual API endpoint
      const response = await fetch('http://localhost:8000/base/user', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username:userName, email, password }),
      });

      const responseData = await response.json();

      if (response.ok) {
        setSuccessMessage('User created successfully!');
        // Implement redirection logic or navigate to the login page
      } else {
        setError(responseData.message || 'Failed to create user.');
      }
    } catch (error) {
      console.error('Error creating user', error);
      setError('An unexpected error occurred.');
    }
  };

  return (
    <div className={styles.body}>
      <h1>Create New User</h1>
      <div className={styles.container}>
        <label>User Name:</label>
        <input className={styles.input} type="text" value={userName} onChange={(e) => setUserName(e.target.value)} />
      </div>
      <div className={styles.container}>
        <label>Email:</label>
        <input className={styles.input} type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
      </div>
      <div className={styles.container}>
        <label>Password:</label>
        <input className={styles.input} type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </div>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {successMessage && (
        <div className={styles.container}>
          <p>{successMessage}</p>
          {/* Implement a popup or modal for success message */}
        </div>
      )}
      <button onClick={handleSubmit} className={styles.button}>Submit</button>
    </div>
  );
};

export default NewUserPage;
