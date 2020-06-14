let dimension = document.getElementById("dimension");
let nbrCtr = document.getElementById("nbrCtr");
let valEnt = document.getElementById("valEnt");
let pts = document.getElementById("points");

let largeurTotale = 0.3 * window.innerWidth;
let division = dimension.value;
let largeurCase = largeurTotale / division;
let weightPoint = largeurCase / 2;

//Coordonnées point de départ
let startPoint = largeurTotale / 2;

let xVerteur = 0;
let yVerteur = 0;

let squareLength = 0;
let nombre = nbrCtr.value;
let couleur = 0;

let compteur = 0;

function setup() {
  var canvas = createCanvas(largeurTotale, largeurTotale);
  canvas.parent("app");
}

function draw() {
  // Modification du monbre maximal de colonnes en fonction du type d'affichage des nombres
  if(valEnt.checked) {
    dimension.max = "31";
    if(dimension.value > 31) {
      dimension.value = "31";
    }
  } else {
    dimension.max = "500";
  }

  if(nbrCtr.value >= 1 && nbrCtr.value <= 600 && dimension.value % 2 == 1) {
    affichageSpirale(dimension.value, nbrCtr.value, valEnt.checked);
  } else {
    background(255); // Ne plus afficher le spirale
  }
}

function affichageSpirale(col, ctr, ent) { // Nombre de colonnes, Nombre central, Valeurs entières ?, Afficher les nombres premiers ?
  //Initialisation des variables
  division = col;
  largeurCase = largeurTotale / division;
  weightPoint = largeurCase / 2;
  startPoint = largeurTotale / 2;
  xVerteur = 0;
  yVerteur = 0;
  squareLength = 0;
  nombre = ctr;
  couleur = 0;
  compteur = 0;

  background(255);

  while(squareLength < col) {
    textSize(weightPoint);
    textAlign(CENTER, CENTER);
    fill(couleur, 0, 0);

    for (let i = 0; i < squareLength; i++) {
      checkPrime(nombre);
      if(ent) {
        noStroke();
        fill(couleur);
        text(nombre, startPoint + xVerteur * largeurCase, startPoint + yVerteur * largeurCase);
      } else {
        strokeWeight(weightPoint);
        checkPrime(nombre);
        stroke(couleur);
        point(startPoint + xVerteur * largeurCase, startPoint + yVerteur * largeurCase);
      }
      yVerteur = yVerteur + ((-1) ** squareLength);
      nombre++;
      couleur = 0;
    }

    for (let i = 0; i <= squareLength; i++) {
      checkPrime(nombre);
      if(ent) {
        noStroke();
        fill(couleur);
        text(nombre, startPoint + xVerteur * largeurCase, startPoint + yVerteur * largeurCase);
      } else {
        strokeWeight(weightPoint);
        checkPrime(nombre);
        stroke(couleur);
        point(startPoint + xVerteur * largeurCase, startPoint + yVerteur * largeurCase);
      }
      xVerteur = xVerteur + ((-1) ** squareLength);
      nombre++;
      couleur = 0;
    }

    squareLength++;
  }
}

function checkPrime(n) {
  if (n == 1) {
    couleur = 255;
  } else {
    for (let i = 0; i ** 2 <= n; i++) {
      if (n % i == 0) {
        compteur++;
      }
    }
    if (compteur <= 1) {
      couleur = 0;
    } else {
      couleur = 255;
    }
    compteur = 0;
  }
}
