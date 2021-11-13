#!/usr/bin/env python
# coding: utf-8
# %% [markdown]
# # comments from GSI:
#
# Q0: -1 equation not in Latex
#
# Q2:  -2 missing two staggered rows
#
# Q3: -10 missing part c
#
# Overall: -8 for no docstring
#
# -2 for all imports aren't collected together near the start

# %% [markdown]
# # Correction that I will make:
#
# I will make the correction about the comments of:
#
# Q2:  -2 missing two staggered rows
#
# Overall: -8 for no docstring
#
# -2 for all imports aren't collected together near the start
#
# ## Hi GSIs, for the comment of "Q3: -10 missing part c", I checked and found that I did have part c, but just forgot to label it, in this case, I add the label and didn't change the content and code of this part (Question 3c), could I get it regraded? Thank you !
#

# %%
import math
import numpy as np
import scipy.stats as st
import numpy as np

# %%

# # Problem 0

# This is *question 0* for [problem set 1](https://jbhender.github.io/Stats507/F21/ps1.html) of [Stats 507](https://jbhender.github.io/Stats507/F21/).
# > Question 0 is about Markdown.
# 
# The next question is about the **Fibonacci sequence**, Fn=Fn−2+Fn−1. In part **a** we will define a Python function `fib_rec()`.
# 
# Below is a …
# 
# ## Level 3 Header
# Next, we can make a bulleted list:
# 
#  - Item 1
#       - detail 1
#       - detail 2
#  - Item 2
# 
# Finally, we can make an enumerated list:
# 
#     a.Item 1
#     b.Item 2
#     c.Item 3

# ```
# This is *question 0* for [problem set 1](https://jbhender.github.io/Stats507/F21/ps1.html) of [Stats 507](https://jbhender.github.io/Stats507/F21/).
# > Question 0 is about Markdown.
# 
# The next question is about the **Fibonacci sequence**, Fn=Fn−2+Fn−1. In part **a** we will define a Python function `fib_rec()`.
# 
# Below is a …
# 
# ## Level 3 Header
# Next, we can make a bulleted list:
# 
#  - Item 1
#       - detail 1
#       - detail 2
#  - Item 2
# 
# Finally, we can make an enumerated list:
# 
#     a.Item 1
#     b.Item 2
#     c.Item 3
# ```

# # Problem 1

# ### (a)

# %%

"""
    The function using the recursive way to calculate Fn. 

    Parameters
    ----------
    n : total number of the Fibonacci sequence.
    a : the first number in the sequence .
    b : the second number of the sequence.

     Returns
     -------
     The value of Fn.

    """
def fib_rec(n, a = 0, b = 1):
    if (n == 0):
        return a
    if (n == 1):
        return b
    else:
        return fib_rec(n - 1, a, b) + fib_rec(n - 2, a, b)


# ### (b)

# %%

"""
    The function using the for loop to calculate Fn. 

    Parameters
    ----------
    n : total number of the Fibonacci sequence.
    a : the first number in the sequence .
    b : the second number of the sequence.

     Returns
     -------
     The value of Fn.

    """
def fib_for(n, a = 0, b = 1):
    x = a
    y = b
    for i in range(1, n):
        (x, y) = (y, x+y)
    return y


# ### (c)

# %%
"""
    The function using the while loop to calculate Fn. 

    Parameters
    ----------
    n : total number of the Fibonacci sequence.
    a : the first number in the sequence .
    b : the second number of the sequence.

     Returns
     -------
     The value of Fn.

    """

def fib_whl(n, a = 0, b = 1):
    x = a
    y = b
    while (i < n):
        (x, y) = (y, x+y)
        i+=1
    return y


# ### (d)

# %%


"""
    The function using the rounding method to calculate Fn. 

    Parameters
    ----------
    n : total number of the Fibonacci sequence.
    a : the first number in the sequence .
    b : the second number of the sequence.

     Returns
     -------
     The value of Fn.

    """
def fib_rnd(n):
    phi = (1+math.sqrt(5))/2
    return round(pow(phi,n)/(math.sqrt(5)))


# ### (e)

# %%

