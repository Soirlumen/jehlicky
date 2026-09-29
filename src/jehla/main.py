from simulace import simulace

if __name__ == "__main__":
    sim = simulace(delkax=10, delkay=10, pocet_linek=5, delka_jehly=1.0, pocet_jehel=5000000)
    sim.per_to_tam()
    print(f"Aproximace Pi: {sim.pi()}")