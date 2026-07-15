from typing import Callable
from .models import ListNode


class Tester:

    def _display_results(self, results: list, test_list: list) -> bool:

        failed_cnt = 0
        for i in range(len(results)):
            if not results[i][0]:
                failed_cnt += 1
                print(f"Failed Test Case -> Test Data: {test_list[i][0]}; Intended Result: {test_list[i][1]}; Returned Result: {results[i][1]}")

        if failed_cnt > 0:
            print(f"{failed_cnt} out of {len(test_list)} tests failed!")
            return False

        print("All Test Cases passed!")
        return True

    def array_test(self, test_list: list, func_to_test: Callable) -> bool:

        results = []
        for case in test_list:
            res = func_to_test(*case[0])
            is_success = res == case[1]
            results.append([is_success, res])

        status = self._display_results(results, test_list)
        return status

    def generate_linked_list(self, arr: list) -> ListNode:

        if not arr: raise Exception("Array provided for the generation of Linked List is empty!")

        node = head = ListNode(arr[0])
        for i in range(1, len(arr)):
            curr_node = ListNode(arr[i])
            node.next = curr_node
            node = curr_node

        return head

    def decode_linked_list(self, head: ListNode) -> list:
        decoded_list = []

        node = head
        while node is not None:
            decoded_list.append(node.val)
            node = node.next

        return decoded_list

    def linked_list_test(self, test_list: list, func_to_test: Callable) -> bool:

        results = []

        for test in test_list:

            args_raw = test[0]
            args_processed = [
                self.generate_linked_list(arg) if type(arg) == list else arg for arg in args_raw
            ]

            res = func_to_test(*args_processed)
            intended_res = test[1]

            if type(intended_res) == list and type(res) == ListNode:
                res = self.decode_linked_list(res)

            is_success = res == intended_res
            results.append([is_success, res])

        status = self._display_results(results, test_list)
        return status




