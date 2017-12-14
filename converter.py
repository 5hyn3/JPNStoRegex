import sys
import jpns_to_regex

args = sys.argv

jregex = jpns_to_regex.JPNStoRegex(sys.argv[1])
print(jregex.get_regex())
