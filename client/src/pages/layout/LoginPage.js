import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import styles from '../style/LoginPage.module.css';

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loggedIn, setLoggedIn] = useState(false);
  const navigate   = useNavigate();

  const handleLogin = async () => {
    // Simulate a simple login logic
    const response = await fetch('http://localhost:8000/base/user/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    const responseData = await response.json();

    if (response.ok) {
      setLoggedIn(true);
      alert('Login succeeded 🆗');
      if(responseData?.requires_pass_change) {
        navigate("/change-password");
      }
    } else {
      alert('Invalid username or password');
    }
  };

  const handleLogout = () => {
    setLoggedIn(false);
  };

  return (
    <div className={styles.body}>
      {loggedIn ? (
        <div className={styles.container}>
          <h2>Welcome, {username}!</h2>
          <button onClick={handleLogout}>Logout</button>
        </div>
      ) : (
        <div className={styles.container}>
          <h2>Welcome back, boss!</h2>
          <form className={styles.form}>
            <label>
              Username:
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className={styles.input}
              />
            </label>
            <br />
            <label>
              Password:
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className={styles.input}
              />
            </label>
            <br />
            <button type="button" onClick={handleLogin} className={styles.button}>
              Login
            </button>
            <br />
            <Link to="/reset-password" className={styles.link}>
              Forgot Password
            </Link>
            <Link to="/new-user" className={styles.link}>
              Sign up
            </Link>
          </form>
        </div>
      )}
    </div>
  );
};

export default LoginPage;
