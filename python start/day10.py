
def format(f_name, l_name):
    print(f"{f_name.title()} {l_name.title()}")

format("bishal", "sharma") 

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1* n2
def div(n1,n2):
    return n1/n2

operation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    n1=float(input("what is the number"))

    for symbol in operation:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input("pick the symbols")
        n2=float(input("what is the number"))
        calculate_function=operation[operation_symbol]
        answer=calculate_function(n1,n2)
        print(f"{n1} {operation_symbol} {n2}={answer}")
        if input(f"type 'y' to continue with {answer}:or 'n' to start a new")=="y":
            n1=answer
        else:
            should_continue=False
        # operation_symbol=input("pick the other symbols")
        # n3=int(input("pick third num"))
        # calculate_function=operation[operation_symbol]
        # last_answer=calculate_function(answer,n3)
        # print(f"{answer}{operation_symbol} {n3}={last_answer}")
calculator()