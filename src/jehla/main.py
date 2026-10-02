from simulace2 import simulace

if __name__ == "__main__":
    sim = simulace(delkax=10, mezilinkovy_prostor=2.0, pocet_linek=5, delka_jehly=1.0, pocet_jehel=5000000)
    sim.per_to_tam_bez_vizualizace()
    print(f"Aproximace Pi: {sim.pi()}")