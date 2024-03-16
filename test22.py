from sympy import fourier_series, pi
from sympy.abc import x
from sympy.plotting import plot  # Vi plottar med sympy.
from ipywidgets import interact


def g(N):
    f = x**2  # Funktionen
    s = fourier_series(f, (x, -pi, pi))  # Beräkna fourier serien
    s1 = s.truncate(N)
    print(s1)
    
    plot(f,s1, (x,-4,4))  # Plottar både f och s1
   
    return N


interact(g, N=(1,8))