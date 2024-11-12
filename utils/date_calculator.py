from datetime import datetime, timedelta

def format_date(num_days_ahead)
    future_date = datetime.now() + timedelta(days=num_days_ahead)
    formatted_future_date = future_date.strftime("%A, %B %d, %Y")

    day = future_date.day
    if day in [1, 21, 31]:
        suffix = 'st'
    elif day in [2, 22]:
        suffix = 'nd'
    elif day in [3, 23]:
        suffix = 'rd'
    else:
        suffix = 'th'

    formatted_future_date = formatted_future_date.replace(f'{day}', f'{day}{suffix}')
    return formatted_future_date

