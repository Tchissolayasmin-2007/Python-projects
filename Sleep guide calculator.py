def sleep_guide():
  age= int(input("Enter your age: "))

  if age < 0:
    print("please enter a valid age.")
  elif age <= 0.25: # 0-3 months
       hours = "14-17 hours"
       group = "Newborn"
  elif age < 1:
    hours = "12-15 hours"
    group = "Infant"
  elif age <= 2:
    hours = "10-13 hours"
    group = "Toddler"
  elif age <=5:
    hours = "8-10 hours"
    group = "Child"
  elif age <= 13:
    hours = "9-11 hours"
    group = "Pre-Teen"
  elif age <=17:
    hours = "8-10 hours"
    group = "Teen"
  elif age <= 25:
    hours = "7-9 hours"
    group = "Young Adult"
  elif age <= 65:
    hours = "7-9 hours"
    group = "Adult"
  else:
    hours = "7-8 hours"
    group = "Senior"
  
  print(f"\nAge Group: {group}")
  print(f"Recommended Sleep: {hours} per day")

sleep_guide()
