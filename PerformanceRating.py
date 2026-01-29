class PerformanceRating:
    def rate(self, time, professional):
        
        if time < 0 or time > 60:
            return "ERROR"

        if time >= 21:
            if professional:
                return 40
            else:
                return 20
        elif time == 16:
            if professional:
                return 70
            else:
                return 45
        elif time >= 13:
            if professional:
                return 80
            else:
                return 50
        else: # time is 0-12
            if professional:
                return 120
            else:
                return 80
