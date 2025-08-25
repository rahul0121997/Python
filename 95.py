s = "i.like.this.program.very.much"

res = list(s.split("."))
string = ".".join(res[::-1])
print(string)