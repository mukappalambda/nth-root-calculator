def square_root(a: float):
    if a == 0:
        return 0

    if a < 0:
        raise ValueError("Only non-negative inputs are accepted.")
        
    x = a
    num_epochs = 100

    for _ in range(num_epochs):
        grad = 4 * x * (x**2 - a)
        hess = 4 * (3 * x**2 - a)
        x = x - grad / hess
    
    return x

def main():
    result = []

    for x in range(50):
        result.append(square_root(x**2))
    
    print(result)

if __name__ == "__main__":
    main()

