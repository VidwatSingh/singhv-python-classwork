temp = int(input("what is the temperature: "))
humidity = input("what is the humidity: ")
window = input("is the window open or closed: ")
if window == "closed":
    if temp > 25 or humidity > 50:
        print("Open the window")
    else:
        print("close the window")
else:
    print("keep the window closed")