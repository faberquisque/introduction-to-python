'''1. El submódulo **scipy.constants** tiene valores de constantes físicas de interés. 
Usando este módulo compute la constante de Stefan-Boltzmann $\sigma$ utilizando la relación:
$$\sigma = \frac{2 \pi^5 k_B^4}{15 h^3 c^2}$$
Confirme que el valor obtenido es correcto comparando con la constante para esta cantidad en ``scipy.constants``
'''
import scipy.constants as cts
import scipy
import numpy as np
import matplotlib.pyplot as plt

sigma = 2*cts.pi**5*cts.Boltzmann**4/15/cts.h**3/cts.speed_of_light**2
print(sigma, cts.Stefan_Boltzmann)
'''2. Usando **Scipy** y **Matplotlib** grafique las funciones de onda del oscilador 
armónico unidimensional para las cuatro energías más bajas ($n=1,2,3,4$), en el intervalo $[-5,5]$. 
Asegúrese de que están correctamente normalizados.

Las funciones están dadas por:

$$ \psi _{n}(x)={\frac {1}{\sqrt {2^{n}\,n!}}}\cdot 
\left({\frac {\omega }{\pi}}\right)^{1/4}\cdot
 e^{-{\frac {\omega x^{2}}{2 }}}\cdot
  H_{n}\left({\sqrt{\omega}}\, x\right),\qquad n=0,1,2,\ldots .$$

donde $H_{n}$ son los polinomios de Hermite, y usando $\omega = 2$.

Trate de obtener un gráfico similar al siguiente (tomado de 
[wikipedia](https://en.wikipedia.org/wiki/Quantum_harmonic_oscillator). 
Realizado por By AllenMcC. - File:HarmOsziFunktionen.jpg, 
[CC BY-SA 3.0](https://commons.wikimedia.org/w/index.php?curid=11623546))

![](figuras/HarmOsziFunktionen.png)
'''

n=(1,2,3,4)

def fun_onda_osc(x,n,omega):
  return 1/np.sqrt(2**n*np.math.factorial(n)) * (omega/cts.pi)**0.25 * np.exp(-omega*x**2/2) * scipy.special.eval_hermite(n,np.sqrt(omega)*x)

x=np.linspace(-5,5,50)
y=fun_onda_osc(x,n[0],2)
plt(x,y)