import numpy as np
# Ratings of various products
product_ratings = np.array([4, 2, 5, 3, 7, 1])

# Use & instead of and, with parentheses around each comparison
print(product_ratings[(product_ratings >= 3) & (product_ratings != 5)])