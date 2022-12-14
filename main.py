# from datetime import datetime 
#
#
# class Developer:
#     def __init__(self, name, dob, employment_date, unit, profile, salary, work_day):
#         self.name = name
#         self.dob = self.transform_date(dob)
#         self.employment_date = self.transform_date(employment_date)
#         self.unit = unit
#         self.profile = profile
#         self.salary = salary
#         self.work_day = work_day
#
#     def transform_date(self, date_as_string: str) -> datetime:
#         date_as_object = datetime.strptime(date_as_string, "%d.%m.%Y")
#         return date_as_object
#
#     def check_work_experience(self):
#         today = datetime.today()
#         experience = today - self.employment_date
#         return experience
#
#     def increase_salary(self, amount, restrictions=True):
#         if amount == self.salary * 0.1 and restrictions:
#             print("You can increase salary more than 10%")
#             self.salary += amount
#             print(f"msg: new salary is {self.salary}")
#         else:
#             print(f"Not can increase salary")
#
#     def data_processing(self):
#         if self.check_work_experience() >= 24:
#             self.increase_salary(
#                 self.salary * 0.3,
#                 restrictions=False
#             )
#
#     def work_bonus(self, bonus=300):
#         if self.work_day > 8:
#             print(f"add bonus developer in size {bonus} dollars")
#             self.salary += bonus
#         else:
#             print("Sorry, developer not get bonus")
#
#
# class Junior(Developer):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#
# class Senior(Developer):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#
# junior = Junior(
#     name="Stan",
#     dob="11.05.1990",
#     employment_date="07.04.2021",
#     unit="B",
#     profile="Python",
#     salary=1000,
#     work_day=10
#
# )
#
#
# senior = Senior(
#     name="Billy",
#     dob="08.11.1989",
#     employment_date="05.02.2018",
#     unit="B",
#     profile="Python",
#     salary=4000,
#     work_day=10
#
# )


