def achivements() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = set(('first_kill', 'level_10', 'treasure_hunter', 'speed_demon'))
    bob = set(('first_kill', 'level_10', 'boss_slayer', 'collector'))
    charlie = set(('level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                   'perfectionist'))

    print(f"Player Alice achievements: {alice}")
    print(f"Player Bob achievements: {bob}")
    print(f"Player Charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===\n")

    print(f"Common to all players: {alice & bob & charlie}")
    print(f"Rare achievements (1 player): "
          {(alice - bob - charlie)
           - (bob - charlie - alice)
           - (charlie - alice - bob)}
          f"\n")

    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    achivements()
