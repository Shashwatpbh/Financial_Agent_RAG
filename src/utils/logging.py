import logging
import structlog
from config.settings import get_settings

settings = get_settings()

def get_logger(name : str) -> structlog.BoundLogger:
    level = getattr(logging,settings.obs_log_level.upper(),logging.INFO)

    if not structlog.is_configured():
        shared_processors = [
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),


        ]
        if settings.obs_log_format == "json":
            processors = shared_processors + [
                structlog.processors.dict_tracebacks,
                structlog.processors.JSONRenderer(),
            ]
        else:
            processors = shared_processors + [
                structlog.dev.ConsoleRenderer(color=True)
            ]

        structlog.configure(
            processors=processors,
            wrapper_class=structlog.make_filtering_bound_logger(level),
            context_class=dict,
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )

        logging.basicConfig(
            format="%(message)s"
            level=level,
        )
    return sturctlog.get_logger(name)