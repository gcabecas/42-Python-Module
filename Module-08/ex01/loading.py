import importlib


def get_version(mod):
    try:
        return mod.__version__
    except Exception:
        return "unknown"


def try_import(name):
    try:
        return importlib.import_module(name)
    except Exception:
        return None


def main():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    pandas_mod = try_import("pandas")
    if pandas_mod is None:
        print("[MISSING] pandas - Data manipulation missing")
    else:
        print(
            f"[OK] pandas ({
                get_version(pandas_mod)}) - Data manipulation ready")

    requests_mod = try_import("requests")
    if requests_mod is None:
        print("[MISSING] requests - Network access missing")
    else:
        print(
            f"[OK] requests ({
                get_version(requests_mod)}) - Network access ready")

    matplotlib_mod = try_import("matplotlib")
    if matplotlib_mod is None:
        print("[MISSING] matplotlib - Visualization missing")
    else:
        print(
            f"[OK] matplotlib ({
                get_version(matplotlib_mod)}) - Visualization ready")

    numpy_mod = try_import("numpy")

    if pandas_mod is None or requests_mod is None or matplotlib_mod \
            is None or numpy_mod is None:
        print("\nDependency Error!")
        print("You need to install missing packages"
              " before entering the Matrix.")
        print("With pip:")
        print("  pip install -r requirements.txt")
        print("With Poetry:")
        print("  poetry install")
        return

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    data = np.random.randn(1000)
    df = pd.DataFrame({"signal": data})

    plt.figure()
    plt.plot(df["signal"])
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
