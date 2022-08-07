from datetime import datetime 

def add_variable_to_context(request):
    current_datetime = datetime.now()  

    current_time = datetime.now().strftime('%H:%M')   
     
    return{
        'time': current_time,
        'date': current_datetime
    }