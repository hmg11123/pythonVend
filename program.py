from db import Vend
from util import Util

class Program :

     # ===================  VIEW VEND ======================

    def view_vend(vend) :

        if len(vend) <= 0 :
            print("🟥 [자판기] 물건이 없어 정보를 가져올 수 없습니다.")
        else :
            print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
            for v in vend :
                print(f"타입 : {v.type}")
                print(f"이름 : {v.name}")
                print(f"가격 : {v.value}원")
                print(f"팔린 개수 : {v.sell}개")
                print(f"재고 : {v.remnant}개")
                print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")


            print("1. 구매")
            print("0. 취소")
            

            answer = Util.custom_input3("구매하실 건가요? >>", 48 ,49)

            if answer == 1 :
                print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
                for v in enumerate(vend) :
                    print(f"{(v[0] + 1)} - {v[1].name}")
                print("0 - 취소하기")
                print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
                answer2 = Util.custom_input2("구매하고 싶은 물건의 번호를 입력해주세요. >>")

                if answer2 == 0 :
                    print("🟥 [자판기] 취소하셧습니다. | 숫자만 입력 가능합니다.")
                    return
                elif answer2 > len(vend) :
                    print("🟥 [자판기] 입력하신 물품은 없습니다.")
                else :
                    re_vend = Vend()
                    re_vend_type = vend[answer2 - 1].type
                    re_vend_name = vend[answer2 - 1].name
                    re_vend_value = vend[answer2 - 1].value
                    re_vend_sell = vend[answer2 - 1].sell + 1
                    re_vend_remnant = vend[answer2 - 1].remnant - 1

                    if re_vend_remnant < 1 and re_vend_sell > 99: 
                        print("🟥 [자판기] 이 제품이 품절되었습니다.")
                        vend.pop(answer2 - 1)
                    else :
                        vend.pop(answer2 - 1)

                        re_vend.data_setter(re_vend_type, re_vend_name, re_vend_value, re_vend_sell, re_vend_remnant)

                        vend.append(re_vend)
                        return True
            elif answer == 0:
                return False
            elif answer == "str" :
                print("🟥 [자판기] 잘못 입력하셧습니다.")
                return False
            else :
                print("🟥 [자판기] 잘못 입력하셧습니다.")
                return False
                

            
            
    # ===================  CREATE VEND ======================
            
        
    def create_vend(vend, type) :
        perv_len = len(vend)
        new_vend = Vend()


        for t in enumerate(type) :
            print(f"{t[0]+1}. {type[t[0]]}")
        print("0. 취소")

        
        type_input = Util.custom_input("타입를 입력하세요. >>", 48, 52)
        name_input = input("이름을 입력하세요. >>")
        value_input = Util.custom_input2("가격을 입력하세요. >>")


        if type_input == 1 :
            type_input = type[0]
        elif type_input == 2 :
            type_input = type[1]   
        elif type_input == 3 :
            type_input = type[2]
        elif type_input == 4 :
            type_input = type[3]
        else :
            print("🟥 [자판기] 위 타입만 고를 수 있습니다.")
            return False
        
        if len(name_input.strip()) == 0  :
            print("🟥 [자판기] 이름을 지정해주세요.")
            return False

        
        if value_input is False :
            print("🟥 [자판기] 가격은 숫자만 입력 가능합니다.")
            return False
        elif value_input < 500:
            print("🟥 [자판기] 물품의 가격은 500원 이상이어야 합니다.")
            return False
        else :
            new_vend.data_setter(type_input, name_input, value_input, 0, 100)
            vend.append(new_vend)

            next_len = len(vend)

            if perv_len < next_len :
                return True
            else :
                return False
    

    # ===================  DELETE VEND ======================
    def delete_vend(vend) :

        if len(vend) <= 0 :
            print("🟥 [자판기] 물건이 없어 삭제할 수 없습니다.")
        else :
            perv_len = len(vend)
            print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
            for v in enumerate(vend) :
                print(f"{(v[0] + 1)} - {v[1].name}")
            print("0 - 취소하기")
            print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")

            answer = Util.custom_input2("삭제할 물건의 번호를 입력해주세요. >>")

            if answer == 0 :
                print("🟥 [자판기] 취소하셧습니다. | 숫자만 입력 가능합니다.")
                return 
            elif answer > len(vend) :
                print("🟥 [자판기] 입력하신 물품은 없습니다.")
            else:
                vend.pop(answer - 1)
                
            next_len = len(vend)



            if perv_len > next_len :
                return True
            else :
                return False

    # def view_type(type) :

    #     print(type)

    # def create_type(type) :
        
    #     type_input = str(input("새로 만들 타입을 입력해주세요. >>"))


    #     # if type.split(" ") == type_input :
    #     #     print("sds")

    #     type.append(type_input)


    #     print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
    #     for t in type :
    #         print(t)
