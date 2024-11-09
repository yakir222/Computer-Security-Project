import React, { useState } from 'react';
import styles from '../style/NewCustomerPage.module.css';

const NewCustomerForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    id: '',
    address: '',
    animal: '',
    feet_size: '',
  });

  const [createdCustomerName, setCreatedCustomerName] = useState('');

  // Function to handle input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Function to handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Check if all fields are filled
    for (const key in formData) {
      if (formData[key] === '') {
        alert('Please fill in all fields');
        return;
      }
    }

    // Send REST request to the backend
    try {
      formData.id = parseInt(formData.id)
      formData.feet_size = parseInt(formData.feet_size)
      const response = await fetch('http://localhost:8000/base/customer/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        alert('Customer added successfully 👨‍🦳');
        const responseData = await response.json()
        setCreatedCustomerName(responseData?.name)
        setFormData({
          name: '',
          id: '',
          address: '',
          animal: '',
          feet_size: '',
        });
      } else {
        alert('Error adding customer!');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className={styles.body}>
      <br/>
      <br/>
      <br/>
      <br/>
      <h2>Add New Customer</h2>
      <form onSubmit={handleSubmit} className={styles.form}>
        <div className={styles.container}>
          <label>Name:</label>
          <input
            className={styles.input}
            type="text"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            // pattern="[A-Za-z]+"
            required
          />
        </div>
        <div className={styles.container}>
          <label>ID:</label>
          <input
            className={styles.input}
            type="text"
            name="id"
            value={formData.id}
            onChange={handleInputChange}
            pattern="[0-9]{9}"
            required
          />
        </div>
        <div className={styles.container}>
          <label>Address:</label>
          <input
            className={styles.input}
            type="text"
            name="address"
            value={formData.address}
            onChange={handleInputChange}
            pattern="[A-Za-z0-9 ]+"
            required
          />
        </div>
        <div className={styles.container}>
          <label>Favorite Animal:</label>
          <select
            name="animal"
            value={formData.animal}
            onChange={handleInputChange}
            required
          >
            <option value="">Select an animal</option>
            <option value="Dog">Dog</option>
            <option value="Cat">Cat</option>
            <option value="Fish">Fish</option>
            <option value="Lion">Lion</option>
            <option value="Bear">Bear</option>
            <option value="Lizard">Lizard</option>
            <option value="Snake">Snake</option>
            <option value="Horse">Horse</option>
            <option value="Monkey">Monkey</option>
          </select>
        </div>
        <div className={styles.container}>
          <label>Feet Size:</label>
          <input
            className={styles.input}
            type="text"
            name="feet_size"
            value={formData.feet_size}
            onChange={handleInputChange}
            pattern="[0-9]{1,2}"
            required
          />
        </div>
        <button type="submit" className={styles.button}>Submit</button>
        <br/>
        <br/>
        <br/>
        <label>{createdCustomerName}</label>
      </form>
    </div>
  );
};

export default NewCustomerForm;
