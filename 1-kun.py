def count_vowels_and_consonants(text: str) -> dict:
    unli_harflar = "aeiouAEIOU"
    unli = 0
    undosh = 0
    
    for char in text:
        if char.isalpha():
            if char in unli_harflar:
                unli += 1
            else:
                undosh += 1
                
    return {"unli": unli, "undosh": undosh}

print(count_vowels_and_consonants("Salom Dunyo!"))