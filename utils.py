from datetime import datetime

def format_time(epoch_time):
    """
    Converts epoch time to a readable time string (HH:MM AM/PM).
    """
    return datetime.fromtimestamp(epoch_time).strftime("%I:%M %p")

def format_date(date_str):
    """
    Converts YYYY-MM-DD string to a readable date format (e.g., Mon, 01 Jan).
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%a, %d %b")

def get_weather_icon_url(icon_path):
    """
    Ensures the icon URL is complete (adds https: if missing).
    """
    if icon_path.startswith("//"):
        return f"https:{icon_path}"
    return icon_path
