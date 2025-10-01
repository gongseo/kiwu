import requests

url = f"https://wttr.in/jeju?format=%C+%t"
# url = f"https://kin.naver.com/park"
# url = f"https://wttr.in/incheon?&n&Q"
# url = f"https://wttr.in/incheon?&0&Q"
reponse = requests.get(url)
print(reponse)
print(reponse.status_code)
if response.status_code == 200:
  print(response.text.strip())
else:
  print(f"상태 코드 : {response.status_code}")
