[![made-with-p5js](https://img.shields.io/badge/Made_with-p5.js-ED1F5E.svg)](https://p5js.org)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[![readme_title](readme_title.png)](https://github.com/armandwayoff/Ulam-Spiral)

What's the [Ulam spiral](https://en.wikipedia.org/wiki/Ulam_spiral) ?

In this repository, I offer two versions of the Ulam spiral. 
The first is an interactive application written in JavaScript on which you can create your own Ulam spiral according to certain parameters.
The second is a version written in Python.

My codes are based on the [A063826 sequence](https://oeis.org/A063826):

let $n \in \mathbb{N}^\star$, we define the sequence $(a_n)$ as follows
$$a_n := \left \lfloor \sqrt{4n+1} \right \rfloor\ \mathrm{mod}[4].$$
For all $n \in \mathbb{N}^\star, a_n \in \\{ 1, 2, 3, 4 \\}$. 	Let $1, 2, 3, 4$ represent moves to the right, down, left and up; this sequence describes the movements in the clockwise square spiral.

## Table of Contents

* [Interactive Application](#interactive-application)
  * [Overview of the Application](#overview-of-the-application)
* [Python Version](#python-version)
  * [Output Example](#output-example)

##  Interactive Application

The interactive application is programmed with the [p5.js library](https://p5js.org/). This library is ideal because it has a full set of drawing functionality.

To use the library, simply add it to your ```HTML``` code:
```html
<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.10.2/p5.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.10.2/addons/p5.sound.min.js"></script>
  </head>
</html>
```

[Visit the Application](https://editor.p5js.org/armandwayoff/present/nq-eqxibK)

### Overview of the Application

![overview-application](illustration_image/overview-application.png)

## Python Version

### Output Example

Here is an output example with a size ```15``` Ulam spiral starting at ```1```:

```
197	   	   	  	193	  	191	   	  	   	  	   	   	   	   
   	   	   	  	   	  	   	139	  	137	  	   	   	   	   
199	   	101	  	   	  	97 	   	  	   	  	   	   	   	181
   	   	   	  	   	  	   	61 	  	59 	  	   	   	131	   
   	   	103	  	37 	  	   	   	  	   	31	   	89 	   	179
   	149	   	67	   	17	   	   	  	13 	  	   	   	   	   
   	   	   	  	   	  	5  	   	3 	   	29	   	   	   	   
   	151	   	  	   	19	   	   	2 	11 	  	53 	   	127	   
   	   	107	  	41 	  	7  	   	  	   	  	   	   	   	   
   	   	   	71	   	  	   	23 	  	   	  	   	   	   	   
   	   	109	  	43 	  	   	   	47	   	  	   	83 	   	173
   	   	   	73	   	  	   	   	  	79 	  	   	   	   	   
   	   	   	  	113	  	   	   	  	   	  	   	   	   	   
   	157	   	  	   	  	   	163	  	   	  	167	   	   	   
211	   	   	  	   	  	   	   	  	   	  	   	223	   	   
```
