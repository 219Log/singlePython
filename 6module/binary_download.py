from urllib import request
import os

target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

os.makedirs("data", exist_ok=True)
file = open("data/logo.png", "wb")
file.write(output)
file.close()