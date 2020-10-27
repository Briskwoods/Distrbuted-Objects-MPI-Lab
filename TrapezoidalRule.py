def f(x):
    return x

# Function to find area
def area( x, y, n):
    # h = Δx
    h = (y - x) / n  
    s = 0.0
    # The sum at initial endpoint
    s += f(x)  
    for i in range(1, int(n)):
        # The sum at endpoints within range a-b
        s += 2 * f(x + i * h)  
    # The sum at final endpoint
    s += f(y)  
    return s * (h / 2.0)

# Compute the area under the curve
if __name__ == '__main__':
    print(area(0, 10, 5))
