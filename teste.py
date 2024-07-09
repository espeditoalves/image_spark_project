import pytz
from datetime import datetime

def main():
    utc_now = datetime.utcnow()
    utc_now = utc_now.replace(tzinfo=pytz.utc)

    local_timezone = pytz.timezone('America/New_York')
    local_time = utc_now.astimezone(local_timezone)

    print("Hora local em Nova York:", local_time.strftime('%Y-%m-%d %H:%M:%S %Z'))

if __name__ == "__main__":
    main()

