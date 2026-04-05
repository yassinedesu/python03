from typing import Generator


def game_event_generator(count: int) -> Generator:
    """Yields game events one at a time."""
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    for i in range(count):
        yield {
            "player": players[i % 3],
            "level": (i % 20) + 1,
            "action": actions[i % 3],
        }


def fibonacci_generator() -> Generator:
    """Yields fibonacci numbers infinitely."""
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator() -> Generator:
    """Yields prime numbers infinitely."""
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, num)):
            yield num
        num += 1


def main() -> None:
    total = 0
    high_level = 0
    treasure = 0
    levelup = 0

    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...\n")

    for event in game_event_generator(1000):
        if total < 3:
            print(f"Event {total + 1}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
        total += 1
        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure += 1
        if event["action"] == "leveled up":
            levelup += 1

    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelup}")
    print("Memory usage: Constant (streaming)")

    fib = fibonacci_generator()
    fib_values = [next(fib) for _ in range(10)]

    prime = prime_generator()
    prime_values = [next(prime) for _ in range(5)]

    print("\n=== Generator Demonstration ===")
    print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib_values))}")
    print(f"Prime numbers (first 5): {', '.join(map(str, prime_values))}")


if __name__ == "__main__":
    main()