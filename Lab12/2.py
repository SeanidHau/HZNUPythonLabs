from datetime import datetime, timedelta

class SundayCounter :
    
    def __init__(self, start = 1901, end = 2000) :
        self.start = start
        self.end = end
    
    def counter(self) :
        count = 0
        for year in range(self.start, self.end + 1) :
            for month in range(1, 13) :
                first_day_of_month = datetime(year, month, 1)
                if first_day_of_month.weekday() == 6 :
                    count += 1
        return count
    

def main() :
    sum = SundayCounter().counter()
    print(sum)
       
       
if __name__ == "__main__" :
    main()