import pytz
from datetime import datetime

def datetime_to_epoch_ms(dt):
    epoch = datetime.utcfromtimestamp(0)
    utc_dt = dt.astimezone(pytz.utc)
    utc_dt = utc_dt.replace(tzinfo=None)
    return int((utc_dt - epoch).total_seconds() * 1000.0)

def validator_datetime_utc(dt: datetime):
    if not isinstance(dt, datetime):
        return dt
    if dt.tzinfo is None:
        return dt.replace(tzinfo=pytz.utc)
    utc_dt = dt.astimezone(pytz.utc)
    return utc_dt

def format_utc_str(dt: datetime):
    dt = validator_datetime_utc(dt)
    return dt.isoformat()