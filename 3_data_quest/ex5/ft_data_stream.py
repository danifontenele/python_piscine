def generate_game_events(n: int):
	players = ["alice", "daniel", "charles", "bob", "jhon"]
	actions = ["found treasure", "died", "leveled up", "killed monster"]
	for i in range(n):
		yield {
			"id" : i,
			"player" : players[i % len(players)],
			"level" : (i % 20) + 1,
			"type" : actions[i % len(actions)]
		}


def process_stream(stream):
	high_level = 0
	treasure = 0
	kills = 0
	deaths = 0
	events = 0

	for event in stream:
		print(f"Event {event['id']}: Player {event['player']} "
		      f"(level {event['level']}) {event['type']}")
		if event["level"] >= 10:
			high_level += 1
		if event["type"] == "found treasure":
			treasure += 1
		if event["type"] == "died":
			deaths += 1
		if event["type"] == "killed monster":
			kills += 1
		events += 1
	print("\n=== Stream Analytics ===")
	print(f"Total events processed: {events}")
	print(f"High-level players(10+): {high_level}")
	print(f"Treasure events: {treasure}")
	print(f"Total monsters killed: {kills}")
	print(f"Total deaths(players): {deaths}")


def get_fibonacci(n: int):
	a, b = 0, 1
	for _ in range(n):
		yield a
		a, b = b, (a + b)


def get_primes(n: int):
    pass


def main():
	print("=== Game Data Stream Processor ===\n")
	n = 1000
	stream = generate_game_events(n)
	print(f"Processing {n} events...\n")
	process_stream(stream)

	print("\nMemory usage: Constant (streaming)")
	print("Processing time: Demonstrates on-demand generation")
	print("\n=== Generator Demonstration ===")
	n = 10
	sequence = []
	for value in get_fibonacci(n):
		sequence.append(value)
	print(f"fibonacci sequence(first {n}): {sequence}")
	n = 5
	sequence = []
	for value in get_primes(n):
		sequence.append(value)
	print(f"Prime numbers (first {n}): {sequence}")



if __name__ == "__main__":
	main()
	
