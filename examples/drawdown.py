"""Fit pressure vs log10(hours) on a user-selected radial-flow interval."""
import math
from statistics import mean


def fit(points):
    if len(points) < 2 or any(t <= 0 for t, _ in points):
        raise ValueError("Provide at least two positive elapsed times")
    x = [math.log10(t) for t, _ in points]
    y = [p for _, p in points]
    x_bar, y_bar = mean(x), mean(y)
    variance = sum((v - x_bar) ** 2 for v in x)
    if not variance:
        raise ValueError("Elapsed times must vary")
    slope = sum((v - x_bar) * (p - y_bar) for v, p in zip(x, y)) / variance
    return slope, y_bar - slope * x_bar


if __name__ == "__main__":
    synthetic = [(1, 3000), (2, 2988), (5, 2972), (10, 2960)]
    slope, intercept = fit(synthetic)
    print(f"Slope {slope:.2f} psi/cycle | Fitted pressure at 1 h {intercept:.1f} psi")
