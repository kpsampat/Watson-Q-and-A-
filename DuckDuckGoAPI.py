from duckduckpy import query

response = query('USA') # namedtuple is used as a container
#print(response)
res = response.result
print(res)

