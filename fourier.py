from scipy.integrate import trapz
import numpy as np
import matplotlib.pyplot as plt
def an(f,n,x1):
    return (1/(np.pi))*trapz(f(x1)*np.cos(n*x1),x1)

def bn(f,n,x1):
    return (1/(np.pi))*trapz(f(x1)*np.sin(n*x1),x1)

def a0(f,x1):
    return (1/(2*np.pi))*trapz(f(x1),x1)
def f(x):
    return (x**3)/2 - 2*(x**2)
arr = np.linspace(0,2*np.pi,100)

def g(x,n):
    s = a0(f,np.linspace(0,2*np.pi,100))
    for N in range(1,n+1):
        s += an(f,N,arr)*np.cos(N*x) + bn(f,N,arr)*np.sin(N*x)
    return s
arr2 = np.linspace(1,5,100)
plt.plot(arr2,g(arr2,5))
plt.plot(arr2,g(arr2,10))
plt.plot(arr2,g(arr2,20))
plt.plot(arr2,g(arr2,50))
plt.plot(arr2,f(arr2))
plt.legend(["N=5","N=10","N=20","N=50","original"])
plt.show()
