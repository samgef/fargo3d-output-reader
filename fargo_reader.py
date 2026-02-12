import pandas as pd
import matplotlib.pyplot as plt


def load_fargo_data():
    # orbit0.dat has 10 columns
    orbit_cols = [
        "time", "ecc", "a", "M", "f",
        "arg_peri", "frame_angle", "inc", "Omega", "varpi"
    ]

    # bigplanet0.dat and planet0.dat have 10 columns
    planet_cols = [
        "output_number", "x", "y", "z",
        "vx", "vy", "vz",
        "mass", "time", "frame_omega"
    ]

    orbit = pd.read_csv("orbit0.dat", sep=r"\s+", header=None, names=orbit_cols)

    return {"orbit": orbit}


def print_quick_info(data):
    print("Rows loaded:")
    print("  orbit0.dat    :", len(data["orbit"]))
    print("  bigplanet0.dat:", len(data["bigplanet"]))
    print("  planet0.dat   :", len(data["planet"]))
    print("\nFirst row of orbit data:")
    print(data["orbit"].iloc[0])

# def make_plots()

 
def main():
    print("SCRIPT STARTED")
    data = load_fargo_data()
    print_quick_info(data)
    input("DONE - press Enter to close...")


if __name__ == "__main__":
    main()
