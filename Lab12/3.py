from datetime import datetime, timedelta

class DateDiffrence:
    
    def __init__(self, date1, date2) :
        self.date1 = datetime.strptime(date1, "%Y%m%d")
        self.date2 = datetime.strptime(date2, "%Y%m%d")

    def days_between(self) :
        return abs((self.date2 - self.date1).days)
    

def main() :
    date = input()
    
    while date != '' :
        date1, date2 = date.split()
        days = DateDiffrence(date1, date2).days_between()
        print(days)
        date = input()
       
       
if __name__ == "__main__" :
    main()