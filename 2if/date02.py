
import datetime

now = datetime.datetime.now()

#오전
if now.hour <12:
    print(f"현재 시각은 {now.hour}시로 오전입니다.")


#오후
if now.hour >=12:
    print(f"현재 시각은 {now.hour}시로 오후입니다.")






