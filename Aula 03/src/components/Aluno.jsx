import React from 'react'
import '../index.css'

export default function Aluno({name, email, course, average}) {
  return (
    <div className="aluno-container">
        <p>Nome: {name} </p>
        <p>Email: {email}</p>
        <p>Curso: {course}</p>
        <p>Status: {average >= 7 ? <span className="aprovado"><b>Aprovado</b></span> : <span className="reprovado"><b>Reprovado</b></span>}</p>
    </div>
  );
}