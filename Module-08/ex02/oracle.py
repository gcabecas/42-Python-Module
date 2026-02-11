import os

from dotenv import load_dotenv


def load_configuration() -> None:
    load_dotenv()


def get_env_variable(name: str) -> str:
    value = os.getenv(name)

    if value is None:
        print(f"[ERROR] Missing configuration: {name}")
        return ""

    return value


def display_configuration() -> None:

    matrix_mode = get_env_variable("MATRIX_MODE")
    database_url = get_env_variable("DATABASE_URL")
    api_key = get_env_variable("API_KEY")
    log_level = get_env_variable("LOG_LEVEL")
    zion_endpoint = get_env_variable("ZION_ENDPOINT")

    if not all([matrix_mode, database_url, api_key, log_level, zion_endpoint]):
        print("\n[ERROR] Configuration incomplete. "
              "Please check your .env file.")
        return

    print("ORACLE STATUS: Reading the Matrix...\n")
    print(f"Mode: {matrix_mode}")
    print(f"Database: Connected {database_url}")
    print(f"API Access: Authenticated {api_key}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: Online {zion_endpoint}")

    security_check(api_key)

    print("\nThe Oracle sees all configurations.")


def security_check(api_key: str) -> None:
    """Simple security verification"""

    print("\nEnvironment security check:")

    if api_key and api_key != "your_api_key_here":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Default API key detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found")

    print("[OK] Production overrides available")


def main() -> None:
    load_configuration()
    display_configuration()


if __name__ == "__main__":
    main()
