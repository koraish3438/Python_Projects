ans = input("Do you play this game? say [yes/no] : ")

if ans == "yes":
    print("Welcome to the adventure game..let's go....")
    ans = input("Where do you go now jungle or cave? : ")
    if ans == "jungle":
        ans = input("A hungry tiger in font of you. Now what do you want run or fight? : ")
        if ans == "run":
            print("Congratulation! you still alive..")
        else:
            print("The tiger is very strong you loss..")
    elif ans == "cave":
        ans = input("A bear sleep on there. Now what do want run or fight? : ")
        if ans == "run":
            print("Congratulation! you still alive..")
        else:
            print("The bear is very strong you loss..")

else:
    print("Please play one time")