import { useState } from "react";
import "../index.css";

export default function HookMegaSena() {
  const [drawnNumber, setDrawnNumber] = useState('');
  const [drawnNumbers, setDrawnNumbers] = useState([]);

  const drawNumber = () => {
    let drawn = Math.floor(Math.random() * 60) + 1;
    while (drawnNumbers.includes(drawn)) {
      drawn = Math.floor(Math.random() * 60) + 1;
    }

    setDrawnNumber(drawn);
    setDrawnNumbers(prevState => [...prevState, drawn]);

    if (drawnNumbers.length >= 6) {
        alert('Já temos 6 números sorteados!');
        return;
      }
  };

  return (
    <div className="megasena-container">
      <img src="https://pbs.twimg.com/profile_images/52033036/av_400x400.png" alt="Logo da Megasena" className="megasena-icon" />
      <h2 className="megasena-title">Sorteador da Mega em React!</h2>
      <p className="megasena-numbers">Último número sorteado: {drawnNumber}</p>
      <p className="megasena-numbers">Sorteados: {drawnNumbers.join(' - ')}</p>
      <button onClick={drawNumber} className="megasena-button">Sortear Números</button>
    </div>
  );
}
