const SIZE = 0.3 * window.innerWidth;

function setup() {
  let canvas = createCanvas(SIZE, SIZE);
  canvas.parent("canvas");
  textAlign(CENTER, CENTER);
  fill(0);
}

function draw() {
  background(255);

  let spiralSize = document.getElementById("spiralSize").value;
  let centralNumber = document.getElementById("centralNumber").value;

  if (spiralSize % 2 == 1 && centralNumber > 0) {
    let wholeNumbers = document.getElementById("wholeNumbers").checked;
    let squareSize = SIZE / spiralSize;
    let x = spiralSize / 2;
    let y = spiralSize / 2;

    for (let n = centralNumber; n < spiralSize ** 2 + centralNumber; n++) {
      if (isPrime(n)) {
        if (wholeNumbers) {
          textSize(squareSize / 2);
          text(n, x * squareSize, y * squareSize);
        } else {
          strokeWeight(squareSize / 2);
          point(x * squareSize, y * squareSize);
        }
      }

      let move = floor((sqrt(4 * (n - centralNumber) + 1) + 3) % 4 + 1); // for more information see https://oeis.org/A063826
      if (move == 1) {
        x++; // move to the right
      } else if (move == 2) {
        y--; // move up
      } else if (move == 3) {
        x--; // move to the left
      } else {
        y++; // move down
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
