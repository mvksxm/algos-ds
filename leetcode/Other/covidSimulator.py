"""
Overview

This question is about building an Covid19 infection simulation algorithm assuming covid 19
transmits when infected users in the same location and same time as non infected users.
Deliver the question by explaining the problem, then walk through an example and ask the
candidate to solve it to verify their understanding.

Instructions

Question delivery

Given an array of visits(user_id, location_id, start_time, end_time) and an array of users
infected with Covid 19 users write a function that returns the total number of users that caught
Covid19.

When a user gets infected they will start infecting other users afterwards immediately
meaning the person becomes contagious right after being infected and there is no
incubation period.

Example

visits = [
    [0, 0, 1, 3],
    [0, 1, 4, 5],
    [0, 2, 8, 9],
    [1, 1, 4, 6],
    [2, 2, 7, 9],
    [3, 2, 6, 8],
]
infected = [1]
infection_simulator(visits, infected) # returns 3
# first 1 infects 0 at location 1
# then 0 infects 2 at location 2
# 3 remains uninfected cause they leave as soon as 0

Approach

1) Create a map: location -> infected interval.
2) Add to the map all the infected intervals we are aware of already.
3) Create an array in the following format arr[][]; arr[user_idx] -> [[loc_id, start_time, end_time]]
2) Sort input array by start_time, end_time in ascending order.
3) Iterate through the sorted array

# visited_set: set;
1) # 1: [1]
2) # 1: [[4,5], [4,6]] -> 0 user and 5 end time; inputting (1,0) and (1,1) to the visited set.
3) # 0: [1, 2] -> 2 loc only (because 1 is visited already) and also passing 5 as the min time after which person can be infected.
4) # 2: [ [8,9], [7, 9], [3, 9] ] - all here are infected; performing step 2 one more time on each infected person.
5) Base Case of a recursion: no more locs to visit or end of the inner for loop.

visits_sorted = [
    [0, 0, 1, 3],
    [3, 2, 3, 9],
    [0, 1, 4, 5],
    [1, 1, 4, 6],
    [2, 2, 7, 9],
    [0, 2, 8, 9],
]

infected = [1]

"""
from collections import defaultdict

from tester import Tester

# Approach: DFS


def covidSimulator(visits: list, infected: list):

    loc_to_users = defaultdict(dict)
    user_to_locs = defaultdict(set)
    visited_set = set()
    infected_set = {inf for inf in infected}

    for visit in visits:
        # loc_to_users[visit[1]].add(visit[0])
        loc_user_timestamps =  loc_to_users[visit[1]].get(visit[0])
        if not loc_user_timestamps:
            loc_to_users[visit[1]][visit[0]] = {(visit[2], visit[3])}
        else:
            loc_to_users[visit[1]][visit[0]].add((visit[2], visit[3]))

        user_to_locs[visit[0]].add(visit[1])

    def dfs_users(loc: int, inf_id: int, min_infected_time: int):
        users = loc_to_users[loc]
        infection_timestamps = users[inf_id]

        for inf_ts in infection_timestamps:
            if inf_ts[0] >= min_infected_time:
                for user, timestamps in users.items():
                    for i, user_ts in enumerate(timestamps):
                        record_id = (loc,user,i)
                        if (
                                record_id not in visited_set
                                and not (user_ts[1] <= inf_ts[0] or inf_ts[1] <= user_ts[0])
                        ):
                            visited_set.add(record_id)
                            infected_set.add(user)
                            dfs_locs(user, user_ts[1])


    def dfs_locs(inf: int, min_infected_time: int):
        infected_locs = user_to_locs[inf]
        for loc in infected_locs:
            dfs_users(loc, inf, min_infected_time)


    for inf in infected:
        dfs_locs(inf, 0)

    return len(infected_set)

if __name__ == "__main__":
    tst = Tester()
    test_list = [

        # Example
        [
            [[
                [0,0,1,3],
                [0,1,4,5],
                [0,2,8,9],
                [1,1,4,6],
                [2,2,7,9],
                [3,2,6,8]
            ],
                [1]],
            3
        ],

        # No visits
        [
            [[],
             [0]],
            1
        ],

        # Nobody initially infected
        [
            [[
                [0,0,1,2],
                [1,0,1,2]
            ],
                []],
            0
        ],

        # Single user
        [
            [[
                [0,0,1,2]
            ],
                [0]],
            1
        ],

        # No overlap
        [
            [[
                [0,0,1,2],
                [1,0,2,3]
            ],
                [0]],
            1
        ],

        # Complete overlap
        [
            [[
                [0,0,1,5],
                [1,0,2,4]
            ],
                [0]],
            2
        ],

        # Different locations
        [
            [[
                [0,0,1,5],
                [1,1,1,5]
            ],
                [0]],
            1
        ],

        # Simple chain
        [
            [[
                [0,0,3,5],
                [1,0,2,4],
                [2,0,4,6]
            ],
                [1]],
            2
        ],

        # Chain should stop
        [
            [[
                [0,0,3,4],
                [1,0,2,3],
                [2,0,4,5]
            ],
                [1]],
            1
        ],

        # Two initial infected
        [
            [[
                [0,0,2,5],
                [1,0,1,3],
                [2,0,4,6],
                [3,1,1,5]
            ],
                [1,2]],
            3
        ],

        # Infect multiple users
        [
            [[
                [0,0,1,10],
                [1,0,2,3],
                [2,0,4,5],
                [3,0,6,7]
            ],
                [0]],
            4
        ],

        # Everyone already infected
        [
            [[
                [0,0,1,2],
                [1,0,1,2]
            ],
                [0,1]],
            2
        ],

        # Multiple visits
        [
            [[
                [0,0,1,2],
                [0,1,5,6],
                [1,1,5,7]
            ],
                [0]],
            2
        ],

        # Infection across locations
        [
            [[
                [0,0,1,3],
                [1,0,2,4],
                [1,1,5,6],
                [2,1,5,7]
            ],
                [0]],
            3
        ],

        # Disconnected groups
        [
            [[
                [0,0,1,3],
                [1,0,2,3],
                [2,1,1,3],
                [3,1,2,3]
            ],
                [0]],
            2
        ],

        # Same user revisits location
        [
            [[
                [0,0,1,2],
                [0,0,5,6],
                [1,0,5,6]
            ],
                [0]],
            2
        ],

        # Immediate contagion
        [
            [[
                [0,0,2,4],
                [1,0,1,3],
                [0,1,5,6],
                [2,1,5,7]
            ],
                [1]],
            3
        ],

        # Endpoint touching only
        [
            [[
                [0,0,1,2],
                [1,0,2,5]
            ],
                [0]],
            1
        ],

        # Large overlap
        [
            [[
                [0,0,1,100],
                [1,0,20,30],
                [2,0,40,50],
                [3,0,60,70],
                [4,0,80,90]
            ],
                [0]],
            5
        ]
    ]
    tst.array_test(test_list, covidSimulator)
    # print(covidSimulator(visits,infected))
