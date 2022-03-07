try:
    a=int(input("Enter the number\n "))

    b=25/a

    print(b)

except Exception as e:
    print(f"The error is generated as {e}")

    exit()


finally:
    print("We are done!")    # finally will execute in any situation! means that,even if try runs succesfully or not run or even after execution!
