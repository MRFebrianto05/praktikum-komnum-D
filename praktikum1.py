import numpy as np
import matplotlib.pyplot as plt

def regula_falsi(func, a, b, tol=1e-6, max_iter=100):
    """
    Implementasi metode Regula Falsi.

    Args:
        func (function): Fungsi yang akan dicari akarnya, f(x).
        a (float): Tebakan awal batas bawah.
        b (float): Tebakan awal batas atas.
        tol (float): Toleransi error untuk kriteria penghentian.
        max_iter (int): Jumlah iterasi maksimum.

    Returns:
        float: Akar fungsi yang ditemukan.
        list: Daftar tuples (iter, a, b, c, f(a), f(b), f(c), error) untuk logging proses.
    """
    if func(a) * func(b) >= 0:
        print("Error: f(a) dan f(b) harus memiliki tanda yang berlawanan.")
        return None, []

    iter_data = []
    c_prev = None

    print(f"{'Iterasi':<8} {'a':<15} {'b':<15} {'c':<15} {'f(a)':<15} {'f(b)':<15} {'f(c)':<15} {'Error Absolut':<15}")
    print("-" * 115)

    for i in range(max_iter):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        f_a = func(a)
        f_b = func(b)
        f_c = func(c)

        error_abs = abs(f_c) 

        iter_data.append((i + 1, a, b, c, f_a, f_b, f_c, error_abs))
        print(f"{i + 1:<8} {a:<15.6f} {b:<15.6f} {c:<15.6f} {f_a:<15.6f} {f_b:<15.6f} {f_c:<15.6f} {error_abs:<15.6e}")

        if error_abs < tol:
            print(f"\nKonvergensi tercapai setelah {i + 1} iterasi. Akar ditemukan: {c:.6f}")
            break

        if f_a * f_c < 0:
            b = c
        else:
            a = c
        
        c_prev = c 

    else: 
        print(f"\nJumlah iterasi maksimum ({max_iter}) tercapai. Akar terakhir: {c:.6f}")

    return c, iter_data

def plot_function_and_root(func, root, a_initial, b_initial, iter_data=None):
    """
    Membuat plot fungsi dan akar yang ditemukan.
    """
    x = np.linspace(min(a_initial, root) - 1, max(b_initial, root) + 1, 400)
    y = func(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
    plt.axvline(0, color='black', linestyle='--', linewidth=0.7)

    if root is not None:
        plt.plot(root, func(root), 'ro', markersize=8, label=f'Akar (Regula Falsi): {root:.6f}')

    if iter_data:
        c_values = [data[3] for data in iter_data]
        f_c_values = [data[6] for data in iter_data]
        plt.plot(c_values, f_c_values, 'go--', markersize=5, alpha=0.6, label='Titik Iterasi c')


    plt.title('Metode Regula Falsi')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    def my_function(x):
        return x**3 - 2*x - 5

    a_initial = 2
    b_initial = 3 

    tolerance = 1e-6
    max_iterations = 100

    print(f"Mencari akar fungsi f(x) = x^3 - 2x - 5 menggunakan Regula Falsi:")
    print(f"Interval awal: [{a_initial}, {b_initial}]")
    print(f"Toleransi: {tolerance}")
    print(f"Iterasi Maksimum: {max_iterations}\n")

    root_found, process_log = regula_falsi(my_function, a_initial, b_initial, tolerance, max_iterations)

    if root_found is not None:
        print(f"\nRoot yang ditemukan: {root_found:.6f}")
        plot_function_and_root(my_function, root_found, a_initial, b_initial, process_log)
