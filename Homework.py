import calendar

# Create a calendar object instance
cal = calendar.Calendar()


for month_num in range(1, 13):
    
    weeks = cal.monthdatescalendar(2026, month_num)
    
   
    sample_date = weeks[2][0]
    
    
    print(f"\n{sample_date.strftime("%B")}")
