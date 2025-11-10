low = -1
high = 11

while True:
    try:
        guess = int(input())
        response = input()

        if response == 'too high':
            high = min(high, guess)
        elif response == 'too low':
            low = max(low, guess)
        else:
            if low < guess < high:
                print('Stan may be honest')
            else:
                print('Stan is dishonest')
            low = -1
            high = 11

    except EOFError:
        exit()
