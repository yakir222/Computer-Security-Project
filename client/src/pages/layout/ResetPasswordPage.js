import React, { useState } from 'react';
import '../style/ResetPasswordPage.css';

const ResetPasswordPage = () => {
  const [email, setEmail] = useState('');
  const [isValidEmail, setIsValidEmail] = useState(false);

  const handleEmailChange = (e) => {
    const inputEmail = e.target.value;
    // Basic email validation
    const isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(inputEmail);
    setIsValidEmail(isValid);
    setEmail(inputEmail);
  };

  const handleResetClick = () => {
    if (isValidEmail) {
      // Send reset email to backend
      const requestBody = { email };
      fetch('http://localhost:8000/base/user/resetPassword', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
      })
        .then(response => response.json())
        .then(data => {
          alert("Sent password reset mail!")
          console.log(data);
        })
        .catch(error => {
          alert("error sending password reset mail")
          console.error('Error sending reset email:', error);
        });
    }
  };

  return (
    <div>
      <label>Email:</label>
      <input
        type="email"
        value={email}
        onChange={handleEmailChange}
        placeholder="Enter your email"
      />
      {/* {!isValidEmail && <p style={{ color: 'red' }}>Invalid email address</p>} */}
      <button onClick={handleResetClick} disabled={!isValidEmail}>
        Send reset email
      </button>
    </div>
  );
};

export default ResetPasswordPage;
