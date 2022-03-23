from functools import partial
from typing import Callable, List


def get_first_n_average(numbers: List[int], n: int) -> float:
    if n > len(numbers):
        raise Exception("n too big")
    return sum(numbers[:n]) / n


def get_first_n_average_closure(n: int) -> Callable:
    # example of closure
    def get_first_n_average_inside(numbers: List[int]) -> float:
        if n > len(numbers):
            raise Exception("n too big")
        return sum(numbers[:n]) / n

    return get_first_n_average_inside


if __name__ == "__main__":

    print(get_first_n_average([1, 2, 3, 4], 3))

    get_first_2_avg = partial(get_first_n_average, n=2)

    print(get_first_2_avg(numbers=[1, 2, 3, 4]))

    get_1234_first_n_avg = partial(get_first_n_average, numbers=[1, 2, 3, 4])

    print(get_1234_first_n_avg(n=4))

    print(get_first_n_average_closure(n=4)(numbers=[1, 2, 3, 4, 5, 6]))
