"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

    Input: intervals = [[1,3],[6,9]], new_interval = [2,5]
    Output: [[1,5],[6,9]]
Example 2:

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], new_interval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, new_interval):
        """
        :type intervals: List[Interval]
        :type new_interval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [new_interval]
        if intervals[-1].end < new_interval.start:
            return intervals + [new_interval]
        if intervals[0].start > new_interval.end:
            return [new_interval] + intervals
        merged_intervals = []
        cached_interval = None
        for i in range(len(intervals)):
            interval = intervals[i]
            if cached_interval == None:
                if new_interval.start > interval.end:
                    merged_intervals.append(interval)
                elif new_interval.end < interval.start:
                    if merged_intervals and merged_intervals[-1].end < new_interval.start:
                        merged_intervals.append(new_interval)
                    merged_intervals.append(interval)
                else:
                    cached_interval = Interval()
                    if new_interval.start < interval.start:
                        cached_interval.start = new_interval.start
                    else:
                        cached_interval.start = interval.start
                    
                    if new_interval.end <= interval.end:
                        cached_interval.end = interval.end
                        merged_intervals.append(cached_interval)
                        cached_interval = None
                    elif len(intervals) == i + 1:
                        cached_interval.end = new_interval.end
                        merged_intervals.append(cached_interval)
                        cached_interval = None
                    else:
                        continue
            else:
                if new_interval.end < interval.start:
                    cached_interval.end = new_interval.end
                    merged_intervals.append(cached_interval)
                    cached_interval = None
                    merged_intervals.append(interval)
                elif new_interval.end <= interval.end: 
                    cached_interval.end = interval.end
                    merged_intervals.append(cached_interval)
                    cached_interval = None
                elif len(intervals) == i + 1:
                    cached_interval.end = new_interval.end
                    merged_intervals.append(cached_interval)
                    cached_interval = None
                else:
                    continue
        return merged_intervals

import unittest
class TestFunc(unittest.TestCase):
    def to_list(self, intervals):
        return map(lambda x: [x.start, x.end], intervals)
    
    def to_intervals(self, intervals):
        return map(lambda x: Interval(x[0], x[1]), intervals)

    def test_1(self):
        intervals = [[1,3],[6,9]]
        new_interval = [2, 5]
        merged_intervals = [[1,5],[6,9]]
        intervals = self.to_intervals(intervals)
        new_interval = Interval(new_interval[0], new_interval[1])
        self.assertEqual(merged_intervals, self.to_list(Solution().insert(intervals, new_interval)))
    
    def test_2(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        new_interval = [4,8]
        merged_intervals = [[1,2],[3,10],[12,16]]
        intervals = self.to_intervals(intervals)
        new_interval = Interval(new_interval[0], new_interval[1])
        self.assertEqual(merged_intervals, self.to_list(Solution().insert(intervals, new_interval)))

    def test_3(self):
        intervals = [[1,3],[6,9]]
        new_interval = [2,5]
        merged_intervals = [[1,5],[6,9]]
        intervals = self.to_intervals(intervals)
        new_interval = Interval(new_interval[0], new_interval[1])
        self.assertEqual(merged_intervals, self.to_list(Solution().insert(intervals, new_interval)))

    def test_4(self):
        intervals = [[1,5]]
        new_interval = [2,7]
        merged_intervals = [[1,7]]
        intervals = self.to_intervals(intervals)
        new_interval = Interval(new_interval[0], new_interval[1])
        self.assertEqual(merged_intervals, self.to_list(Solution().insert(intervals, new_interval)))

    def test_5(self):
        intervals = [[1,5]]
        new_interval = [6,8]
        merged_intervals = [[1,5], [6,8]]
        intervals = self.to_intervals(intervals)
        new_interval = Interval(new_interval[0], new_interval[1])
        self.assertEqual(merged_intervals, self.to_list(Solution().insert(intervals, new_interval)))

    def test_6(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        new_interval = [4,8]
        merged_intervals = [[1,2],[3,10],[12,16]]
        intervals = self.to_intervals(intervals)
        new_interval = Interval(new_interval[0], new_interval[1])
        self.assertEqual(merged_intervals, self.to_list(Solution().insert(intervals, new_interval)))

if __name__ == '__main__':
    unittest.main()