"""
    The function using the truncation method to calculate Fn. 

    Parameters
    ----------
    n : total number of the Fibonacci sequence.
    a : the first number in the sequence .
    b : the second number of the sequence.

     Returns
     -------
     The value of Fn.

    """

def fib_flr(n):
    phi = (1+math.sqrt(5))/2
    return math.floor(pow(phi,n)/(math.sqrt(5))+1/2)


# ### (f)

# %% [markdown]
# ## All the functions are from above, so no new docstring are needed 

# %%


from time import time
def fib_rec(n, a = 0, b = 1):
    if (n == 0):
        return a
    if (n == 1):
        return b
    else:
        return fib_rec(n - 1, a, b) + fib_rec(n - 2, a, b)

def fib_for(n, a = 0, b = 1):
    x = a
    y = b
    for i in range(1, n):
        (x, y) = (y, x+y)
    return y

def fib_whl(n, a = 0, b = 1):
    x = a
    y = b
    i = 0
    while (i != n):
        (x, y) = (y, x+y)
        i+=1
    return y

def fib_rnd(n):
    phi = (1+math.sqrt(5))/2
    return round(pow(phi,n)/(math.sqrt(5)))

def fib_flr(n):
    phi = (1+math.sqrt(5))/2
    return math.floor(pow(phi,n)/(math.sqrt(5))+1/2)


t0 = time()
fib_rec(40)
t1 = time()
fib_for(40)
t2 = time()
fib_whl(40)
t3 = time()
fib_rnd(40)
t4 = time()
fib_flr(40)
t5 = time()

print (t1-t0)
print (t2-t1)
print (t3-t2)
print (t4-t3)
print (t5-t4)


# n|fib_rec|fib_for|fib_whl|fib_rnd|fib_flr
# --|:--:|--:|-:|-:|-:
# 30|0.35|6.01e-05|4.10e-05|4.10e-05|3.60e-05
# 40|41.7|5.8e-05|4.2e-05|4.1e-05|3.5e-05

# # Problem 2

# ### (a)

# %%

"""
    The function computes the secified row of Pascal's triangle. 

    Parameters
    ----------
    n : specific row.
    k: number of success from binomial coef.
     Returns
     -------
     The row.

    """

def pascal_row(n,k):
    if (k == 0):
        return 1
    else:
        return pascal_row(n,k-1)*((n+1-k)/k)


# ### (b)

# %%
"""
    The function prints the first n rows of Pascal's triangle. 

    Parameters
    ----------
    n : specific row.
    k: number of success from binomial coef.
     Returns
     -------
     The first n rows.

    """

def pascal_row(n,k):
    if (k == 0):
        return 1
    else:
        return pascal_row(n,k-1)*((n+1-k)/k)

def print_pascal(n):
    for i in range(0, n):
        for k in range(0, n-i):
            print(" ", end = " ")
        for j in range(0, i+1):
            print(int(pascal_row(i, j)), end = " ")
            print(" ", end = " ")
        print()
            
print_pascal(10)


# # Problem 3

# %%

"""
    The function gives the point and confidence interval estimation of the population mean. 

    Parameters
    ----------
    arr : array.
    cl: confidence level.
    se: standard error

     Returns
     -------
     The string form of the point and confidence interval estimations.

    """
def func_a(arr, Cl, ci_format=None):
    x_bar = np.mean(arr)
    se = st.sem(arr)
    z = st.norm.ppf((1+Cl/100)/2)
    theta_L = x_bar-z*se
    theta_H = x_bar+z*se
    if ci_format == None:
        return {"est": x_bar, "lwr": theta_L, "upr": theta_H, "level": Cl}
    return str(x_bar)+"["+str(Cl)+"%Cl:("+str()+","+str(theta_H)+")"+"]"
    


# %%




"""
    The function gives the point and confidence interval estimation of the population mean. 

    Parameters
    ----------
    x_bar : sample mean.
    se : standard error .

     Returns
     -------
     The string form of the point and confidence interval estimations.

    """
