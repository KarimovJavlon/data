def find_top_seller(products: dict, sales: dict) -> str:
    eng_maxs_mahsulot = None
    max_tushum = -1
    
    for mahsulot, narx in products.items():
        # Har bir mahsulot uchun tushum hisoblanadi: narx * sotilgan soni
        tushum = narx * sales.get(mahsulot, 0)
        
        # Eng yuqori tushum topiladi
        if tushum > max_tushum:
            max_tushum = tushum
            eng_maxs_mahsulot = mahsulot
            
    return eng_maxs_mahsulot

print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))