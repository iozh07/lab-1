# TODO Найдите количество книг, которое можно разместить на дискете
mem_in_bites = 1.44*1024*1024
pages = 100
rows = 50
symbols_in_row = 25
symbols_book = symbols_in_row*rows*pages*4
amount = mem_in_bites/symbols_book

print("Количество книг, помещающихся на дискету:", round(amount))






