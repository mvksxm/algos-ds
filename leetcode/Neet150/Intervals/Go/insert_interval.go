package main

import "fmt"

// Time Complexity: O(n)
// Space Complexity: O(1)

// Step 1
// Iterate through the intervals array. Keep track of the second value of a previous interval (store it in the prevVal var).
// In case if 'prevVal' < currInterval[0] && currInterval[1] < interval[i][0] (first value of a currently observed interval
// in a loop) -> it means that the currInterval can be added now into the final 'res' array, otherwise, it means there is
// a conflict (Step 2) or the observer interval in a loop  is not touching the range in the 'currInterval' at all and
// can be freely added to the final 'res' array.

// Step 2
// In case, if a conflict observed between currently observed interval in a loop and the currInterval, we need to mutate
// 'currInterval' in such a way that conflicts are resolved. Specifically, first val of a new interval will be equal to
// the min value between min of a currInterval and a min of a currently observed in a loop and the second val will be equal to
// the max value between max of a currInterval and the max of  currently observed in a loop. After mutation of the
// 'currInterval' was performed, we are continuously repeating a step 1 and step 2 until the end of the intervals array.

func Insert(intervals [][]int, newInterval []int) [][]int {
	currInterval := newInterval
	var res [][]int

	prevVal := -1
	isAppended := false
	for i := 0; i < len(intervals); i++ {

		if currInterval[1] < intervals[i][0] && currInterval[0] > prevVal {
			res = append(res, currInterval)
			res = append(res, intervals[i])
			isAppended = true
		} else if currInterval[0] > intervals[i][1] || currInterval[1] < intervals[i][0] {
			res = append(res, intervals[i])
		} else {
			currInterval[0] = min(currInterval[0], intervals[i][0])
			currInterval[1] = max(currInterval[1], intervals[i][1])
			continue
		}
		prevVal = intervals[i][1]
	}

	if !isAppended {
		res = append(res, currInterval)
	}

	return res
}

func main() {

	// Test Cases (Insert Intervals)
	//intervals := [][]int{{1, 5}}
	//newInterval := []int{2, 7}
	//intervals := [][]int{{1, 3}, {4, 6}}
	//newInterval := []int{2, 5}
	intervals := [][]int{{1, 5}}
	newInterval := []int{6, 8}
	fmt.Println(Insert(intervals, newInterval))
}
