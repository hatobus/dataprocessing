try:
    while(1):
        print("同じ文字数の文字列を入力してください")
        S=input()
        T=input()
        
        for i in range(len(S)):
            print(S[i],end="")
            print(T[i],end="")
            
        print("")
            
except KeyboardInterrupt:
    print("End!")