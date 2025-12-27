import datetime as dt
import math

global REF_NEW_MOON; global REF_LAST_QUARTER; global REF_FIRST_QUARTER; global REF_FULL; global SYNODIC_MONTH
SYNODIC_MONTH = 29.530588853
REF_NEW_MOON = dt.datetime(2025, 12, 20, 1, 43)
REF_FIRST_QUARTER = dt.datetime(2025, 11, 28, 6, 58)
REF_FULL = dt.datetime(2025, 12, 4, 23, 14)
REF_LAST_QUARTER = dt.datetime(2025, 12, 11, 20, 51)

def next_new_moon(after):
    if isinstance(after, dt.date) and not isinstance(after, dt.datetime):
        after = dt.datetime.combine(after, dt.time.min)
    delta_days = (after - REF_NEW_MOON).total_seconds() / 86400
    n = math.ceil(delta_days / SYNODIC_MONTH)
    return REF_NEW_MOON + dt.timedelta(days=n * SYNODIC_MONTH)

def next_last_quarter_moon(after):
    if isinstance(after, dt.date) and not isinstance(after, dt.datetime):
        after = dt.datetime.combine(after, dt.time.min)
    delta_days = (after - REF_LAST_QUARTER).total_seconds() / 86400
    n = math.ceil(delta_days / SYNODIC_MONTH)
    return REF_LAST_QUARTER + dt.timedelta(days=n * SYNODIC_MONTH)

def next_first_quarter_moon(after):
    if isinstance(after, dt.date) and not isinstance(after, dt.datetime):
        after = dt.datetime.combine(after, dt.time.min)
    delta_days = (after - REF_FIRST_QUARTER).total_seconds() / 86400
    n = math.ceil(delta_days / SYNODIC_MONTH)
    return REF_FIRST_QUARTER + dt.timedelta(days=n * SYNODIC_MONTH)

def next_full_moon(after):
    if isinstance(after, dt.date) and not isinstance(after, dt.datetime):
        after = dt.datetime.combine(after, dt.time.min)
    delta_days = (after - REF_FULL).total_seconds() / 86400
    n = math.ceil(delta_days / SYNODIC_MONTH)
    return REF_FULL + dt.timedelta(days=n * SYNODIC_MONTH)

def localtime(date):
    if hasattr(date, 'datetime'):
        date = date.datetime()
    if date.tzinfo is None:
        date = date.replace(tzinfo=dt.timezone.utc)
    local_dt = date.astimezone()
    return local_dt.replace(tzinfo=None)