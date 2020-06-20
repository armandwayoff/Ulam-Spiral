# Ulam Spiral

What's the [Ulam spiral](https://en.wikipedia.org/wiki/Ulam_spiral) ?

In this repository, I offer two versions of the Ulam spiral. 
The first is an interactive application written in JavaScript on which you can create your own Ulam spiral according to certain parameters.
The second is a version written in Python.

My codes are based on the [A063826 sequence](https://oeis.org/A063826). This sequence describes the movements in the Ulam Spiral.

## Table of Contents

* [Interactive Application](#interactive-application)
  * [Overview of the Application](#overview-of-the-application)
* [Python Version](#python-version)
  * [How to use this Code](#how-to-use-this-code)
  * [Output Example](#output-example)

##  Interactive Application

To program the interactive application, I use the [p5.js library](https://p5js.org/).

[Visit the Application](https://editor.p5js.org/armandwayoff/present/q7rzZCcgv)

### Overview of the Application

![overview-application](illustration_image/overview-application.png)

## Python Version

### How to use this Code

To run this code, you will need the [SymPy](https://www.sympy.org/en/index.html) library. I use the [sympy.isprime()](https://www.geeksforgeeks.org/python-sympy-isprime-method/) method to check the primality of numbers.  
You will find all the information necessary for its installation on the following page : <https://docs.sympy.org/latest/install.html>

### Output Example

Here is an example with a size ```15``` Ulam spiral starting at ```1```:

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
