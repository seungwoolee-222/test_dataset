import requests

url = 'http://data.ekape.or.kr/openapi-data/service/user/animalTrace/traceNoSearch'
params ={'serviceKey' : 'Z%2BqOG0BXgDHjNYllLmPz7rVXZehwdYityRTSOZLJRIYYpIos1%2Fe7Mm488NQHCx3OmzOjKti2u4Y56rggoC2ktQ%3D%3D', 'traceNo' : 'L01709271277007t', 'optionNo' : '9', 'corpNo' : '1178522046' }

response = requests.get(url, params=params)
print(response.content)