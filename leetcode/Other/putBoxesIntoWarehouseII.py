from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        res = 0

        #  Data preparation
        sorted_boxes = sorted(boxes, reverse=True)

        wh_capacity = []
        for i in range(len(warehouse)):
            updated_cc = warehouse[i]
            if i > 0 and i < len(warehouse) - 1:
                updated_cc = min(warehouse[i], max(warehouse[i+1], warehouse[i-1]))
            wh_capacity.append(updated_cc)

        w_left_p = 0
        w_right_p = len(warehouse) - 1
        boxes_p = 0

        while w_left_p <= w_right_p and boxes_p < len(boxes):

            left_val = wh_capacity[w_left_p]
            right_val = wh_capacity[w_right_p]
            curr_box = sorted_boxes[boxes_p]

            if left_val >= curr_box:
                res += 1
                w_left_p += 1
            elif right_val >= curr_box:
                res += 1
                w_right_p -= 1

            boxes_p += 1

        return res
