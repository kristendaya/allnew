import json

data = {'age':30, 'name':'홍길동', 'address':'마포구 공덕동', 'broadcast':{'sbs':5, 'kbs':9, 'mbc':11}}

json_str = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True)

print(json_str)
print(type(json_str))
print( '-'*40)

json_data = json.loads(json_str)
print(json_str)
print(type(json_str))
print( '-'*40)

print(json_data['name'])
print(json_data['age'])
print(json_data['broadcast']['kbs'])


print('finished')