import React, { useState, useEffect } from 'react';

const SignupForm = () => {
  const [formData, setFormData] = useState({
    fullName: '',
    email: '',
    sex: 'male',
    phoneNumber: '',
    country: '',
    password: '',
    confirmPassword: '',
  });

  const [activeField, setActiveField] = useState(null);

  useEffect(() => {
    if (activeField) {
      listenToSpeech();
    }
  }, [activeField]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSpeakClick = (fieldName) => {
    setActiveField(fieldName);
  };

  const listenToSpeech = () => {
    const recognition = new window.webkitSpeechRecognition(); // For Safari compatibility
    recognition.continuous = true;
    recognition.lang = 'en-US';

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setFormData((prevData) => ({
        ...prevData,
        [activeField]: transcript,
      }));
    };

    recognition.onend = () => {
      setActiveField(null);
    };

    recognition.start();
  };

  const signup = () => {
    // signup logic 
    console.log('Form data:', formData);
  };

  return (
    <div>
      <h1>User Signup</h1>
      {Object.keys(formData).map((fieldName) => (
        <div key={fieldName}>
          <label htmlFor={fieldName}>{fieldName.replace(/([A-Z])/g, ' $1').trim() + ':'}</label>
          <input
            type="text"
            id={fieldName}
            name={fieldName}
            value={formData[fieldName]}
            onChange={handleInputChange}
            placeholder={`Enter ${fieldName}`}
            required
          />
          <button type="button" onClick={() => handleSpeakClick(fieldName)}>
            Speak
          </button>
        </div>
      ))}
      <button type="button" onClick={signup}>
        Sign Up
      </button>
    </div>
  );
};

export default SignupForm;
