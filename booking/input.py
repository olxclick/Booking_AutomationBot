from datetime import datetime, timedelta

def add_days_to_current_date(days_to_add):
    new_date = datetime.now() + timedelta(days=days_to_add)
    return new_date.strftime("%Y-%m-%d")  # Formats as 'YYYY-MM-DD'
