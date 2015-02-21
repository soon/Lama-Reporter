from threading import Lock
import vk
from utils import safe_call_and_log_if_failed

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

__all__ = ['ThreadSafeVkApi']


class ThreadSafeVkApi(object):
    def __init__(self, **kwargs):
        """
        You should provide either app_id/login/password or access_token as named parameters
        """
        self.app_id = None
        self.login = None
        self.password = None
        self.access_token = None
        self.lock = Lock()
        self._vkapi = None

        self.init_credentials(**kwargs)

    def init_credentials(self, **kwargs):
        """
        Initializes vk api using given credentials.
        You should provide either app_id/login/password or access_token as named parameters
        """
        if all(x in kwargs for x in ('app_id', 'login', 'password')):
            self.app_id, self.login, self.password = kwargs['app_id'], kwargs['login'], kwargs['password']
        elif 'access_token' in kwargs:
            self.access_token = kwargs['access_token']
        else:
            raise ValueError('Expected either app_id/login/password or access_token parameter')

    def initialize_vkapi(self):
        """
        Initializes internal vk api using stored credentials.
        :raises ValueError: When api_id/login/password or access_token has not been defined
                            via __init__ or init_credentials
        """
        if self.app_id and self.login and self.password:
            self._vkapi = vk.API(self.app_id, self.login, self.password)
        elif self.access_token:
            self._vkapi = vk.API(access_token=self.access_token)
        else:
            raise ValueError('Either login/password or access_token are not initialized')

    @safe_call_and_log_if_failed
    def execute_vkapi_method_thread_safe(self, method, **kwargs):
        """
        Executes given method with given named parameters
        This method does not throw an exception if there was an error while executing method
        All implemented method uses this version, instead of unsafe one (unsafe_execute_vkapi_method_thread_safe)

        :param method: A method to be executed
        :param kwargs: Method parameters
        :return: Response from executed method
        """
        return self.unsafe_execute_vkapi_method_thread_safe(method, **kwargs)

    def unsafe_execute_vkapi_method_thread_safe(self, method, **kwargs):
        """
        Executes given method with given named parameters
        This method throws exception if there was an error while executing method
        All implemented methods uses safe version (execute_vkapi_method_thread_safe)

        :param method: A method to be executed
        :param kwargs: Method parameters
        :return: Response from executed method
        """
        self.lock.acquire()
        try:
            self.initialize_vkapi()
            return self._vkapi(method, **kwargs)
        finally:
            self.lock.release()

    def execute_messages_method_thread_safe(self, method, **kwargs):
        """
        Executes given method with prefix 'messages.'
        """
        return self.execute_vkapi_method_thread_safe('messages.' + method, **kwargs)

    def messages_get(self, **kwargs):
        """
        Executes method messages.get with given parameters
        """
        return self.execute_messages_method_thread_safe('get', **kwargs)

    def messages_send(self, **kwargs):
        """
        Executes method messages.send with given parameters
        """
        return self.execute_messages_method_thread_safe('send', **kwargs)

    def messages_mark_as_read(self, **kwargs):
        """
        Executes method messages.markAsRead with given parameters
        """
        return self.execute_messages_method_thread_safe('markAsRead', **kwargs)

    def messages_get_long_poll_server(self, **kwargs):
        """
        Executes method messages.getLongPollServer with given parameters
        """
        return self.execute_messages_method_thread_safe('getLongPollServer', **kwargs)

    def messages_set_activity(self, **kwargs):
        """
        Executes method messages.setActivity with given parameters
        """
        return self.execute_messages_method_thread_safe('setActivity', **kwargs)

    def execute_photos_method_thread_safe(self, method, **kwargs):
        """
        Executes given methods with prefix 'photos.'
        """
        return self.execute_vkapi_method_thread_safe('photos.' + method, **kwargs)

    def photos_save_message_photo(self, **kwargs):
        """
        Executes method photos.saveMessagePhoto with given parameters
        """
        return self.execute_photos_method_thread_safe('saveMessagesPhoto', **kwargs)

    def photos_get_messages_upload_server(self, **kwargs):
        """
        Executes method photos.getMessagesUploadServer with given parameters
        """
        return self.execute_photos_method_thread_safe('getMessagesUploadServer', **kwargs)

    def execute_docs_method_thread_safe(self, method, **kwargs):
        """
        Executes given method with prefix 'docs.'
        """
        return self.execute_vkapi_method_thread_safe('docs.' + method, **kwargs)

    def docs_save(self, **kwargs):
        """
        Executes method docs.save with given parameters
        """
        return self.execute_docs_method_thread_safe('save', **kwargs)

    def docs_get_upload_server(self, **kwargs):
        """
        Executes method docs.getUploadServer with given parameters
        """
        return self.execute_docs_method_thread_safe('getUploadServer', **kwargs)

    def execute_users_method_thread_safe(self, method, **kwargs):
        """
        Executes given method with prefix 'users.'
        """
        return self.execute_vkapi_method_thread_safe('users.' + method, **kwargs)

    def users_get(self, **kwargs):
        """
        Executes method users.get with given parameters
        """
        return self.execute_users_method_thread_safe('get', **kwargs)