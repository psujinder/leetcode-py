from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 1

        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)

        l = len(intervals)

        start_pointer = 1
        end_pointer = 0

        while start_pointer < l:
            if start_times[start_pointer] >= end_times[end_pointer]:
                rooms -= 1
                end_pointer += 1

            rooms += 1
            start_pointer += 1

        return rooms
