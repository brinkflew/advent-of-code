from pathlib import Path


input_file = Path(__file__).parent / "input.txt"

# --- Part 1 -------------------------------------------------------------------


COLORS = ["red", "green", "blue"]


def parse_games(f):
    games = {}

    for line in f:
        label, game = line.split(": ", 1)
        game_id = int(label.lstrip("Game "))
        games[game_id] = []

        for move in game.split(";"):
            colors = {color: 0 for color in COLORS}

            for cubes in move.split(","):
                count, color = cubes.strip().split()
                colors[color] = int(count)

            games[game_id].append(colors)

    return games


def all_moves_possible(moves):
    return all(move["red"] <= 12 and move["green"] <= 13 and move["blue"] <= 14 for move in moves)


def challenge_01():
    with input_file.open() as f:
        games = parse_games(input_file.open())
        possible_games = {game_id: moves for game_id, moves in games.items() if all_moves_possible(moves)}
        return sum(possible_games.keys())


# --- Part 2 -------------------------------------------------------------------


def max_color_count(moves):
    colors = {color: 0 for color in COLORS}

    for move in moves:
        for color, count in move.items():
            colors[color] = max(colors[color], count)

    return list(colors.values())


def challenge_02():
    with input_file.open() as f:
        games = parse_games(input_file.open())

        total = 0

        for game in games.values():
            power_set = max_color_count(game)
            total += power_set.pop() * power_set.pop() * power_set.pop()

        return total
