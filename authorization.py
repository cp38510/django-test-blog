import requests

my_domain = 'cp38510.pythonanywhere.com'
username = 'cp38510'
token = 'bdcffe22cf57def45614173fa27fd853d509c983'

response = requests.post(
  'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
      username=username, domain=my_domain
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('All OK')
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
