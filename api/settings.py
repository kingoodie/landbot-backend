from secrets import token_urlsafe

from starlette.config import Config

# Config will be read from environment variables and/or ".env" files.
from starlette.datastructures import Secret

config = Config(".env")

DEBUG = config("DEBUG", cast=bool, default=False)
TESTING = config("TESTING", cast=bool, default=False)
HTTPS_ONLY = config("HTTPS_ONLY", cast=bool, default=False)
GZIP_COMPRESSION = config("GZIP", cast=bool, default=False)
SECRET = config("SECRET", cast=Secret, default=token_urlsafe(10))

DB_URL = config("DB_URL", cast=str, default="sqlite://:memory:")
GENERATE_SCHEMAS = config("GENERATE_SCHEMAS", cast=bool, default=True)

SSL_PORT = config("SSL_PORT", cast=int, default=465)
SMTP_PASSWORD = config("SMTP_PASSWORD", cast=Secret, default="bad")
SENDER_EMAIL = config("SENDER_EMAIL", cast=str, default="badmail@bad.com")
SLEEP_TIME_IN_SECONDS_BEFORE_SEND_EMAIL = config(
    "SLEEP_TIME_IN_SECONDS_BEFORE_SEND_EMAIL", cast=int, default=60
)

# The Sentry DSN is a unique identifier for our app when connecting to Sentry
# See https://docs.sentry.io/platforms/python/#connecting-the-sdk-to-sentry
SENTRY_DSN = config("SENTRY_DSN", cast=str, default="")
RELEASE_VERSION = config("RELEASE_VERSION", cast=str, default="<local dev>")

if SENTRY_DSN:  # pragma: nocover
    import sentry_sdk

    sentry_sdk.init(dsn=SENTRY_DSN, release=RELEASE_VERSION)
