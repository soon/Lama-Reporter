from utils import safe_call, log_if_failed, safe_call_and_log_if_failed
from unittest import TestCase
from testfixtures import LogCapture


__author__ = 'soon'


class TestSafeCall(TestCase):
    def unsafe_function_without_exception(self, a, b, **kwargs):
        return a + b + sum(kwargs.itervalues())

    def unsafe_function_with_exception(self, a, b, **kwargs):
        raise ValueError('Such exception!')

    @safe_call
    def safe_function_without_exception(self, a, b, **kwargs):
        return self.unsafe_function_without_exception(a, b, **kwargs)

    @safe_call
    def safe_function_with_exception(self, a, b, **kwargs):
        return self.unsafe_function_with_exception(a, b, **kwargs)

    @log_if_failed(default=42)
    def safe_function_without_exception_with_logging(self, a, b, **kwargs):
        return self.safe_function_without_exception(a, b, **kwargs)

    @log_if_failed(default=42)
    def safe_function_with_exception_with_logging(self, a, b, **kwargs):
        return self.safe_function_with_exception(a, b, **kwargs)

    @safe_call_and_log_if_failed(default=42)
    def safe_function_without_exception_with_logging_dual_decorator(self, a, b, **kwargs):
        return self.unsafe_function_without_exception(a, b, **kwargs)

    @safe_call_and_log_if_failed(default=42)
    def safe_function_with_exception_with_logging_dual_decorator(self, a, b, **kwargs):
        return self.unsafe_function_with_exception(a, b, **kwargs)

    def test_safe_call_without_exception(self):
        succeed, result = self.safe_function_without_exception(1, 2, c=3)
        self.assertTrue(succeed)
        self.assertEqual(result, 6)

    def test_safe_call_with_exception(self):
        succeed, exception = self.safe_function_with_exception(1, 2, c=3)
        self.assertFalse(succeed)
        self.assertIsInstance(exception, Exception)

    def test_safe_call_with_exception_with_logging(self):
        with LogCapture() as l:
            result = self.safe_function_without_exception_with_logging(1, 2, c=3)
            self.assertEqual(result, 6)
            l.check()

    def test_safe_call_without_exception_with_logging(self):
        with LogCapture() as l:
            result = self.safe_function_with_exception_with_logging(1, 2, c=3)
            self.assertEqual(result, 42)
            l.check(('root', 'ERROR', 'Such exception!'))

    def test_safe_call_with_exception_with_logging_dual_decorator(self):
        with LogCapture() as l:
            result = self.safe_function_without_exception_with_logging_dual_decorator(1, 2, c=3)
            self.assertEqual(result, 6)
            l.check()

    def test_safe_call_without_exception_with_logging_dual_decorator(self):
        with LogCapture() as l:
            result = self.safe_function_with_exception_with_logging_dual_decorator(1, 2, c=3)
            self.assertEqual(result, 42)
            l.check(('root', 'ERROR', 'Such exception!'))