# Create a collection of dates (date like ‘1/11/2018’ with weekday like ‘Monday’),
# print total number of date, dates for non-working days (Saturday, Sunday)
# Создайте коллекцию дат (например, дату «1/11/2018» с днем недели, например «понедельник»),
# распечатайте общее количество дат, даты для нерабочих дней (суббота, воскресенье)
week_days = {"1/11/2018": "Monday", "08/11/2020": "Sunday", "07/11/2020": "Saturday", "5/11/2020": "Thursday",
             "01/11/2020": "Sunday", "14/11/2020": "Saturday"}
print(len(week_days))
count = 0
weekend = []
for i in week_days.items():
    if "Sunday" in i or "Saturday" in i:
        count += 1
        weekend.append(i)
print(weekend)
print(count)