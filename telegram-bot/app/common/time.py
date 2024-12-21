import datetime


def get_now() -> datetime.datetime:
    return datetime.datetime.now(tz=datetime.timezone.utc).replace(tzinfo=None)
