from typing import List
from data_structures.DisjointSet import DisjointSet

# Time Complexity: O(k+n) + O(k * n * log(n))
# Space Complexity: O(k+n)

# Approach: use DSU Data Structure


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # Set up an email to name map.
        email_to_name = {}
        for acc in accounts:
            for email in acc[1:]:
                email_to_name[email] = acc[0]

        # Set up an email to idx map
        email_to_idx = {}
        idx_to_email = {}
        idx = 0
        for acc in accounts:
            for email in acc[1:]:
                if email not in email_to_idx:
                    email_to_idx[email] = idx
                    idx_to_email[idx] = email
                    idx += 1

        # DSU Approach
        dsu = DisjointSet(len(email_to_idx))
        for acc in accounts:
            for i in range(2, len(acc)):
                dsu.unite(email_to_idx[acc[i-1]], email_to_idx[acc[i]])

        grouped_map = {}
        for k, v in email_to_idx.items():
            parent_email = idx_to_email[dsu.find(v)]
            if parent_email in grouped_map:
                grouped_map[parent_email].append(k)
            else:
                grouped_map[parent_email] = [k]

        res_arr = [[email_to_name[k]] +  sorted(v) for k, v in grouped_map.items()]
        return res_arr

if __name__ == "__main__":


    test_cases = [
        [
            ["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ],
        [
            ["David","David0@m.co","David1@m.co"],
            ["David","David3@m.co","David4@m.co"],
            ["David","David4@m.co","David5@m.co"],
            ["David","David2@m.co","David3@m.co"],
            ["David","David1@m.co","David2@m.co"]
        ],
        [
            ["Test","test1@ap.com","test2@ap.com"],
            ["Test","test2@ap.com","test1@ap.com"],
        ]
    ]

    sln = Solution()
    for test in test_cases:
        print(sln.accountsMerge(test))
