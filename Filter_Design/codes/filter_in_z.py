import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 2.48e-4 * s**4 / (s**8 + 0.189*s**7 + 4.598*s**6 + 0.627*s**5 + 7.581*s**4 + 0.687*s**3 + 5.521*s**2 + 0.249*s + 1.498)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


