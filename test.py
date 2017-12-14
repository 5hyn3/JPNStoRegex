import jpns_to_regex


print("JPNS" + " → " + "Regex")

test1 = "( a か b か c ) が3回以上"
test2 = "行頭 任意の文字 が1回以上 空白文字"
test3 = "( タブ か   か 　 ) が0回以上9回以下"
test4 = "class 任意の文字 が1回以上 行末"

jregex = jpns_to_regex.JPNStoRegex(test1)
print(test1 + " → " + jregex.get_regex())

jregex = jpns_to_regex.JPNStoRegex(test2)
print(test2 + " → " + jregex.get_regex())

jregex = jpns_to_regex.JPNStoRegex(test3)
print(test3 + " → " + jregex.get_regex())

jregex = jpns_to_regex.JPNStoRegex(test4)
print(test4 + " → " + jregex.get_regex())
