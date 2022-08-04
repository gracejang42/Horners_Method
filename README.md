# Horners_Method
**Polynomial evaluation in python** 

Horner’s Method (or Horner’s scheme) is an algorithm for polynomial evaluation. 
After the introduction of computers, this algorithm became fundamental for computing efficiently with polynomials. 
It can also be referred to as a a method for approximating the roots of polynomials, described by Horner in 1819. 
It is a variant of the Newton-Raphson Method made more efficient for hand calculation by the application of Horner's rule. 
It was widely used until computers came into general use around 1970.

## Horner's Rule

$$a_0+a_1 x+a_2 x^{2}+a_3 x^{3}+...+a_n x^{n} = a_0+x\left(a_1+x\left(a_2+x\left(a_3+...+x\left(a_{n-1}+xa_n \right)...\right)\right)\right)$$

This allows the evaluation of a polynomial of degree n with only n multiplications and n additions. 
This is optimal, since there are polynomials of degree n that cannot be evaluated with fewer arithmetic operations. 
