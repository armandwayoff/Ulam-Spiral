let canvasSize = 0.3 * window.innerWidth;

function setup() {
  let canvas = createCanvas(canvasSize, canvasSize);
  canvas.parent("canvas");
  textAlign(CENTER, CENTER);
  fill(0);
}

function draw() {
  let spiralSize = document.getElementById("spiralSize").value;
  let centralNumber = document.getElementById("centralNumber").value;
  let wholeNumbers = document.getElementById("wholeNumbers").checked;
  if (spiralSize % 2 == 1 && centralNumber > 0) {
    let x = spiralSize / 2;
    let y = spiralSize / 2;
    let squareSize = canvasSize / spiralSize;
    background(255);
    strokeWeight(squareSize / 2);
    textSize(squareSize / 2);
    for (let n = centralNumber; n < spiralSize ** 2 + centralNumber; n++) {
      if (isPrime(n)) {
        if (wholeNumbers) {
          text(n, x * squareSize, y * squareSize);
        } else {
          point(x * squareSize, y * squareSize);

        }
      }
      let move = floor((sqrt(4 * (n - centralNumber) + 1) + 3) % 4 + 1);
      if (move == 1) {
        x++;
      } else if (move == 2) {
        y--;
      } else if (move == 3) {
        x--;
      } else {
        y++;
      }
    }
  }
}


function isPrime(n) {
  if (n == 1) {
    return false;
  } else {
    for (let i = 2; i ** 2 <= n; i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }
}
