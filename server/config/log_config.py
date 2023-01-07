# The uvicorn_logger is used to add timestamps

uvicorn_logger = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(levelprefix)s %(asctime)s :: %(client_addr)s - "%(request_line)s" %(status_code)s',
            "use_colors": True
        },
    },
    "handlers": {
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "formatter": "access",
            "class": "logging.FileHandler",
            "filename": "/var/log/fast-test.log"
        }
    },
    "loggers": {
        "uvicorn.access": {
            "handlers": ["access", "file"],
            # "level": "INFO",
            "propagate": False
        },
    },
}
