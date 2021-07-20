def cube_root(a: float):
    if a == 0:
        return 0

    if a < 0:
        raise ValueError("Only non-negative inputs are accepted.")

    x = a
    num_epochs = 100

    for _ in range(num_epochs):
        grad = 6 * x**2 * (x**3 - a)
        hess = 6 * (5 * x**4 - 2 * a * x)
        x = x - grad / hess
    
    return x

def main():
    result = []

    for x in range(50):
        result.append(cube_root(x**3))
    
    print(result)

if __name__ == "__main__":
    main()

