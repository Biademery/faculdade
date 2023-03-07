const heigth = [];
const gender = [];

let womanCount = [];
let manCount = [];
let sum = 0;

for (let i = 0; i < 15; i++) {
  heigth.push(prompt('Informe sua altura: '));
  gender.push(prompt('Informe seu gênero: '));
}

for (let i = 0; i < gender.length; i++) {
  if (gender[i] === 'F') {
    ++womanCount;
  }

  if (gender[i] === 'M') {
    sum += parseFloat(heigth[i]);
    ++manCount;
  }
}

// Pergunta 1
console.log(Math.max(...heigth));
console.log(Math.min(...heigth));
// Pergunta 2
console.log(sum / manCount);
// Pergunta 3
console.log(womanCount);
