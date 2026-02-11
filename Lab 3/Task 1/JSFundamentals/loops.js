let i = 3;

while (i) {
  alert( i-- );
}				//1



let i = 0;
while (++i < 5) alert( i ); //form 1 to 4

let i = 0;
while (i++ < 5) alert( i ); //from 1 to 5



for (let i = 0; i < 5; i++) alert( i ); //from 1 to 4

for (let i = 0; i < 5; ++i) alert( i ); //from 1 to 4




for (let i = 2; i <= 10; i++) {
  if (i % 2 == 0) {
    alert( i );
  }
}





let i = 0;
while (i < 3) {
  alert( `number ${i}!` );
  i++;
}



let num;

do {
  num = prompt("Enter a number greater than 100?", 0);
} while (num <= 100 && num);




let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) { // for each i...

  for (let j = 2; j < i; j++) { // look for a divisor..
    if (i % j == 0) continue nextPrime; // not a prime, go next i
  }

  alert( i ); // a prime
}
