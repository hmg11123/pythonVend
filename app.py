from db import Vend
from util import Util
from program import Program


all_vend = []

def start_app() :
    print("π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©")
    print("1. μνκΈ° λ©λ΄ λ³΄κΈ°")
    print("2. μνκΈ° λ©λ΄ μΆκ°")
    print("3. μνκΈ° λ©λ΄ μ­μ ")
    # print("4. μνκΈ° νμ λ³΄κΈ°")
    # print("5. μνκΈ° νμ μΆκ°")
    # print("6. μνκΈ° νμ μ­μ ")
    print("0. λκ°κΈ°")
    print("π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©π©")

    type = [
        "π§ μλ£",
        "π μν", 
        "π« ν°μΌ", 
        "π¦ λ¬Όν", 
    ]

    answer = Util.custom_input(">>", 48, 54)

    # =================== False ==================== 

    if answer is False:
        print("[μνκΈ°] μλͺ» λ μλ ₯μλλ€.")
        start_app()

    # =================== 1 ==================== 

    elif answer == 1:

        result = Program.view_vend(all_vend)

        if result is False :
            print("[μνκΈ°] μ·¨μνμ¨μ΅λλ€.")
        elif result is True :
            print("[μνκΈ°] κ΅¬λ§€νμ¨μ΅λλ€.")
        else :
            print("π₯ [μνκΈ°] μ·¨μνμ¨μ΅λλ€..")

        start_app()

    # =================== 2 ==================== 

    elif answer == 2 :
        result = Program.create_vend(all_vend, type)
        
        if result is True :
            print("[μνκΈ°] μλ‘μ΄ λ¬Όκ±΄μ΄ μΆκ° λμμ΅λλ€.")
            start_app()
        else :
            print("π₯ [μνκΈ°] λ¬ΌνμΆκ°μ μ€ν¨νμμ΅λλ€.")
            start_app()

    # =================== 3 ==================== 

    elif answer == 3 :
        result = Program.delete_vend(all_vend)
            
        if result is True:
            print("[μνκΈ°] λ¬Όκ±΄μ μ­μ νμ΅λλ€.")
            start_app()
        else : 
            print("π₯ [μνκΈ°] λ¬Όκ±΄μ μ­μ νλλ° μ€ν¨νμ΅λλ€.")
            start_app()
    # elif answer == 4 :
    #     result = Program.view_type(type)
    #     start_app()
    # elif answer == 5 :
    #     result = Program.create_type(type)
    #     start_app()

    # =================== 0 ==================== 
    elif answer == 0 :
        print("[μνκΈ°] μ’λ£")

start_app()