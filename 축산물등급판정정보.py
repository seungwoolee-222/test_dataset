import requests

url = 'http://data.ekape.or.kr/openapi-data/service/user/grade/auct/cattleDetail'
params ={'serviceKey' : 'Z%2BqOG0BXgDHjNYllLmPz7rVXZehwdYityRTSOZLJRIYYpIos1%2Fe7Mm488NQHCx3OmzOjKti2u4Y56rggoC2ktQ%3D%3D', 'startYmd' : '20220204', 'endYmd' : '20220204', 'breedCd' : '024001', 'sexCd' : '', 'qgradeYn' : 'N', 'defectIncludeYn' : '' }

response = requests.get(url, params=params)
print(response.content)