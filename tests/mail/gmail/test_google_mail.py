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
