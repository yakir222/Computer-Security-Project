import '../style/CustomerDetails.css';
import React, { useState } from 'react';
// import React, { useState } from 'react';

function CustomerDetails() {
  const [customerId, setCustomerId] = useState('');
  const [customerName, setCustomerName] = useState('');
  const [customerDetails, setCustomerDetails] = useState(null);

  const handleIDChange = (e) => {
    setCustomerId(e.target.value);
  };

  const handleNameChange = (e) => {
    setCustomerName(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const queryParams = new URLSearchParams();
      if (!!customerId) {
        queryParams.append('id', customerId);
      }
      if (!!customerName) {
        queryParams.append('name', customerName);
      }

      const response = await fetch(`http://localhost:8000/base/customer/?${queryParams}`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          }
        },
        // ?id=${customerId}
      );
      let cust = await response.json();
      if (!Array.isArray(cust)) {
        cust = [cust]
      }
      setCustomerDetails(cust);
    } catch (error) {
      console.error('Error fetching customer details:', error);
    }
  };

  return (
    <div>
      <h1>Customer Details</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Customer ID:
          <input type="text" value={customerId} onChange={handleIDChange} />
          Name:
          <input type="text" value={customerName} onChange={handleNameChange} />
        </label>
        <button type="submit">Search</button>
      </form>
      <br/>
      <br/>
      <br/>
      <br/>
      <br/>
      <br/>
      <br/>
      {customerDetails && (
        <table className="customer-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Address</th>
              <th>Animal</th>
              <th>Feet Size</th>
            </tr>
          </thead>
          <tbody>
            {customerDetails.map((customer, index) => (
              <tr key={index}>
                <td>{customer.id}</td>
                <td>{customer.name}</td>
                <td>{customer.address}</td>
                <td>{customer.animal}</td>
                <td>{customer.feet_size}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default CustomerDetails;
