import Pyro4

def main():

    prime_checker = Pyro4.Proxy("PYRONAME:prime.checker")


    number = int(input("Enter a number: "))


    is_prime = prime_checker.is_prime(number)


    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()
