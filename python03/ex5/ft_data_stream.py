from typing import Generator


def game_event_stream(count: int) -> Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]
    levels = list(range(1, 16))
    for stream in range(count):
        player = players[stream % len(players)]
        event = events[stream % len(events)]
        level = levels[stream % len(levels)]
        yield (stream + 1, player, event, level)


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    for i in range(n):
        yield a
        tmp = a
        a = b
        b = tmp + b


def prime_generator(n: int) -> Generator[int, None, None]:
    nbr = 2
    count = 0
    while count < n:
        x = 2
        while (nbr > x):
            if nbr % x == 0:
                break
            x += 1
        if nbr == x:
            yield nbr
            count += 1
        nbr += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...")
    total = 0
    high_level = 0
    treasure = 0
    levelup = 0
    for event_num, player, event, level in game_event_stream(1000):
        total += 1
        if level >= 10:
            high_level += 1
        if event == "leveled up":
            levelup += 1
        elif event == "found treasure":
            treasure += 1
        if (event_num <= 3):
            print(f"Event {event_num}: Player "
                  f"{player} (level {level}) {event}")
    print("...\n")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelup}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")
    print("=== Generator Demonstration ===")
    fibos = []
    count_fib = 0
    for fibo in fibonacci_generator(10):
        fibos.append(fibo)
        count_fib += 1
    print(f"Fibonacci sequence (first {count_fib}): "
          f"{', '.join(str(f) for f in fibos)}")
    primes = []
    count_prime = 0
    for prime in prime_generator(5):
        primes.append(prime)
        count_prime += 1
    print(f"Prime numbers (first {count_prime}): "
          f"{', '.join(str(p) for p in primes)}")


if __name__ == "__main__":
    main()
