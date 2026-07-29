"""Intentionally buggy harmonic-oscillator script for Week 2 debugging."""
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import special

hbar = 1.0
omega = 1.0


def energy_levels(n_max: int = 5):
    levels = []
    for n in range(n_max):
        e_n = hbar * omega * n  # BUG 1: missing zero-point term +0.5
        levels.append(e_n)
    return np.array(levels)


def psi_n(n: int, x: np.ndarray):
    # BUG 3: hallucinated SciPy API (should be special.hermite(n)(x))
    Hn = special.hermite_poly(n, x)
    # BUG 4: wrong normalization factor
    norm = 1.0 / np.sqrt(math.factorial(n))
    return norm * np.exp(-(x ** 2) / 2) * Hn


def main():
    x = np.linspace(-4, 4, 400)
    energies = energy_levels(5)
    print("Energy levels:", energies)

    psi = np.array([psi_n(n, x) for n in range(5)])
    psi = psi[1:5]  # BUG 2: off-by-one drops ground state

    plt.figure(figsize=(8, 5))
    for i, y in enumerate(psi):
        density = y  # BUG 5: should be np.abs(y)**2
        plt.plot(x, density, label=f"n={i}")

    plt.title("Quantum Harmonic Oscillator (buggy)")
    plt.xlabel("x")
    plt.ylabel("Probability density")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
