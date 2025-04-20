#!/bin/bash
export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1
export LC_CTYPE=tr_TR.UTF-8

echo "Lütfen yapmak istediğiniz işlemi seçin:"
echo "1: Ping atmak istediğiniz web sitesine ping gönder"
echo "2: Sayı yarışması (GS vs FB)"
echo "3: Dosya yükle (GitHub'a)"
echo "4: Kelime ayırıcı"
read secim

if [ "$secim" == "1" ]; then
    echo "Ping atmak istediğiniz web sitesinin adresini girin:"
    read adres
    ping "$adres"
elif [ "$secim" == "2" ]; then
    python3 << 'EOF'
import random
gs = random.randint(0, 10)
fb = random.randint(0, 10)
print("GS:", gs)
print("FB:", fb)

if gs > fb:
    print("GS, FB'den daha çok gol atmıştır.")
elif fb > gs:
    print("FB, GS'den daha fazla gol atmıştır.")
else:
    print("İkisinin golü eşit")
EOF
elif [ "$secim" == "3" ]; then
    echo "Dosya yükle seçildi. Lütfen aşağıdaki alt seçeneklerden birini seçin:"
    echo "a: Yeni repoyu yükle (GitHub'a yeni repoyu ekle)"
    echo "b: Eski repoyu yükle (GitHub'a mevcut repoyu ekle)"
    read alt_secim

    if [ "$alt_secim" == "a" ]; then
        echo "Yeni repoyu oluşturmak için dizin adını girin:"
        read dirname
        mkdir "$dirname"
        cd "$dirname" || exit
        git init
        git add .
        echo "İlk commit mesajını girin:"
        read commit_msg
        git commit -m "$commit_msg"
        echo "GitHub remote URL'sini girin (örneğin: git@github.com:kullanici/repoadi.git):"
        read remote_url
        git remote add origin "$remote_url"
        git push -u origin master
    elif [ "$alt_secim" == "b" ]; then
        echo "Eski repoyu yüklemek için dizin adını girin:"
        read dirname
        cd "$dirname" || exit
        git add .
        echo "Commit mesajını girin:"
        read commit_msg
        git commit -m "$commit_msg"
        git push
    else
        echo "Geçersiz alt seçenek."
    fi
elif [ "$secim" == "4" ]; then
    python3 << 'EOF'
g = """Söz konusu toplantı basına kapalı olarak gerçekleştirilmiştir. Bu toplantıda döviz kuruna ilişkin Sayın Bakanımıza atfedilen ve haberde yer verilen değerlendirmeler doğru değildir.
Sayın Bakanımız, ihracatçıların kura ilişkin sorularına verdiği yanıtta; döviz piyasasının sağlıklı işlemesi için oynaklığı dengeleyici adımlar atıldığını ve enflasyon beklentileri çıpalanana kadar aşırı dalgalanmalara izin verilmeyeceğini ifade etmiştir. Uygulanan para politikasının özünün Türk Lirası’nın değerlenmesine odaklanmadığını belirten Sayın Bakanımız, Türk Lirasına artan ilginin doğal olarak kurda reel bir değerlenme oluşturduğunu vurgulamıştır."""
kelimeler = g.split()

def donustur(a):
    sayac = []
    for kelime in a:
        print(kelime)
        sayici = 0
        for harf in kelime:
            sayici += 1
        sayac.append(sayici)
    return sayac

b = donustur(kelimeler)
EOF
else
    echo "Geçersiz seçim."
fi
