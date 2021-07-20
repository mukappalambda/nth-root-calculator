def fifth_root(a: float):
    if a == 0:
        return 0

    if a < 0:
        raise ValueError("Only non-negative inputs are accepted.")

    x = a
    num_epochs = 200

    for _ in range(num_epochs):
        grad = 10 * x**4 * (x**5 - a)
        hess = 10 * (9 * x**8 - 4 * a * x**3)
        x = x - grad / hess
    
    return x

def main():
    result = []

    for x in range(50):
        result.append(fifth_root(x**5))
    
    print(result)

if __name__ == "__main__":
    main()

