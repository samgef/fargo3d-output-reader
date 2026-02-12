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


def make_plots(data):
    orbit = data["orbit"].copy()
    big = data["bigplanet"].copy()

    # Sort by time and drop duplicate times (helps remove restart/time-jump artifacts)
    orbit = orbit.sort_values("time").drop_duplicates(subset="time")
    big = big.sort_values("time").drop_duplicates(subset="time")

    
    # --- Plot 1: change in semi-major axis (a - a0) ---
    plt.figure()
    plt.plot(orbit_plot["time"], orbit_plot["a"] - a0)
    plt.xlabel("time")
    plt.ylabel("a - a0")
    plt.title("Change in semi-major axis: a(t) - a0")
    plt.show()

 
def main():
    print("SCRIPT STARTED")
    data = load_fargo_data()
    print_quick_info(data)
    make_plots(data)
    input("DONE - press Enter to close...")


if __name__ == "__main__":
    main()
