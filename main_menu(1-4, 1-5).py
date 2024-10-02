# 1) 영화 예매 결제 여부 확인 - 결제여부(y/n) 선택 입력 받기
# y -> 결제 완료
# n -> 시스템 종료

# 2) 영화 예매 결과 출력(mainmenu.py >> def)
# 예매한 영화제목(title) / 시간(time) / 좌석(seat) / 예매번호(rev_id) 출력 *단어는 임시 설정

# 영화 예매 결과 출력
# import

def rev_movie(title, time, seat, rev_id):
    print(f"영화제목 : {title}")
    print(f"상영시간 : {time}")
    print(f"선택좌석 : {seat}")
    print(f"예매번호 : {rev_id}")

def 영화_예매_프로그램():
    print("🎬🎬🎬 영화 예매 🎬🎬🎬")

    # 1) 영화 선택

    # 2) 상영 시간 선택

    # 3) 좌석 선택


# 영화 예매 결제 여부 확인
while True:
    pay_check = input("결제를 진행하시겠습니까? (y/n): ").lower()

    if pay_check == "y":
        print("🎫🎫🎫 예매가 완료되었습니다. 🎫🎫🎫")

        # 결제가 완료된 후 예매 결과 출력(예매영화(rev_movie))
        rev_movie(title, time, seat, rev_id)
        break

    elif pay_check == 'n':
        print("결제를 취소하여 프로그램을 종료합니다.\n🤗 다음에 또 오세요. 🤗")
        break

    else:
        print("잘못된 입력입니다.\n😊 y 또는 n으로 입력해 주세요. 😊") # 잘못 입력시 다시 y/n 선택









