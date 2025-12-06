import string
import sys
def cumle_analizi(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            folder = f.read()
    except FileNotFoundError:
        print("dosya bluunamadı")
    
    for p in string.punctuation:
        text = folder.replace(p," ")
    words=text.lower().split()
    if not words:
        print("dosya boş")
        return 0
    count={}
    for w in words:
        count [w]=count.get(w,0) + 1

    total_words=len(words)
    total_benzersiz=len(count)
    print(f"toplam kelime {total_words} toplam benzersiz kelime {total_benzersiz}")
    top3= sorted(count.items(),key=lambda x:(-x[1],x[0]))[:3]
    # print(top3) ctrl+k+c hızlı yorum satırı
    uzun_kelimeler={w:c for w,c in count.items() if len(w)>5}
    en_uzun_kelime =max(uzun_kelimeler,
                    key=lambda x:(x[1],len(x[0]))
                    ,default=("yok",0))
    #print(en_uzun_kelime)
    alpha_kelimeler={w:c for w,c in count.items() if w.isalpha()}
    en_uzun_alpha =max(alpha_kelimeler,key=lambda:x(x[1],x[0]),default=("yok",0))
    
cumle_analizi("uygulama1.txt")
print("selam")