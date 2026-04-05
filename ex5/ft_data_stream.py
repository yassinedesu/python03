from typing import Generator


def game_event_generator(count: int) -> Generator:
    """
    Yields game events one at a time — never stores all of them in memory.
    """
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(count):
        # yield pauses the function and sends one value to the caller
        # next call to the generator resumes right after this line
        yield {
            "player": players[i % len(players)],  # cycles through players
            "level": (i % 20) + 1,  # levels 1-20, repeating
            "action": actions[i % len(actions)],  # cycles through actions
        }


def fibonacci_generator() -> Generator:
    """Yields fibonacci numbers infinitely — caller decides when to stop."""
    a, b = 0, 1
    while True:
        yield a  # pause and send current value
        a, b = b, a + b  # update for next call


def prime_generator() -> Generator:
    """Yields prime numbers one by one, infinitely."""
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num  # only yields if num is prime
        num += 1


def process_stream(count: int) -> None:
    """Loops over the generator, tracking stats without storing all events."""
    total = 0
    high_level = 0
    treasure = 0
    levelup = 0

    # the for loop calls the generator one event at a time
    for event in game_event_generator(count):
        # print first 3 events to show what they look like
        if total < 3:
            print(
                f"Event {total + 1}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}"
            )

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


def demo_generators() -> None:
    """Shows fibonacci and prime generators using next() to pull values."""
    print("\n=== Generator Demonstration ===")

    # create the generator object — nothing runs yet
    fib = fibonacci_generator()

    # next() manually pulls one value at a time from the generator
    fib_values = [next(fib) for _ in range(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib_values))}")

    prime = prime_generator()
    prime_values = [next(prime) for _ in range(5)]
    print(f"Prime numbers (first 5): {', '.join(map(str, prime_values))}")


def main() -> None:
    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...\n")

    process_stream(1000)
    demo_generators()


if __name__ == "__main__":
    main()
