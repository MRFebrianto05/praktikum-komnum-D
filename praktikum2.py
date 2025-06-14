import numpy as np

def f(x):
    """Fungsi yang akan diintegrasikan."""
    return x**2

def trapezoidal_rule(func, a, b, n):
    """
    Mengimplementasikan metode Trapezoidal.
    func: fungsi yang akan diintegrasikan
    a: batas bawah integrasi
    b: batas atas integrasi
    n: jumlah sub-interval
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

def romberg_integration(func, a, b, max_level=5):
    """
    Mengimplementasikan metode Integrasi Romberg.
    func: fungsi yang akan diintegrasikan
    a: batas bawah integrasi
    b: batas atas integrasi
    max_level: level maksimum ekstrapolasi Romberg
    """
    R = np.zeros((max_level, max_level))

    for k in range(max_level):
        n = 2**k 
        R[k, 0] = trapezoidal_rule(func, a, b, n)
        print(f"Trapezoidal dengan n={n}: {R[k, 0]:.10f}")

    for j in range(1, max_level):
        for k in range(j, max_level):
            R[k, j] = (4**j * R[k, j-1] - R[k-1, j-1]) / (4**j - 1)
            print(f"  Romberg R({k}, {j}): {R[k, j]:.10f}")

    return R[max_level-1, max_level-1]

a = 0
b = 1
exact_integral = 1/3

print(f"Fungsi: f(x) = x^2")
print(f"Batas Integrasi: {a} sampai {b}")
print(f"Nilai Integral Eksak: {exact_integral:.10f}\n")

print("--- Demonstrasi Metode Trapezoidal ---")
for n_trap in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
    trap_result = trapezoidal_rule(f, a, b, n_trap)
    error_trap = abs(trap_result - exact_integral)
    print(f"Trapezoidal (n={n_trap}): {trap_result:.10f}, Error: {error_trap:.10f}")

print("\n--- Demonstrasi Metode Integrasi Romberg ---")
romberg_result = romberg_integration(f, a, b, max_level=5) 
error_romberg = abs(romberg_result - exact_integral)
print(f"\nHasil Akhir Integrasi Romberg: {romberg_result:.10f}")
print(f"Error Integrasi Romberg: {error_romberg:.10f}")
