suhu = float(input("suhunya berapa bos : "))

if suhu < 0 :
    print("membeku")
elif suhu < 10 : 
    print("sangat dingin")
elif suhu < 20 :
    print("sejuk")
elif suhu < 30 :
    print("hangat")
elif suhu < 40 :
    print("panas")
else:
    print("sangat panas")