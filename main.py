age = int(input("How old are you?\n"))
days_in_year = 365
weeks_in_year = 52
months_in_year = 12
#number of years that is supposed to be lived
years_90 = 90
#calculating number of years left
years_left = years_90 - age
#calculating the number of days you haved lived at your present age
days_lived = age * days_in_year
#calculating the number of days supposed to be lived
days_90 = years_90 * days_in_year
#calculating the number of days left
days_left = days_90 - days_lived
#calculating number of weeks lived
weeks_lived = age * weeks_in_year
#calculating wweks supposed to live
weeks_90 = years_90 * weeks_in_year
#calculating weeks left
weeks_left = weeks_90 - weeks_lived
#calculating months lived
months_lived = age * months_in_year
#calculating months supposed to live
months_90 = years_90 * months_in_year
# calculating months left 
months_left = months_90 - months_lived

print(f"you have {years_left} years  left, {months_left} months left, {weeks_left} weeks left and {days_left} days left to live ")
 