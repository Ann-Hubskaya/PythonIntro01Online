s = 'eofheihwejhfwljkehbrilehhhhhhhewqfuhehfheqohfhweuifhweiuyrwei'

idx_l = s.find('h')
idx_r = s.rfind('h')
str_l = s[:idx_l+1]
str_r = s[idx_r:]
str_m = s[idx_l+1: idx_r]
res = str_l + str_m.replace('h', 'H') + str_r
print(res)

res1 = s[:s.find('h')+1] + s[s.find('h')+1: s.rfind('h')].replace('h', 'H') + s[s.rfind('h'):]
print(res1)

s1 = 'hehreh'
res2 = s1 if s1.find('h') == s1.rfind('h') else s1[:s1.find('h')+1] + s1[s1.find('h')+1: s1.rfind('h')].replace('h', 'H') + s1[s1.rfind('h'):]
print(res2)
