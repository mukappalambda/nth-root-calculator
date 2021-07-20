def fourth_root(a: float):
    if a == 0:
        return 0

    if a < 0:
        raise ValueError("Only non-negative inputs are accepted.")

    x = a
    num_epochs = 100

    for _ in range(num_epochs):
        grad = 8 * x**3 * (x**4 - a)
        hess = 8 * (7 * x**6 - 3 * a * x**2)
        x = x - grad / hess
    
    return x

def main():
    result = []

    for x in range(50):
        result.append(fourth_root(x**4))
    
    print(result)

if __name__ == "__main__":
    main()

