class Date:

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return 'Day: {}\tMonth: {}\tYear: {}'. format(self.day, self.month, self.year)

    @classmethod
    def is_date_valid(cls, data: str) -> bool:
        day, month, year = map(int, data.split('-'))
        data_obj = cls(day, month, year)
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999

    @classmethod
    def from_string(cls, data: str) -> 'Date':
        day, month, year = map(int, data.split('-'))
        data_obj = cls(day, month, year)
        return data_obj

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))