Project Lama Reporter
=====================

##Intro:

This bot forwards messages from e-mail to VK dialog.

##How to run:

Firstly, you should place file `settings.py` to the project root with the following defiles:

 + `VK_LOGIN` - Your VK bot login
 + `VK_PASSWORD` - Your VK bot password
 + `VK_APP_ID` - Your VK application id
 + `VK_CHAT_ID` - Your VK chat id
 + `GMAIL_CLIENT_SECRET_JSON` - Path to file with GMail secret json. See below section with explanations
 + `GMAIL_STORAGE` - Path to file with GMail storage information
 + `LOG_FILENAME` - Path to file with logs
 
###GMAIL_CLIENT_SECRET_JSON

To get started using Gmail API, you need to first [create or select a project in the Google Developers Console 
and enable the API][1]. Using this link guides you through the process and activates the Gmail API automatically.

Alternatively, you can activate the Gmail API yourself in the Developers Console by doing the following:

 1. Go to the [Google Developers Console][2].
 1. Select a project, or create a new one.
 1. In the sidebar on the left, expand **APIs & auth**. Next, click **APIs**. In the list of APIs, 
    make sure the status is **ON** for the Gmail API.
 1. In the sidebar on the left, select **Credentials**.
 
In either case, you end up on the **Credentials** page and can create your project's credentials from here.

If you haven't done so already, create your OAuth 2.0 credentials by clicking **Create new Client ID** 
under the **OAuth** heading. Next, look for your application's client ID and client secret in the relevant table. 
You may also create and edit redirect URIs from this page.

Click **Download JSON** to save the client secrets file, then place this file at a location where your app can easily access it.


 _via [Google API Documentation][3]_


 [1]: https://console.developers.google.com//start/api?id=gmail&credential=client_key
 [2]: https://console.developers.google.com/
 [3]: https://developers.google.com/gmail/api/quickstart/quickstart-python
 
##Python version 

Python 2.7 is required. Python 3.x is not supported

##Third Party Libraries and Dependencies

In order to run bot you should install the following libraries

 + [vk][vk_library]
 + [google-api-python-client][google_api_library]
 + [beautifulsoup4][bs4_library]
 + [requests][requests_library]
 
 
[vk_library]: https://pypi.python.org/pypi/vk/1.5
[google_api_library]: https://developers.google.com/api-client-library/python/
[bs4_library]: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
[requests_library]: http://docs.python-requests.org/en/latest/

