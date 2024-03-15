def semf(A, Z):
    # Fitting parameters (Lilley Fig 2.3)
    params = (15.56, 17.23, 0.7, 23.28)
    a_v, a_s, a_c, a_a = params
    
    # Paring term
    delta=0
    if A%2==0 and Z%2==0:
        delta = 12*A**(-1/2)
    elif A%2==0 and Z%2==1:
        delta = -1*12*A**(-1/2)
    
    binding_energy = a_v*A - a_s*A**(2/3) - a_c*Z**2*A**(-1/3) - a_a*((A - 2*Z)**2/A) + delta
    
    return binding_energy