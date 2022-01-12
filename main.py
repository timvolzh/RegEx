import re
import csv


# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


# Форматируем ячейки
for row in contacts_list[1:]:
  # Разделение ФИО
  i = 0
  splited_lastname = row[0].split()
  for word in splited_lastname:
    row[i] = word
    i += 1

  # Разделение ИО
  i = 1
  splited_firsttname = row[1].split()
  for word in splited_firsttname:
    row[i] = word
    i += 1

  # Форматирование тел. номера
  phone_pattern = r"(\+7|8).*(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})"
  additional_phone_pattern = r"\(*(\w{3}\.).*(\d{4})\)*"
  res = re.sub(phone_pattern, r"+7(\2)\3-\4-\5", row[5])
  res = re.sub(additional_phone_pattern, r"\1\2", res)
  row[5] = res

 # Удаляем задвоения
for row in contacts_list:
  for row2 in contacts_list:
    if row[0] == row2[0] and row[1] == row2[1] and row is not row2:
      if row[2] == '': row[2] = row2[2]
      if row[3] == '': row[3] = row2[3]
      if row[4] == '': row[4] = row2[4]
      if row[5] == '': row[5] = row2[5]
      if row[6] == '': row[6] = row2[6]
      contacts_list.pop(contacts_list.index(row2))
      break

# Запись файла
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)