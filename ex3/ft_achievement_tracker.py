def players_info(name: str, player: set) -> None:
    print(f"Player {name} achievements: {player}")


def achievement_analytics(sets: set) -> None:
    print(f"All unique achievements: {sets}")
    print(f"Total unique achievements: {len(sets)}\n")


def comparing(alice: set, bob: set, charlie: set) -> None:
    print(f"Common to all players: {alice.intersection(bob, charlie)}")
    rare = (
        alice.difference(bob, charlie)
        .union(charlie.difference(alice, bob))
        .union(bob.difference(alice, charlie))
    )
    print(f"Rare achievements (1 player): {rare}\n")
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    players_info("alice", alice)
    players_info("bob", bob)
    players_info("charlie", charlie)

    print("\n=== Achievement Analytics ===")
    all_of_it = alice.union(bob, charlie)
    achievement_analytics(all_of_it)
    comparing(alice, bob, charlie)
