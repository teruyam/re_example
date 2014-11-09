#!/usr/bin/env python

import re

text = ("Kushikawa Hatoko, 17, 2014/11/09, Hayami Saori, Over Element;"
        "Takanashi Sayumi, 18, 2014/11/09, Taneda Risa, Root of Origin")

pattern = ("("
           "(?P<last_name>\w+)" "\s"
           "(?P<first_name>\w+)" "\s*,\s*"
           "(?P<age>\d+)" "\s*,\s*"
           "(?P<date>\d+/\d+/\d+)" "\s*,\s*"
           "(?P<voice_last_name>\w+)" "\s"
           "(?P<voice_first_name>\w+)" "\s*,\s*?"
           "(?P<specialty>[^;^,]+)" "\s*[;,]?\s*"
           ")")

print(pattern)
r = re.compile(pattern)
match_list = r.finditer(text)
for m in match_list:
    print("----- " + m.group("first_name") + m.group("last_name") + " -----")
    print("SP:" + m.group("specialty"))
    print("CV: " + m.group("voice_first_name") + m.group("voice_last_name"))
