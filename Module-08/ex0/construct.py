import sys
import os
import site


def out_venv() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate    # On Windows\n")
    print("Then run this program again.")


def in_venv() -> None:
    env_path = sys.prefix
    env_name = os.path.basename(env_path.rstrip("/\\"))

    pkgs = site.getsitepackages()
    pkg_path = pkgs[0] if pkgs else "Unknown"

    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print("Package installation path:")
    print(pkg_path)


def main() -> None:
    if sys.prefix == sys.base_prefix:
        out_venv()
    else:
        in_venv()


if __name__ == "__main__":
    main()
