let p = document.getElementsByClassName('2_polynome');
let coeff = [];

for (let i = 0; i <p.length; i++) 
{
	j = (p.length-1)-i;
	console.log(p[j].value);
	coeff.push(parseFloat(p[j].value));  // p[i].value est de type String
	// La fonction push renvoie la nouvelle taille du tableau
	// Donc à chaque iteration de la boucle tu affectes à coeff la valeur 2
}
console.log(coeff[0])
function factorisator(a, b, c) 
{
	let d = (b ** 2) - (4 * a * c);
	console.log("Le discriminant est égal à " + d);
	if (d > 0)
   {
		let x1 = (-b - Math.sqrt(d)) / (2 * a);
		let x2 = (-b + Math.sqrt(d)) / (2 * a);
		console.log("Le polynôme peut s'écrire sous forme factorisée : " + a + "(x-" + x1 + ")(x-" + x2 + ")");
	}

	else if(d == 0)
  {
		let x = -b / (2 * a);
		console.log("Le polynôme peut s'écrire sous forme factorisée :" + a + "(x-" + x + ")^2)");
	}

	else
	{
		console.log("P A N I K le discriminant est inférieur à 0!");
	}
}

let but = document.getElementById("button");
// but.addEventListener("click", factorisator(coeff[2], coeff[1], coeff[0]));
but.addEventListener("click", () => {
	console.log("On va factoriser")
	factorisator(coeff[2], coeff[1], coeff[0]);
});