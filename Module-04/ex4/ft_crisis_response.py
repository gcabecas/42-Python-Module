def crisisHandler(file: str) -> None:
    print(f"CRISIS ALERT: Attempting access to '{file}'...")
    try:
        with open(file, 'r') as f:
            for line in f:
                print(line, end='')
            print("SUCCESS: Archive recovered - "
                  "Knowledge preserved for humanity''")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except OSError as e:
        print(f"An unexpected error occurred: {e}\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    crisisHandler("lost_archive.txt")
    crisisHandler("classified_vault.txt")
    crisisHandler("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
