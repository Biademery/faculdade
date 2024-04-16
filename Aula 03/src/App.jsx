import React from 'react'
import Aluno from './components/Aluno'


export default function App () {
  return (
    <>
      {
        [
         {name: "Bia", email: "bia@email.com", course: "Sistema para Internet", average: 10},
         {name: "André", email: "andre@email.com", course: "Ciências contábeis", average: 7},
         {name: "Janaina", email: "jana@email.com", course: "Psicologia", average:5}
        ].map((aluno) =>
          <Aluno nome={aluno.name} course={aluno.course} email={aluno.email} average={aluno.average}/>
        )
      }
    </>
  )
}