def func_a(arr, Cl, ci_format = None):
    x_bar = np.mean(arr)
    se = st.sem(arr)
    z = st.norm.ppf((1+Cl/100)/2)
    theta_L = x_bar-z*se
    theta_H = x_bar+z*se
    if ci_format == None:
        return {"est": x_bar, "lwr": theta_L, "upr": theta_H, "level": Cl}
    return str(x_bar)+"["+str(Cl)+"%Cl:("+str(theta_L)+","+str(theta_H)+")"+"]"

"""
    The function gives different ways of the point and confidence interval estimation for parameters. 

    Parameters
    ----------
    p_hat : the estimation of probibility.
    z: z score.
    alpha: confidence level.

     Returns
     -------
     The string form of the point and confidence interval estimations.

    """
def func_b(arr,Cl, method,ci_format = None):
    x = 42#arr.bincount(1)
    n = arr.size
    
    if (method == "i"):
        p_hat = x/n
        z = st.norm.ppf((1+Cl/100)/2)
        theta_L = math.pow(p_hat,2)-z*math.sqrt(p_hat*(1-p_hat)/n)
        theta_H = math.pow(p_hat,2)+z*math.sqrt(p_hat*(1-p_hat)/n)
        if ci_format == None:
            return {"est": p_hat, "lwr": theta_L, "upr": theta_H, "level": Cl}
        return str(p_hat)+"["+str(Cl)+"%Cl:("+str(theta_L)+","+str(theta_H)+")"+"]"
    elif (method == "ii"):
        p_hat = x/n
        alpha = 1-Cl/100;
        theta_L = st.beta.ppf(alpha/2, x, n-x+1)
        theta_H = st.beta.ppf(1-alpha/2, x+1, n-x)
        if ci_format == None:
            return {"est": p_hat, "lwr": theta_L, "upr": theta_H, "level": Cl}
        else:
            return str((theta_L+theta_H)/2)+"["+str(Cl)+"%Cl:("+str(theta_L)+","+str(theta_H)+")"+"]"
    elif (method == "iii"):
        p_hat = x/n
        alpha = 1-Cl/100;
        theta_L = max(0, st.beta.ppf(alpha/2, x+0.5, n-x+0.5))
        theta_H = min(1, st.beta.ppf(1-alpha/2, x+0.5, n-x+0.5))
        if ci_format == None:
            return {"est": p_hat, "lwr": theta_L, "upr": theta_H, "level": Cl}
        return str((theta_L+theta_H)/2)+"["+str(Cl)+"%Cl:("+str(theta_L)+","+str(theta_H)+")"+"]"
    elif (method == "iv"):
        p_hat = x/n
        z = st.norm.ppf((1+Cl/100)/2)
        n_tilda = n + math.pow(z, 2)
        p_tilda = (x+math.pow(z, 2)/2)/n_tilda
        theta_L = math.pow(p_tilda,2)-z*math.sqrt(p_tilda*(1-p_tilda)/n)
        theta_H = math.pow(p_tilda,2)+z*math.sqrt(p_tilda*(1-p_tilda)/n)
        if ci_format == None:
            return {"est": p_tilda, "lwr": theta_L, "upr": theta_H, "level": Cl}
        return str(p_tilda)+"["+str(Cl)+"%Cl:("+str(theta_L)+","+str(theta_H)+")"+"]"




# %% [markdown]
# ## 3C.

# %%

#arr = np.array([1,2,3,4,5])
#print(func_a(arr, 3, 5, 95))
zeros = np.zeros(48)
ones = np.ones(42)
arr = np.concatenate((zeros, ones), axis=None)
print(func_b(arr, 99, "iv"))
print(func_a(arr, 99))
    
method|90|95|99
:-:|:-:|:-:|:-:
a|(0.3797,0.55365)|(0.3630,0.5703)|(0.3305,0.6029)
bi|(0.1313,0.3043)|(0.1147,0.3208)|(0.0823,0.3532)
bii|(0.3765,0.5586)|(0.3607,0.5749)|(0.3306,0.6064)
biii|(0.3818,0.5531)|(0.3660,0.5694)|(0.3357,0.6010)
biv|(0.1322,0.3052)|(0.1160,0.3221)|(0.0844,0.3554)


# %%




