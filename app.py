from db import Vend
from util import Util
from program import Program


all_vend = []

def start_app() :
    print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")
    print("1. 자판기 메뉴 보기")
    print("2. 자판기 메뉴 추가")
    print("3. 자판기 메뉴 삭제")
    # print("4. 자판기 타입 보기")
    # print("5. 자판기 타입 추가")
    # print("6. 자판기 타입 삭제")
    print("0. 나가기")
    print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")

    type = [
        "🧋 음료",
        "🍜 식품", 
        "🎫 티켓", 
        "📦 물품", 
    ]

    answer = Util.custom_input(">>", 48, 54)

    # =================== False ==================== 

    if answer is False:
        print("[자판기] 잘못 된 입력입니다.")
        start_app()

    # =================== 1 ==================== 

    elif answer == 1:

        result = Program.view_vend(all_vend)

        if result is False :
            print("[자판기] 취소하셨습니다.")
        elif result is True :
            print("[자판기] 구매하셨습니다.")
        else :
            print("🟥 [자판기] 취소하셨습니다..")

        start_app()

    # =================== 2 ==================== 

    elif answer == 2 :
        result = Program.create_vend(all_vend, type)
        
        if result is True :
            print("[자판기] 새로운 물건이 추가 되었습니다.")
            start_app()
        else :
            print("🟥 [자판기] 물품추가에 실패하였습니다.")
            start_app()

    # =================== 3 ==================== 

    elif answer == 3 :
        result = Program.delete_vend(all_vend)
            
        if result is True:
            print("[자판기] 물건을 삭제했습니다.")
            start_app()
        else : 
            print("🟥 [자판기] 물건을 삭제하는데 실패했습니다.")
            start_app()
    # elif answer == 4 :
    #     result = Program.view_type(type)
    #     start_app()
    # elif answer == 5 :
    #     result = Program.create_type(type)
    #     start_app()

    # =================== 0 ==================== 
    elif answer == 0 :
        print("[자판기] 종료")

start_app()