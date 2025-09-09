tel = input('전화번호를 입력하세요 >>> ')
if tel[3] != '-' and tel[8] != '-' and len(tel) != 13:
    print('유효하지않은 전화번호 형식입니다.')
else:
    print(f'전화번호의 중간 4자리는 {tel[4:8]} 입니다.')