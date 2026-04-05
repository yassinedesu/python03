players_data = [
    {
        "name": "alice", "score": 2300,
        "level": 15, "region": "north", "active": True
    },
    {
        "name": "bob", "score": 1800,
        "level": 8, "region": "east", "active": True
    },
    {
        "name": "charlie", "score": 2150,
        "level": 12, "region": "central", "active": True
    },
    {
        "name": "diana", "score": 2050,
        "level": 11, "region": "north", "active": False
    },
    {
        "name": "eve", "score": 950,
        "level": 4, "region": "east", "active": False
    },
]

achievements_data = [
    {"player": "alice", "achievement": "first_kill"},
    {"player": "alice", "achievement": "level_10"},
    {"player": "alice", "achievement": "boss_slayer"},
    {"player": "bob", "achievement": "first_kill"},
    {"player": "bob", "achievement": "level_10"},
    {"player": "charlie", "achievement": "level_10"},
    {"player": "charlie", "achievement": "boss_slayer"},
    {"player": "charlie", "achievement": "speed_demon"},
    {"player": "diana", "achievement": "first_kill"},
    {"player": "diana", "achievement": "treasure_hunter"},
]


def list_comprehension_examples() -> None:
    print("=== List Comprehension Examples ===")
    high_scorers = [p["name"] for p in players_data if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    scores_doubled = [
        p["score"] * 2 for p in players_data if p["score"] > 2000
    ]
    print(f"Scores doubled: {scores_doubled}")
    active_players = [p["name"] for p in players_data if p["active"]]
    print(f"Active players: {active_players}")


def dict_comprehension_examples() -> None:
    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in players_data}
    print(f"Player scores: {player_scores}")

    def score_category(score: int) -> str:
        if score >= 2000:
            return "high"
        elif score >= 1500:
            return "medium"
        return "low"

    score_categories = {
        p["name"]: score_category(p["score"]) for p in players_data
    }
    print(f"Score categories: {score_categories}")
    achievement_counts = {
        p["name"]: sum(
            1 for a in achievements_data if a["player"] == p["name"]
        )
        for p in players_data
    }
    print(f"Achievement counts: {achievement_counts}")


def set_comprehension_examples() -> None:
    print("\n=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in players_data}
    print(f"Unique players: {unique_players}")
    unique_achievements = {a["achievement"] for a in achievements_data}
    print(f"Unique achievements: {unique_achievements}")
    active_regions = {p["region"] for p in players_data if p["active"]}
    print(f"Active regions: {active_regions}")


def combined_analysis() -> None:
    print("\n=== Combined Analysis ===")
    total_players = len({p["name"] for p in players_data})
    unique_achievements = {a["achievement"] for a in achievements_data}
    total_achievements = len(unique_achievements)
    scores = [p["score"] for p in players_data]
    average_score = sum(scores) / len(scores)
    achievement_counts = {
        p["name"]: sum(
            1 for a in achievements_data if a["player"] == p["name"]
        )
        for p in players_data
    }
    top = max(players_data, key=lambda p: p["score"])
    top_achievements = achievement_counts.get(top["name"], 0)
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_achievements}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {top['name']} ({top['score']} points,"
        f" {top_achievements} achievements)"
    )


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")
    list_comprehension_examples()
    dict_comprehension_examples()
    set_comprehension_examples()
    combined_analysis()


if __name__ == "__main__":
    main()
