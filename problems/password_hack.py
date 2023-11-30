
def hack_password(dayCount_list, year): 
   
    birthDate = (19, 10, 2000)
    for month in range(12): 
        daycount = dayCount_list[month] 
        for date in range(1, daycount+1):    
            if birthDate[0] == date and birthDate[1] == month+1 and birthDate[2] == year:
                return(date,month+1,year) 
          

dayCount_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
print(hack_password(dayCount_list, 2000))