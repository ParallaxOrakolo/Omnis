def exception(logger):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur

    @param logger: The logging object
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                # log the exception
                logger.exception(f"There was an exception in {func.__name__}")

                # re-raise the exception
                raise

        return wrapper

    return decorator
