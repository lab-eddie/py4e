# # <정 규 표 현 식>
# data = """
# park 800905-1049118
# kim  700905-1059119"""

# # result = []
# # for line in date.split("\n"):
# #     word_result = []
# #     for word in line.split(" "):
# #         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
# #             word = word[:6] + "-" + "******"
# #         word_result.append(word)
# #     result.append(" ".join(word_result))
# # print("\n".join(result))

# import re

# pat = re.compile("(\d{6}[-]\d{7})")
# print(pat.sub("\g<1>-******", data))

import re
p = re.compile("[a-z]+")
# m = p.match("3python")
# m = p.search("3 python")
# m = p.findall("life is too short")
m = p.finditer("life is too short")
print(m)
for i in m:
    print(i)