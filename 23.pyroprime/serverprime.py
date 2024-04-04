import Pyro4

@Pyro4.expose
class PrimeChecker:
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

def main():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()

    uri = daemon.register(PrimeChecker)
    ns.register("prime.checker", uri)

    print("Prime Checker Server is ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
