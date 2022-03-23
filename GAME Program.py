import random

life = 5
score = 0
combo = 0

while True:

    print("="*30)
    print("♥ "*life + "♡ " *(5-life))
    print(combo,"combo!")
    print("="*30)

    com = random.randint(10,99)
    user = int(input("홀(1)? 짝(0)?"))

    if com % 2 == user:
        print("O")
        score += 100 * (1 + 0.2*combo)
        combo += 1
                    
    else:
        print("X")
        life -= 1
        comno = 0

        if life == 0:
            print("G.A.M.E O.V.E.R")
            print("점수", score)
            break
