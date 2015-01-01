import logging

__author__ = 'soon'


def safe_call(unsafe_function):
    """
    Decorator for making function safe

    :return: Function, which returns tuple of two elements:
             - (True, result)     - no error, result is returned
             - (False, exception) - error has occurred
    """
    def wrapper(*args, **kwargs):
        try:
            return True, unsafe_function(*args, **kwargs)
        except Exception, e:
            return False, e

    return wrapper


def log_if_failed(default=None):
    """
    Decorator for logging safe function if error has occurred
    :param default: Returned, if error has occurred
    :return: Function, which returns result if no error,
                                else default
    """
    def log_if_failed_with_default(safe_function):
        def wrapper(*args, **kwargs):
            succeed, result_or_error = safe_function(*args, **kwargs)
            result = default if not succeed else result_or_error
            if not succeed:
                logging.error(result_or_error)
            return result

        return wrapper

    return log_if_failed_with_default


def safe_call_and_log_if_failed(default=None):
    """
    Just combination of safe_call and log_if_failed
    :param default:
    :return:
    """
    def wrapper(unsafe_function):
        return log_if_failed(default)(safe_call(unsafe_function))

    return wrapper