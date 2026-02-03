def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    try:
        print("Initializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")

        print("Inscribing preservation data...")
        txt = ["[ENTRY 001] New quantum algorithm discovered\n",
               "[ENTRY 002] Efficiency increased by 347%\n",
               "[ENTRY 003] Archived by Data Archivist trainee\n"]
        for line in txt:
            file.write(line)
        file.close()
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except OSError as e:
        print(f"ERROR: {e}")
        return


if __name__ == "__main__":
    main()
