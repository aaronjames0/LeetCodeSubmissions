class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        seats = []
        open_seat = 0
        departures = []
        max_time = times[targetFriend][0]
        arrivals = [(arrive, leave) for i, (arrive, leave) in enumerate(times) if arrive < max_time]
        heapify(arrivals)

        while arrivals:
            arrive, leave = heappop(arrivals)
            while departures and departures[0][0] <= arrive:
                time, seat = heappop(departures)
                if seat == open_seat - 1:
                    open_seat -= 1
                else:
                    heappush(seats, seat)
            if seats:
                seat = heappop(seats)
            else:
                seat = open_seat
                open_seat += 1
            if leave <= max_time:
                heappush(departures, (leave, seat))
            
        if seats:
            result = seats[0]
        else:
            result = open_seat
            
        for time, seat in departures:
            if seat < result:
                result = seat
        return result