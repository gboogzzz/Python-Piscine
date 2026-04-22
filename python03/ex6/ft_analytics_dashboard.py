def list_comprehension_demo(players: list) -> None:
    print("=== List Comprehension Examples ===")
    high_scorers = [player["name"] for player in players if
                    player["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    double_scores = [player["score"] * 2 for player in players if
                     player["score"] > 2000]
    print(f"Scores doubled: {double_scores}")
    active_players = [player["name"] for player in players if
                      player["status"] == "active"]
    print(f"Active players: {active_players}\n")


def dict_comprehension_demo(players: list) -> None:
    print("=== Dict Comprehension Examples ===")
    player_scores = {player["name"]: player["score"] for player in players}
    print(f"Player scores: {player_scores}")
    high = len([player for player in players if player["score"] > 2000])
    medium = len([player for player in players if
                  1500 <= player["score"] <= 2000])
    low = len([player for player in players if player["score"] < 1500])
    score_categories = {"high": high, "medium": medium, "low": low}
    print(f"Score categories: {score_categories}")
    achievement_count = {player["name"]: len(player["achievements"])
                         for player in players}
    print(f"Achievement counts: {achievement_count}\n")


def set_comprehension_demo(players: list) -> None:
    print("=== Set Comprehension Examples ===")
    unique_players = {player["name"] for player in players}
    print(f"Unique players: {unique_players}")
    unique_achievements = {achievement for player in players for
                           achievement in player["achievements"]}
    print(f"Unique achievements: {unique_achievements}")
    unique_regions = {player["region"] for player in players}
    print(f"Unique regions: {unique_regions}\n")


def combined_analysis(players: list) -> None:
    print("=== Combined Analysis ===")
    total_players = len([player["name"] for player in players])
    print(f"Total players: {total_players}")
    unique_achievements_total = len({achievement for player in players for
                                     achievement in player["achievements"]})
    print(f"Total Unique Achievements: {unique_achievements_total}")
    average_score = sum([player["score"] for player
                         in players]) / len([player["name"] for player
                                             in players])
    print(f"Average Score: {average_score}")
    max_score = max([player["score"] for player in players])
    name_player = [player["name"] for player in players if
                   player["score"] == max_score]
    max_playerachievements = len([player["achievements"] for player in players
                                  if player["name"] == name_player[0]])
    print(f"Top performer: {name_player} ({max_score} points, "
          f"{max_playerachievements} achievements)")


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")
    players = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "treasure_hunter",
                "speed_demon",
            ],
            "status": "active",
            "region": "north",
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": ["first_kill", "level_10", "boss_slayer"],
            "status": "active",
            "region": "east",
        },
        {
            "name": "charlie",
            "score": 2150,
            "achievements": [
                "level_10",
                "boss_slayer",
                "treasure_hunter",
                "boss_slayer",
                "speed_demon",
                "perfectionist",
                "collector",
            ],
            "status": "active",
            "region": "central",
        },
        {
            "name": "diana",
            "score": 2050,
            "achievements": ["first_kill", "level_10"],
            "status": "inactive",
            "region": "north",
        },
    ]
    list_comprehension_demo(players)
    dict_comprehension_demo(players)
    set_comprehension_demo(players)
    combined_analysis(players)


if __name__ == "__main__":
    main()
