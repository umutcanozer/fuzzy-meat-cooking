# 🍖 Akıllı Et Pişirme Asistanı

Bu proje, Python ile geliştirilmiş bir **bulanık mantık kontrol sistemi** kullanarak farklı et türleri için **pişirme süresi** ve **sıcaklık** tahmini yapar.  
Kullanıcıdan alınan 5 farklı girdiye göre 2 çıktıyı hesaplar. Arayüzü ise tamamen kullanıcı dostu olarak **Tkinter** ile tasarlanmıştır.

---

## 🎯 Problem Tanımı

Günlük hayatta et pişirirken birçok faktör hesaba katılır:
- Etin türü (tavuk mu kuzu mu?)
- Kalınlığı
- Yağ oranı
- Nasıl pişirileceği (ızgara mı, fırın mı?)
- Hangi pişmişlik tercih edildiği

Bu sistem, yukarıdaki gibi insanın sezgisel kararlarını **bulanık mantıkla** simüle ederek **pişirme süresi ve sıcaklık önerisi** yapar.

---

## 🔢 Girdi Değişkenleri

| Değişken         | Değerler                          |
|------------------|-----------------------------------|
| Et Türü          | Dana, Kuzu, Tavuk                 |
| Pişirme Yöntemi  | Izgara, Tavada, Fırında           |
| Pişirme Tercihi  | Az Pişmiş, Orta, Çok Pişmiş       |
| Yağ Oranı        | Yağsız, Orta Yağlı, Yağlı         |
| Et Kalınlığı     | 1.0 – 6.0 cm arası (slider ile)   |

---

## 🎯 Çıktı Değişkenleri

- **Pişirme Süresi** (dakika)
- **Pişirme Sıcaklığı** (°C veya °F olarak değiştirilebilir)

---

## 🚀 Kurulum ve Çalıştırma

### 1. Depoyu Klonla

```bash
git clone https://github.com/umutcanozer/fuzzy-meat-cooking.git
cd fuzzy-meat-cooking
```

### 2. Gerekli Paketleri Kur

```bash
pip install -r requirements.txt
```


### 3. Programı Başlat

```bash
python main.py
```
