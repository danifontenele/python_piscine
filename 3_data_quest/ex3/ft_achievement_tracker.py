def main() -> None:
    alice = ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon']
    bob = ['first_kill', 'level_10', 'boss_slayer', 'collector']
    charlie = ['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 
               'perfectionism']
    a = set(alice)
    b = set(bob)
    c = set(charlie)
    
    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {a}")
    print(f"Player bob achievements: {b}")
    print(f"Player charlie achievements: {c}")

    print("\n=== Achievement Analytics ===")
    
    achievements_set = a | b | c
    print(f"All unique achievements: {achievements_set}")
    print(f"Total unique achievements: {len(achievements_set)}")

    common_to_all = a & b & c
    print(f"\nCommon to all players: {common_to_all}")
    
    just_one_have = ((a - b - c) | (b - c - a) | (c - a - b))
    print(f"Rare achievements (1 player): {just_one_have}")

    print(f"\nAlice vs Bob common: {a & b}")
    print(f"Alice unique: {a - b}")
    print(f"Bob unique: {b - a}")

if __name__ == "__main__":
    main()