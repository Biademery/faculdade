import React, { useState } from 'react';
import '../index.css';

export default function FormularioDeContato() {
  const [name, setName] = useState('');
  const [contact, setContact] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    const objetoLiteral = {
      name,
      contact,
      message,
    };

    const jsonToSend = JSON.stringify(objetoLiteral);

    console.log('O seguinte JSON será enviado via HTTP POST para o back-end:', jsonToSend);
  };

  return (
    <div>
      <form onSubmit={handleSubmit} className='form-contact'>
        <label>
          Nome:
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
        </label>
        <br />
        <label>
          Contato:
          <input type="text" value={contact} onChange={(e) => setContact(e.target.value)} />
        </label>
        <br />
        <label>
          Mensagem:
          <textarea value={message} onChange={(e) => setMessage(e.target.value)}></textarea>
        </label>
        <br />
        <button type="submit">Enviar</button>
      </form>
    </div>
  );
}
