'''
외부 패키지의 설치 #1 : settings를 통한 방법
좌측 상단 메뉴버튼 -> file -> settings(혿은 alt + ctrl + s)
좌측리스트에서 project : 프로젝트명으로 되어있는 부분 클릭
-> python interpreter 클릭
-> 좌상단에 + 버튼 눌러서 필요한 패키지 검색 및 설치

외부 패키지의 설치 #2 : 터미널을 이용하는 방법
alt + f12 눌러서 터미널 켠다
pip install prettytable


'''
from prettytable import PrettyTable
from pokemon_data import *
# PrettyTable의 객체 생성
table = PrettyTable()
table.field_names = ['번호', '이름', '타입']

# for key in pokemon_data:
#     table.add_row(key)

table.add_rows(pokemon_data)

print(table)
