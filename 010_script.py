hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

minutes = mins+dura
min_final = minutes

if(minutes >= 60):
    min_final = minutes%60
    hour = ((hour*60) + minutes)/60

# Ajuste hour
if(hour < 10):
    hour = '0'+str(int(hour))
elif (hour >= 24):
    hour %= 24
    hour = str(int(hour))
else:
    hour = str(int(hour))
 
# Ajuste minutes   
if(min_final < 10):
    min_final = '0'+str(min_final)
else:
    min_final = str(min_final)
    
# Print result
print('End time: '+hour+':'+min_final)