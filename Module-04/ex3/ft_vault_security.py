def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(file.read())
            print("\nSECURE PRESERVATION:")
        with open("security_protocol.txt", "w") as file:
            file.write("[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")
    except OSError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
