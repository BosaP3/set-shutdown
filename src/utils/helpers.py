from datetime import datetime

# Function to schedule a shutdown in seconds
def get_seconds_until(target_datetime: datetime) -> int:
    now = datetime.now()
    delta = target_datetime - now
    return max(0, int(delta.total_seconds()))

def is_valid_datetime_string(date_str: str, time_str: str) -> bool:
    try:
        datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M")
        return True
    except ValueError:
        return False

def parse_datetime_from_input(date_str: str, time_str: str) -> datetime:
    return datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M")