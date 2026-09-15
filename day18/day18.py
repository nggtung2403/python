import re
txt = "I love to teach python"
match = re.match("I love to teach",txt,re.I)
print(match)
span = match.span()
print(span)
start,end = span
print(start,end)
substring = txt[start:end]
print(substring)

txt = "I love to teach python and javastcript"
match = re.match("I love to teach",txt,re.I)
print(match)
print(match.group(0))

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search("first",txt,re.I)
print(match)
span = match.span()
print(span)
a,b = span
substring = txt[a:b]
print(substring)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.findall("Language",txt,re.I)
print(match)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.findall("python",txt,re.I)
print(match)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.findall("python",txt)
print(match)
match = re.findall("python|Python",txt)
print(match)
match = re.findall("[Pp]ython",txt)
print(match)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_replace = re.sub("Python|python","C++",txt,re.I)
print(match_replace)
match_replace = re.sub("C\+\+","python",match_replace)
print(match_replace)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
match = re.sub("%","",txt)
print(match)

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split("\n",txt))

regex_pattern = r"banana"
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
match = re.findall(regex_pattern,txt)
print(match)