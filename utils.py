from datetime import datetime

def validate_amount(amount):
    try:
        return float(amount)
    except ValueError:
        print("Invalid amount!")
        return None


def get_today_date():
    return datetime.now().strftime("%Y-%m-%d")