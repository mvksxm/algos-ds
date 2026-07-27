from tester import Tester

# n -> len(boxes); m -> len(warehouse)
# TC -> O(n*log(n) + m)
# SC -> O(n+m)

def put_boxes_warehouse(boxes, warehouse):
    wh_capacity = []
    prev_capacity = float('inf')
    sorted_boxes = sorted(boxes, reverse=True)

    for cap in warehouse:
        if cap < prev_capacity: prev_capacity = cap
        wh_capacity.append(prev_capacity)

    res = 0
    w_p = len(warehouse) - 1
    b_p = len(sorted_boxes) - 1

    while w_p >= 0 and b_p >= 0:
        cur_box = sorted_boxes[b_p]
        w_space = wh_capacity[w_p]

        if cur_box <= w_space:
            res += 1
            b_p -= 1

        w_p -= 1

    return res


if __name__ == "__main__":
    tst = Tester()

    test_list = [
        # Official examples
        [[[4, 3, 4, 1], [5, 3, 3, 4, 1]], 3],
        [[[1, 2, 2, 3, 4], [3, 4, 1, 2]], 3],
        [[[1, 2, 3], [1, 2, 3, 4]], 1],

        # Empty inputs
        [[[], [1, 2, 3]], 0],
        [[[1, 2, 3], []], 0],

        # Single box
        [[[1], [1]], 1],
        [[[2], [1]], 0],
        [[[1], [2]], 1],

        # Single warehouse slot
        [[[1, 2, 3], [2]], 1],
        [[[3, 4], [2]], 0],

        # All boxes fit
        [[[1, 1, 1], [2, 2, 2]], 3],
        [[[2, 2, 2], [2, 2, 2]], 3],

        # No boxes fit
        [[[5, 6, 7], [1, 2, 3]], 0],

        # Bottleneck near entrance
        [[[1, 2, 3], [3, 1, 3]], 2],
        [[[2, 2, 2], [3, 1, 3]], 1],

        # Bottleneck at the end
        [[[1, 2, 3], [3, 3, 3, 1]], 3],
        [[[1, 1, 1], [3, 3, 3, 1]], 3],

        # More boxes than rooms
        [[[1, 1, 1, 1, 1], [2, 2]], 2],
        [[[2, 2, 2, 2], [2, 2, 2]], 3],

        # More rooms than boxes
        [[[2, 3], [5, 5, 5, 5, 5]], 2],

        # Duplicate sizes
        [[[2, 2, 2], [2, 2, 2, 2]], 3],
        [[[3, 3, 3], [3, 2, 3, 3]], 1],

        # Tricky cases
        [[[4, 4, 1], [5, 4, 3, 2]], 3],
        [[[5, 4, 3, 2, 1], [5, 4, 3, 2, 1]], 5],
        [[[5, 5, 1], [6, 5, 4]], 3],
        [[[2, 3, 4], [4, 2, 3]], 2],
    ]

    tst.array_test(test_list, put_boxes_warehouse)
