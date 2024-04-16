import React from 'react';
import '../index.css'

export default function Sum (props){
  return (
    <div className="sum-container">
      <div className="result-text">
        A adição de {props.num1} e {props.num2} é: {props.num1 + props.num2}
        </div>
    </div>
  );
}

