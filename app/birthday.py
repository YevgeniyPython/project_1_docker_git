from datetime import datetime
from field import Field

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
            self.str = self.value.strftime("%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
# print(Birthday("22.02.2022"))
# r = Birthday("12.02.2000")
# print(r.str)