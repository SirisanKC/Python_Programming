import os
import csv

def process_titanic_data(file_name):
    male_count = 0
    female_count = 0
    total_age = 0
    age_count = 0
    oldest_age = 0
    
    f = open(file_name, newline='', encoding='utf-8')
    reader = csv.DictReader(f)
    
    for row in reader:
        sex = row['Sex']
        age = row['Age']
        
        if sex == 'male':
            male_count += 1
        elif sex == 'female':
            female_count += 1
        
        if age != '' and age is not None:
            try:
                age = float(age)
                total_age += age
                age_count += 1
                
                if age > oldest_age:
                    oldest_age = age
            except ValueError:
                continue
    
    average_age = round(total_age / age_count) if age_count > 0 else 0
    
    print(f"The number of male passengers: {male_count}")
    print(f"The number of female passengers: {female_count}")
    print(f"The average age of passengers: {average_age}")
    print(f"The age of the oldest passenger: {int(oldest_age)}")
    
    f.close()

if not os.path.exists('titanic.csv'):
    print("File 'titanic.csv' not found!")
else:
    process_titanic_data('titanic.csv')