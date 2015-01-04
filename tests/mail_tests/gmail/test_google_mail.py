# coding=utf-8
from unittest import TestCase
from mail import GoogleMail

__author__ = 'soon'


class TestGoogleMail(TestCase):
    def test_multi_part_mail_1(self):
        response = {
            "id": "14a97232cd15490c",
            "threadId": "14a97232cd15490c",
            "labelIds": [
                "INBOX",
                "IMPORTANT",
                "CATEGORY_PERSONAL"
            ],
            "snippet": "Добрый вечер! Высылаю результаты. Завтра в 19.00 отошлю ведомости, поэтому кому что не понятно -",
            "historyId": "8530",
            "payload": {
                "mimeType": "multipart/mixed",
                "filename": "",
                "headers": [
                    {
                        "name": "Delivered-To",
                        "value": "project.lama.reporter@gmail.com"
                    },
                    {
                        "name": "Received",
                        "value": "by 10.76.58.75 with SMTP id o11csp1793827oaq;        Mon, 29 Dec 2014 09:41:13 -0800 (PST)"
                    },
                    {
                        "name": "X-Received",
                        "value": "by 10.152.6.132 with SMTP id b4mr39033133laa.59.1419874872799;        Mon, 29 Dec 2014 09:41:12 -0800 (PST)"
                    },
                    {
                        "name": "Return-Path",
                        "value": "<uliadubrov@mail.ru>"
                    },
                    {
                        "name": "Received",
                        "value": "from f392.i.mail.ru (f392.i.mail.ru. [185.5.136.63])        by mx.google.com with ESMTPS id x12si19352431lbm.44.2014.12.29.09.41.12        for <project.lama.reporter@gmail.com>        (version=TLSv1.2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);        Mon, 29 Dec 2014 09:41:12 -0800 (PST)"
                    },
                    {
                        "name": "Received-SPF",
                        "value": "pass (google.com: domain of uliadubrov@mail.ru designates 185.5.136.63 as permitted sender) client-ip=185.5.136.63;"
                    },
                    {
                        "name": "Authentication-Results",
                        "value": "mx.google.com;       spf=pass (google.com: domain of uliadubrov@mail.ru designates 185.5.136.63 as permitted sender) smtp.mail=uliadubrov@mail.ru;       dkim=pass header.i=@mail.ru;       dmarc=pass (p=NONE dis=NONE) header.from=mail.ru"
                    },
                    {
                        "name": "DKIM-Signature",
                        "value": "v=1; a=rsa-sha256; q=dns/txt; c=relaxed/relaxed; d=mail.ru; s=mail2; h=Content-Type:Message-ID:Reply-To:Date:MIME-Version:Subject:To:From; bh=hqEF/DUBvJSMIRZQ9iXgEwu3O1wXlV3HHKXoe7KrhWE=; b=ReQmmR21iV/s3N7vl25767IYgpusIZqiw8gJ/P456M52pSlHIQt9Wc+V75s+gF5GAPVzqYcNSgfnHh6/H6Wh+ytU9l/EKvQgdQ6j1qNyCSjjYglxDeIplCAHAzj1RsAHG/GnKPOis1R/17ipKAxyf3Pn7Z5kxSxtrxZnYnsG7xY=;"
                    },
                    {
                        "name": "Received",
                        "value": "from [46.147.7.38] (ident=mail) by f392.i.mail.ru with local (envelope-from <uliadubrov@mail.ru>) id 1Y5eJb-0006gd-ES for project.lama.reporter@gmail.com; Mon, 29 Dec 2014 20:41:11 +0300"
                    },
                    {
                        "name": "X-ResentFrom",
                        "value": "<pi131@inbox.ru>"
                    },
                    {
                        "name": "X-MailRu-Forward",
                        "value": "1"
                    },
                    {
                        "name": "DKIM-Signature",
                        "value": "v=1; a=rsa-sha256; q=dns/txt; c=relaxed/relaxed; d=mail.ru; s=mail2; h=Content-Type:Message-ID:Reply-To:Date:MIME-Version:Subject:To:From; bh=47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; b=DTRgPshx2L8ZyoORLMnoCJ3S/zqoSNcXdntuYWbmPQU9d0iwlfgEIpqO28OxXSILRFhaG7dMzurJFtaJxJW5bp1z+TCmoAhCj5gzml1RH6tZ3uFizoRPjN6WpE76b3fYZdJ/5z0M/QQZ3ppjzY+ys9Bhc+p4N65W8zIbTCGeXRI=;"
                    },
                    {
                        "name": "Received",
                        "value": "from [46.147.7.38] (ident=mail) by f392.i.mail.ru with local (envelope-from <uliadubrov@mail.ru>) id 1Y5eJa-0006gP-P4 for pi131@inbox.ru; Mon, 29 Dec 2014 20:41:11 +0300"
                    },
                    {
                        "name": "Received",
                        "value": "from [46.147.7.38] by e.mail.ru with HTTP; Mon, 29 Dec 2014 20:41:10 +0300"
                    },
                    {
                        "name": "From",
                        "value": "\"Юлия Дубровская\" <uliadubrov@mail.ru>"
                    },
                    {
                        "name": "To",
                        "value": "pi131 <pi131@inbox.ru>"
                    },
                    {
                        "name": "Subject",
                        "value": "результаты"
                    },
                    {
                        "name": "MIME-Version",
                        "value": "1.0"
                    },
                    {
                        "name": "X-Mailer",
                        "value": "Mail.Ru Mailer 1.0"
                    },
                    {
                        "name": "X-Originating-IP",
                        "value": "[46.147.7.38]"
                    },
                    {
                        "name": "Date",
                        "value": "Mon, 29 Dec 2014 20:41:10 +0300"
                    },
                    {
                        "name": "Reply-To",
                        "value": "\"Юлия Дубровская\" <uliadubrov@mail.ru>"
                    },
                    {
                        "name": "X-Priority",
                        "value": "3 (Normal)"
                    },
                    {
                        "name": "Message-ID",
                        "value": "<1419874870.184996686@f392.i.mail.ru>"
                    },
                    {
                        "name": "Content-Type",
                        "value": "multipart/mixed; boundary=\"----gO4sYtsr6urfWBt16UCy7dnEEp46tebl-TuLf5PzlAEEhRGpP:1419874870\""
                    },
                    {
                        "name": "X-Mras",
                        "value": "Ok"
                    },
                    {
                        "name": "X-Spam",
                        "value": "undefined"
                    },
                    {
                        "name": "X-Mras",
                        "value": "Ok"
                    }
                ],
                "body": {
                    "size": 0
                },
                "parts": [
                    {
                        "mimeType": "multipart/alternative",
                        "filename": "",
                        "headers": [
                            {
                                "name": "Content-Type",
                                "value": "multipart/alternative; boundary=\"--ALT--gO4sYtsr6urfWBt16UCy7dnEEp46tebl1419874870\""
                            }
                        ],
                        "body": {
                            "size": 0
                        },
                        "parts": [
                            {
                                "partId": "0.0",
                                "mimeType": "text/plain",
                                "filename": "",
                                "headers": [
                                    {
                                        "name": "Content-Type",
                                        "value": "text/plain; charset=utf-8"
                                    },
                                    {
                                        "name": "Content-Transfer-Encoding",
                                        "value": "base64"
                                    }
                                ],
                                "body": {
                                    "size": 624,
                                    "data": "INCU0L7QsdGA0YvQuSDQstC10YfQtdGAIQrQktGL0YHRi9C70LDRjiDRgNC10LfRg9C70YzRgtCw0YLRiy4K0JfQsNCy0YLRgNCwINCyIDE5LjAwINC-0YLQvtGI0LvRjiDQstC10LTQvtC80L7RgdGC0LgsINC_0L7RjdGC0L7QvNGDINC60L7QvNGDINGH0YLQviDQvdC1INC_0L7QvdGP0YLQvdC-IC0g0L_QuNGI0LjRgtC1INC00L4g0Y3RgtC-0LPQviDQstGA0LXQvNC10L3QuCwg0L7RgtCy0LXRh9GDLgrQryDRgdGC0LDQstC40LvQsCDQv9GA0LjQvNC10YfQsNC90LjRjywg0LPQtNC1INGB0L3QuNC20LDQu9CwINC-0YbQtdC90LrRgy4KCgrQoSDRg9Cy0LDQttC10L3QuNC10LwsINCU0YPQsdGA0L7QstGB0LrQsNGPINCu0LvQuNGPINCS0LvQsNC00LjQvNC40YDQvtCy0L3QsCwK0Lou0Y0u0L0uLCDQtNC-0YbQtdC90YIg0LrQsNGELiAi0K3QutC-0L3QvtC80LjQutCwINC4INGE0LjQvdCw0L3RgdGLIgrQn9C10YDQvNGB0LrQvtCz0L4g0L3QsNGG0LjQvtC90LDQu9GM0L3QvtCz0L4g0LjRgdGB0LvQtdC00L7QstCw0YLQtdC70YzRgdC60L7Qs9C-IArQv9C-0LvQuNGC0LXRhdC90LjRh9C10YHQutC-0LPQviDRg9C90LjQstC10YDRgdC40YLQtdGC0LAKaHR0cDovL3d3dy5rYWZ1cHJmaW4ucnUv"
                                }
                            },
                            {
                                "partId": "0.1",
                                "mimeType": "text/html",
                                "filename": "",
                                "headers": [
                                    {
                                        "name": "Content-Type",
                                        "value": "text/html; charset=utf-8"
                                    },
                                    {
                                        "name": "Content-Transfer-Encoding",
                                        "value": "base64"
                                    }
                                ],
                                "body": {
                                    "size": 681,
                                    "data": "CjxIVE1MPjxCT0RZPtCU0L7QsdGA0YvQuSDQstC10YfQtdGAITxicj7QktGL0YHRi9C70LDRjiDRgNC10LfRg9C70YzRgtCw0YLRiy48YnI-0JfQsNCy0YLRgNCwINCyIDE5LjAwINC-0YLQvtGI0LvRjiDQstC10LTQvtC80L7RgdGC0LgsINC_0L7RjdGC0L7QvNGDINC60L7QvNGDINGH0YLQviDQvdC1INC_0L7QvdGP0YLQvdC-IC0g0L_QuNGI0LjRgtC1INC00L4g0Y3RgtC-0LPQviDQstGA0LXQvNC10L3QuCwg0L7RgtCy0LXRh9GDLjxicj7QryDRgdGC0LDQstC40LvQsCDQv9GA0LjQvNC10YfQsNC90LjRjywg0LPQtNC1INGB0L3QuNC20LDQu9CwINC-0YbQtdC90LrRgy48YnI-PGJyPjxicj7QoSDRg9Cy0LDQttC10L3QuNC10LwsINCU0YPQsdGA0L7QstGB0LrQsNGPINCu0LvQuNGPINCS0LvQsNC00LjQvNC40YDQvtCy0L3QsCw8YnI-0Lou0Y0u0L0uLCDQtNC-0YbQtdC90YIg0LrQsNGELiAi0K3QutC-0L3QvtC80LjQutCwINC4INGE0LjQvdCw0L3RgdGLIjxicj7Qn9C10YDQvNGB0LrQvtCz0L4g0L3QsNGG0LjQvtC90LDQu9GM0L3QvtCz0L4g0LjRgdGB0LvQtdC00L7QstCw0YLQtdC70YzRgdC60L7Qs9C-IDxicj7Qv9C-0LvQuNGC0LXRhdC90LjRh9C10YHQutC-0LPQviDRg9C90LjQstC10YDRgdC40YLQtdGC0LA8YnI-aHR0cDovL3d3dy5rYWZ1cHJmaW4ucnUvPC9CT0RZPjwvSFRNTD4K"
                                }
                            }
                        ]
                    },
                    {
                        "partId": "1",
                        "mimeType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        "filename": "ВШЭ_экз.xlsx",
                        "headers": [
                            {
                                "name": "Content-Type",
                                "value": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; name=\"ВШЭ_экз.xlsx\""
                            },
                            {
                                "name": "Content-Disposition",
                                "value": "attachment"
                            },
                            {
                                "name": "Content-Transfer-Encoding",
                                "value": "base64"
                            }
                        ],
                        "body": {
                            "attachmentId": "ANGjdJ9G3IaoOaQJSW_Oxjpde8XOpgOsILPujHiXvgdyAeX27BVbNfk87Al91eeKt1wI5ozmxFhIM_b8ZNPl9k6oc6h7BJ7vztpyj9NWaq8SC1VJjSNd0aemD-TRB610ApaHON97hdrE76ZGzkSrFTc2okdV0tD1MuFlG6PRqDbFN1KZ8P7m8WFyzJbQBX-s2u0PUmlzT_KnL7HF2dCK-junSY9V-4QgXV8tpXrmWOxRmCnbZTbKP8zkIuYJ96mQpM5AGQKn5-m4XAUcxXg3Ix8XUc2Js6_qf7kxCRm9Ww",
                            "size": 25080
                        }
                    }
                ]
            },
            "sizeEstimate": 30635
        }
        m = GoogleMail(response)

        self.assertEquals(m.id, '14a97232cd15490c')
        self.assertEquals(m.subject, 'результаты')
        self.assertEquals(m.body.split(), u'''Высылаю результаты.
Завтра в 19.00 отошлю ведомости, поэтому кому что не понятно - пишите до этого времени, отвечу.
Я ставила примечания, где снижала оценку.


С уважением, Дубровская Юлия Владимировна,
к.э.н., доцент каф. "Экономика и финансы"
Пермского национального исследовательского
политехнического университета
http://www.kafuprfin.ru/'''.split())
        self.assertEquals(m.sender, '"Юлия Дубровская" <uliadubrov@mail.ru>')

        self.assertEquals(len(m.attachments), 1)

        attachment = m.attachments[0]
        self.assertFalse(attachment.is_loaded)
        self.assertEquals(attachment.id,
                          'ANGjdJ9G3IaoOaQJSW_Oxjpde8XOpgOsILPujHiXvgdyAeX27BVbNfk87Al91eeKt1wI5ozmxFhIM_b8ZNPl9k6oc6h7BJ7vztpyj9NWaq8SC1VJjSNd0aemD-TRB610ApaHON97hdrE76ZGzkSrFTc2okdV0tD1MuFlG6PRqDbFN1KZ8P7m8WFyzJbQBX-s2u0PUmlzT_KnL7HF2dCK-junSY9V-4QgXV8tpXrmWOxRmCnbZTbKP8zkIuYJ96mQpM5AGQKn5-m4XAUcxXg3Ix8XUc2Js6_qf7kxCRm9Ww')
        self.assertEquals(attachment.message_id, m.id)
        self.assertIsNone(m.attachments[0].data)

    def test_message_without_attachments(self):
        response = {
            "id": "14a9272ffa2620f7",
            "threadId": "14a8fd83e212fe42",
            "labelIds": [
                "INBOX",
                "IMPORTANT",
                "CATEGORY_PERSONAL"
            ],
            "snippet": "Данил Губайдулин ALLO запретить присылать мне сообщения (block messages from this contact)",
            "historyId": "12341",
            "payload": {
                "mimeType": "multipart/alternative",
                "filename": "",
                "headers": [
                    {
                        "name": "Delivered-To",
                        "value": "project.lama.reporter@gmail.com"
                    },
                    {
                        "name": "Received",
                        "value": "by 10.76.58.75 with SMTP id o11csp1611948oaq;        Sun, 28 Dec 2014 11:50:18 -0800 (PST)"
                    },
                    {
                        "name": "X-Received",
                        "value": "by 10.68.68.227 with SMTP id z3mr83936421pbt.3.1419796217834;        Sun, 28 Dec 2014 11:50:17 -0800 (PST)"
                    },
                    {
                        "name": "Return-Path",
                        "value": "<ilumgpz-10e8ba14b@vkmessenger.com>"
                    },
                    {
                        "name": "Received",
                        "value": "from mail1.vkmessenger.com ([87.240.182.146])        by mx.google.com with ESMTP id oz4si15910695pbb.42.2014.12.28.11.50.17        for <project.lama.reporter@gmail.com>;        Sun, 28 Dec 2014 11:50:17 -0800 (PST)"
                    },
                    {
                        "name": "Received-SPF",
                        "value": "pass (google.com: domain of ilumgpz-10e8ba14b@vkmessenger.com designates 87.240.182.146 as permitted sender) client-ip=87.240.182.146;"
                    },
                    {
                        "name": "Authentication-Results",
                        "value": "mx.google.com;       spf=pass (google.com: domain of ilumgpz-10e8ba14b@vkmessenger.com designates 87.240.182.146 as permitted sender) smtp.mail=ilumgpz-10e8ba14b@vkmessenger.com"
                    },
                    {
                        "name": "Received",
                        "value": "from [127.0.0.1] (localhost [127.0.0.1]) by mail1.vkmessenger.com (Postfix) with ESMTPS id A7C362EEF4 for <project.lama.reporter@gmail.com>; Sun, 28 Dec 2014 22:50:13 +0300 (MSK)"
                    },
                    {
                        "name": "Message-Id",
                        "value": "<fea4a1bfb78bfaac@vk.com>"
                    },
                    {
                        "name": "In-Reply-To",
                        "value": "<eb37912062a146b8@vk.com>"
                    },
                    {
                        "name": "Date",
                        "value": "Sun, 28 Dec 2014 19:50:13 GMT"
                    },
                    {
                        "name": "From",
                        "value": "\"Данил Губайдулин Danil Gubaydulin\" <ilumgpz-10e8ba14b@vkmessenger.com>"
                    },
                    {
                        "name": "To",
                        "value": "project.lama.reporter@gmail.com"
                    },
                    {
                        "name": "Subject",
                        "value": "Беседа с Данилом Губайдулиным"
                    },
                    {
                        "name": "MIME-Version",
                        "value": "1.0"
                    },
                    {
                        "name": "Content-Type",
                        "value": "multipart/alternative;        boundary=----vkmessenger-0.99771416001021862"
                    }
                ],
                "body": {
                    "size": 0
                },
                "parts": [
                    {
                        "partId": "0",
                        "mimeType": "text/plain",
                        "filename": "",
                        "headers": [
                            {
                                "name": "Content-Type",
                                "value": "text/plain; charset=UTF-8"
                            },
                            {
                                "name": "Content-Transfer-Encoding",
                                "value": "quoted-printable"
                            }
                        ],
                        "body": {
                            "size": 140,
                            "data": "0JTQsNC90LjQuyDQk9GD0LHQsNC50LTRg9C70LjQvSBBTExPDQoNCtC30LDQv9GA0LXRgtC40YLRjCDQv9GA0LjRgdGL0LvQsNGC0Ywg0LzQvdC1INGB0L7QvtCx0YnQtdC90LjRjyAoYmxvY2sgbWVzc2FnZXMgZnJvbSB0aGlzIGNvbnRhY3QpDQo="
                        }
                    },
                    {
                        "partId": "1",
                        "mimeType": "text/html",
                        "filename": "",
                        "headers": [
                            {
                                "name": "Content-Type",
                                "value": "text/html; charset=UTF-8"
                            },
                            {
                                "name": "Content-Transfer-Encoding",
                                "value": "quoted-printable"
                            }
                        ],
                        "body": {
                            "size": 1171,
                            "data": "PCFET0NUWVBFIGh0bWwgUFVCTElDICItLy9XM0MvL0RURCBYSFRNTCAxLjAgU3RyaWN0Ly9FTiIgImh0dHA6Ly93d3cudzMub3JnL1RSL3hodG1sMS9EVEQveGh0bWwxLXN0cmljdC5kdGQiPg0KPGh0bWw-DQo8aGVhZD4NCiAgPG1ldGEgaHR0cC1lcXVpdj0iQ29udGVudC1UeXBlIiBjb250ZW50PSJ0ZXh0L2h0bWw7IGNoYXJzZXQ9dXRmLTgiPg0KICA8dGl0bGU-PC90aXRsZT4NCjwvaGVhZD4NCjxib2R5IHN0eWxlPSJtYXJnaW46MDsgcGFkZGluZzogMDsgZm9udC1mYW1pbHk6IHRhaG9tYSxhcmlhbDsgZm9udC1zaXplOiAxMXB4OyBmb250LXdlaWdodDogbm9ybWFsOyI-DQogIDx0YWJsZSB3aWR0aD0iMTAwJSI-PHRyPjx0ZCB3aWR0aD0iNTUiIHZhbGlnbj0idG9wIj48YSBocmVmPSJodHRwczovL3ZrLmNvbS9pbHVtZ3B6Ij48aW1nIHNyYz0iaHR0cHM6Ly9wcC52ay5tZS9jNjIyNDI4L3Y2MjI0MjgyNTEvZjUxOC9TbHFQWXJZR2N3QS5qcGciLz48L2E-PC90ZD48dGQgdmFsaWduPSJ0b3AiIHN0eWxlPSJmb250LXNpemU6IDEycHg7IGNvbG9yOiAjMDAwMDAwOyI-DQogICAgPGI-PGEgaHJlZj0iaHR0cHM6Ly92ay5jb20vaWx1bWdweiIgc3R5bGU9ImNvbG9yOiAjMkI1ODdBOyB0ZXh0LWRlY29yYXRpb246IG5vbmU7Ij7QlNCw0L3QuNC7INCT0YPQsdCw0LnQtNGD0LvQuNC9PC9hPjwvYj48YnIgLz4NCiAgICBBTExPPC90ZD48L3RyPjwvdGFibGU-DQogICAgPGEgc3R5bGU9ImNvbG9yOiAjNzc3Nzc3OyIgaHJlZj0iaHR0cDovL3ZrLmNvbS9tYWlsP2FjdD1lbWFpbF9tYXJrX3NwYW0maXRlbT0yYmVjYTYxY2E4JnVpZD00NTkyMzI1MSZoYXNoPTJhMGZmYTJhMDgyZmJiN2Q2ZSZ0aW1lPTE0MTk3OTYyMTMmY29ycmVzcG9uZD0yMjA1OWU0MmY5YzdlYjczYjImdG89Njc1YWM5ZTUxNDg2MjBhMjVjYjkxYTc3NGRhNTI1NmQiPtC30LDQv9GA0LXRgtC40YLRjCDQv9GA0LjRgdGL0LvQsNGC0Ywg0LzQvdC1INGB0L7QvtCx0YnQtdC90LjRjyAoYmxvY2sgbWVzc2FnZXMgZnJvbSB0aGlzIGNvbnRhY3QpPC9hPjxpbWcgc3JjPSJodHRwOi8vdmsuY29tL21haWw_YWN0PWVtYWlsX21hcmtfcmVhZCZpdGVtPTJiZWNhNjFjYTgmdWlkPTQ1OTIzMjUxJmhhc2g9OThhNGFkOTkzNTkyNWQ3NmY5JnRpbWU9MTQxOTc5NjIxMyIgLz4NCjwvYm9keT4NCjwvaHRtbD4NCg=="
                        }
                    }
                ]
            },
            "sizeEstimate": 3854
        }

        m = GoogleMail(response)

        self.assertEquals(m.id, '14a9272ffa2620f7')
        self.assertEquals(m.subject, 'Беседа с Данилом Губайдулиным')
        self.assertEquals(m.body.split(), u'''Данил Губайдулин ALLO запретить присылать мне сообщения (block messages from this contact)'''.split())
        self.assertEquals(m.sender, '\"Данил Губайдулин Danil Gubaydulin\" <ilumgpz-10e8ba14b@vkmessenger.com>')

        self.assertEquals(len(m.attachments), 0)
