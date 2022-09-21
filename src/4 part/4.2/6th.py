a, b = map(int, input().split())

if a in [1, 3, 5, 7, 8, 10, 12]:
    d_o_m = 31
elif a == 2:
    d_o_m = 28
else:
    d_o_m = 30

if b == d_o_m:
    next_date = 1
    next_month = a + 1
else:
    next_date = b + 1
    next_month = a

if b == 1:
    priv_month = a - 1
    if priv_month in [1, 3, 5, 7, 8, 10, 12]:
        priv_day = 31
    elif priv_month == 2:
        priv_day = 28
    else:
        priv_day = 30
else:
    priv_month = a
    priv_day = b - 1

print(f"{priv_month:02}.{priv_day:02} {next_month:02}.{next_date:02}")

