# {'date': datetime(2020, 6, 15), 'guests': 3, 'subscribers': 4, 'store_managers': 5, 'store_owners': 6, 'system_managers': 7},
#         #                          {'date':
import datetime

from src.main.DataAccessLayer.DataAccessFacade import DataAccessFacade


class Statistics:

    def __init__(self):
        self.__date = datetime.datetime.today()
        self.__guests_amount : int = 0
        self.__subscribers_amount = 0
        self.__store_managers_amount = 0
        self.__store_owners_amount = 0
        self.__system_managers_amount = 0
        self.__DB_handler = DataAccessFacade()

    def date (self):
        return self.__date

    def guests_amount (self):
        return self.__guests_amount

    def subscribers_amount (self):
        return self.__subscribers_amount

    def store_managers_amount (self):
        return self.__store_managers_amount

    def store_owners_amount (self):
        return self.__store_owners_amount

    def system_managers_amount (self):
        return self.__system_managers_amount


    def inc_guests_counter(self):
        if self.correct_date('guest'):
            self.__guests_amount += 1

    def inc_subscribers_counter(self):
        self.__subscribers_amount += 1

    def inc_store_managers_counter(self):
        self.__store_managers_amount += 1

    def inc_store_owners_counter(self):
        self.__store_owners_amount += 1

    def inc_store_managers_counter(self):
        self.__store_managers_amount += 1

    def inc_system_managers_counter(self):
        self.__system_managers_amount += 1

    def save_date_statistics_on_DB(self):
        return self.__DB_handler.write_statistic(self.__date, self.__guests_amount, self.__subscribers_amount,
                                                  self.__store_managers_amount, self.__store_owners_amount,
                                                  self.__system_managers_amount)

    def correct_date(self, counter_kind):
        print(f"check the dates: self={self.__date.date()}, today={datetime.datetime.today()}")
        if (self.__date.date() == datetime.datetime.today()):
            return True
        if self.save_date_statistics_on_DB():
            self.reset_daily_statistics(counter_kind)
        else:
            print("error in saving statistics to DB")
        return False

    def reset_daily_statistics(self, counter_kind):
        self.__date = datetime.datetime.today()
        self.__guests_amount = 0
        self.__subscribers_amount = 0
        self.__store_managers_amount = 0
        self.__store_owners_amount = 0
        self.__system_managers_amount = 0
        if counter_kind == 'guest':
            self.inc_guests_counter()
        elif counter_kind == 'subscriber':
            self.inc_subscribers_counter()
        elif counter_kind == 'store_manager':
            self.inc_store_managers_counter()
        elif counter_kind == 'store_owner':
            self.__store_owners_amount()
        elif counter_kind == 'system_manager':
            self.inc_system_managers_counter()

