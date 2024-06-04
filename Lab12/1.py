from datetime import datetime, timedelta

class LastDayOfMonth :
    
    def __init__(self, year, month) :
        self.year = year
        self.month = month
    
    def get_last_day_weekday(self) :
        if self.month == 12 :
            next_month = datetime(self.year + 1, 1, 1)
        else :
            next_month = datetime(self.year, self.month + 1, 1)
    
        last_day = next_month - timedelta(days = 1)
        return last_day.weekday() + 1

def main() :
    user_input = input()
    
    while(user_input != '') :
        year, month = map(int, user_input.split())
        day = LastDayOfMonth(year, month).get_last_day_weekday()
        print(day)
        user_input = input()    


if __name__ == "__main__" :
    main()