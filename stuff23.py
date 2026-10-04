"""Odds and ends."""

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

def flatten(xs):
    return [y for x in xs for y in x]

if __name__ == "__main__":
    print(most_common("abracadabra"))

# cleanup later
