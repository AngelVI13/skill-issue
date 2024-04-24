import csv
from random import randrange, choice
from dataclasses import dataclass
from enum import Enum, auto
from itertools import cycle

HEADERS = ["Red", "Yellow", "Green", "TimeActive", "Time"]


class Color(Enum):
    Red = auto()
    Yellow = auto()
    Green = auto()


PATTERN = [Color.Red, Color.Yellow, Color.Green, Color.Yellow]


@dataclass
class Row:
    Red: int
    Yellow: int
    Green: int
    TimeActive: int
    Time: str

    def to_list(self) -> list:
        return [self.Red, self.Yellow, self.Green, self.TimeActive, self.Time]

    def set_color(self, color: Color):
        match color:
            case Color.Red:
                self.Red = 1
            case Color.Yellow:
                self.Yellow = 1
            case Color.Green:
                self.Green = 1
            case _:
                assert False, f"not handled {color=}"


def write_to_file(filename: str, data: list[Row]):
    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(HEADERS)

        for row in data:
            writer.writerow(row.to_list())


def calculate_corrupt_idxs(n: int, n_corrupted: int) -> list[int]:
    corrupt_idxs = []
    while len(corrupt_idxs) < n_corrupted:
        new_corrupt_idx = randrange(0, n)
        if new_corrupt_idx in corrupt_idxs:
            continue

        corrupt_idxs.append(new_corrupt_idx)

    corrupt_idxs.sort(key=lambda x: -x)
    return corrupt_idxs


def generate_data(n: int, n_corrupted: int) -> list[Row]:
    assert n > 0, f"expected n >= 0 ({n})"
    assert (
        n_corrupted >= 0 and n_corrupted < n
    ), f"expected 0 <= n_corrupted ({n_corrupted}) < n"

    all_corruption_idxs = calculate_corrupt_idxs(n, n_corrupted)

    data = []
    start_time = 0
    corrupt_idx = all_corruption_idxs.pop()
    for idx, color in enumerate(cycle(PATTERN)):
        if idx == n:
            break

        time_active = randrange(1, 10)
        start_time += time_active
        min, sec = divmod(start_time, 60)
        hour, min = divmod(min, 60)
        start_time_str = f"{hour}:{min:02}:{sec:02}"

        row = Row(Red=0, Yellow=0, Green=0, TimeActive=time_active, Time=start_time_str)
        row.set_color(color)

        if corrupt_idx is not None and idx == corrupt_idx:
            row.set_color(choice([color.Red, color.Yellow, color.Green]))
            corrupt_idx = None if not all_corruption_idxs else all_corruption_idxs.pop()

        data.append(row)

    return data


def main():
    data = generate_data(15000, 1000)
    write_to_file("data.txt", data)


if __name__ == "__main__":
    main()
