class Util :

    def custom_input(u1, u2, u3) :
        answer = input(u1)

        if len(answer) > 1:
            return False
        elif len(answer) == 0:
            return False
        else :
            ascii_value = ord(answer)

            if ascii_value >= u2 and ascii_value <= u3 :
                return int(answer)
            else:
                return False


# 묹자열에서 정수형 구분하는 함수
    def custom_input2(u1) :
        answer = input(u1)

        if answer.isdigit() is True:
            return int(answer)
        else :
            return False
        
    # def custom_input3(u1) :
    #     answer = str(input(u1))

    #     if len(answer) < 0 :
    #         return False
    #     else :
            
    #         return answer


    def custom_input3(u1, u2 , u3) :
        answer = input(u1)
        print(answer)

        if answer.isdigit() is True:
            ascii_value = ord(answer)

            if ascii_value >= u2 and ascii_value <= u3 :
                return int(answer)
            elif answer.strip() == 0:
                return False
            else:
                return False
        elif len(answer) > 1:
            return False
        elif len(answer) == 0:
            return False
        else :
            return "str"
