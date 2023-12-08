import React, { useState } from 'react';
import Modal from 'react-bootstrap/Modal';
import './Form.css';

const Form = () => {

  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);

  const [formData, setFormData] = useState({
    island: '0',
    bill_length_mm: '',
    bill_depth_mm: '',
    flipper_length_mm: '',
    body_mass_g: '',
    sex: '1',
  });

  const [especie, setEspecie] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const mapEspecie = (val) => {
    return {
      '0': 'Adelie',
      '1': 'Chinstrap',
      '2': 'Gentoo'
    }[val] ?? null
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formDataObject = new FormData();
    for (const key in formData) {
      formDataObject.append(key, formData[key]);
    }

    try {
      const response = await fetch(
        new URL('pinguim', process.env.REACT_APP_BACKEND_URL).toString(), 
        {
          method: 'POST',
          body: formDataObject,
        }
      );

      if (response.ok) {
        const textResponse = await response.text();
        setEspecie(mapEspecie(textResponse));
        setShow(true);
      } else {
        console.error('Failed to submit form:', response.statusText);
      }
    } catch (error) {
      console.error('Error submitting form:', error.message);
    }
  };

  return (
    <div>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Aqui está a predição</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          De acordo com as características fornecidas, esse pinguim é da espécie: 
          <b> { especie } </b>
        </Modal.Body>
      </Modal>
      <h1>Pinguins de Palmer</h1>
      <img width="500" src='pinguins.png' />
      <p>Identifique a qual das espécies (Adelie, Gentoo ou Chinstrap) um pinguim pertence com base em alguns de seus atributos físicos.</p>
      <form onSubmit={handleSubmit}>
        <label>
          Island:
          <select name="island" value={formData.island} onChange={handleChange}>
            <option value="0">Dream</option>
            <option value="1">Biscoe</option>
            <option value="2">Torgersen</option>
          </select>
        </label>

        <label>
          Bill length (mm):
          <input
            type="number"
            name="bill_length_mm"
            value={formData.bill_length_mm}
            onChange={handleChange}
          />
        </label>

        <label>
          Bill depth (mm):
          <input
            type="number"
            name="bill_depth_mm"
            value={formData.bill_depth_mm}
            onChange={handleChange}
          />
        </label>

        <label>
          Flipper length (mm):
          <input
            type="number"
            name="flipper_length_mm"
            value={formData.flipper_length_mm}
            onChange={handleChange}
          />
        </label>

        <label>
          Body mass (g):
          <input
            type="number"
            name="body_mass_g"
            value={formData.body_mass_g}
            onChange={handleChange}
          />
        </label>

        <label>
          Sex:
          <select name="sex" value={formData.sex} onChange={handleChange}>
            <option value="0">Female</option>
            <option value="1">Male</option>
          </select>
        </label>

        <button type="submit">Enviar</button>
      </form>
    </div>
  );
};

export default Form;