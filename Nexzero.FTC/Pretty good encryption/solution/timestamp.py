import pytz
from datetime import datetime

# you need first to get the pgp timestamp by importing it 
# PGP timestamp (Fri 03 Jan 2025 12:43:46 PM EST)
# the time is in EST time stamp so we need also to convert it to utc 
pgp_timestamp_str = "Fri 03 Jan 2025 12:43:46 PM EST"
pgp_format = "%a %d %b %Y %I:%M:%S %p %Z"

# Parse the timestamp into a datetime object using the given format
pgp_timestamp = datetime.strptime(pgp_timestamp_str, pgp_format)

# Convert the parsed datetime into UTC
pgp_timestamp_utc = pytz.timezone('US/Eastern').localize(pgp_timestamp).astimezone(pytz.utc)

# Get the Unix timestamp (seconds since the Unix epoch)
pgp_unix_timestamp = int(pgp_timestamp_utc.timestamp())

print("PGP Unix Timestamp:", pgp_unix_timestamp)
