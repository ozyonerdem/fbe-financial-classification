# 📊 FBE Financial Health Classification Models

Şirketlerin finansal tablo verilerinden **finansal sağlık seviyesini** (Yüksek / Orta / Düşük) sınıflandırmaya yönelik bir veri madenciliği projesi. Kural tabanlı bir puanlama sistemiyle etiketlenen veri seti üzerinde dört farklı makine öğrenmesi modeli eğitilip karşılaştırıldı.

## 🎯 Amaç

Şirketlerin temel finansal oranları (özsermaye kârlılığı, faaliyet kâr marjı, cari oran, net borç/FAVÖK vb.) kullanılarak bir **Finansal Başarı Endeksi (FBE)** etiketi türetildi ve bu etiketin farklı sınıflandırma algoritmalarıyla ne kadar doğru tahmin edilebildiği incelendi.

## 🧮 Yöntem

**1. Etiketleme (Feature Engineering)**
Aşağıdaki 7 finansal orana dayalı ağırlıklı bir puanlama sistemiyle her şirkete bir FBE skoru ve buna karşılık gelen sınıf (`Yuksek` / `Orta` / `Dusuk`) atandı:
- Özsermaye Kârlılığı (%)
- Faaliyet Kâr Marjı
- Aktif Kârlılık (%)
- Cari Oran
- Net Borç / FAVÖK
- FAVÖK / Kısa Vade Borç
- Özsermaye / Aktif
- Net Satışlar / Kısa Vade Borç

**2. Veri Hazırlama**
- Eksik (NaN) ve sıfır değerli satırların temizlenmesi
- Anlamsız/etiket sızıntısına yol açabilecek sütunların (Şirket Adı, Periyot, Yıl, Altman Z-Skoru vb.) çıkarılması
- Stratified train / validation / test ayrımı (sınıf dağılımı korunarak)

**3. Modelleme**
Aşağıdaki dört sınıflandırma algoritması eğitilip karşılaştırıldı:
- Logistic Regression
- Naive Bayes
- Random Forest
- Decision Tree

**4. Değerlendirme**
Her model için ROC eğrileri, kalibrasyon grafikleri ve performans eğrileri (`RocPlots/`, `CalibrationPlots/`, `PerformanceCurvePlots/`) üretildi; ayrıca her modelin tahminleri ayrı CSV dosyalarına kaydedildi.

## 🛠 Teknolojiler

- Python
- pandas, numpy
- scikit-learn (train_test_split, sınıflandırma modelleri)
- Orange Data Mining (`.ows` dosyası — görsel iş akışı / model karşılaştırma)

## 📁 Proje Yapısı

```
.
├── data_mining.py                    # Veri temizleme, etiketleme, train/test/validation ayrımı
├── financial_data.csv                # Ham finansal veri seti
├── train.csv / test.csv / validation.csv
├── ground_truth.csv                  # Test seti gerçek etiketleri
├── train_validation_analyse.ows      # Orange ile model karşılaştırma iş akışı
├── *Predictions.csv                  # Her modelin tahmin sonuçları
│   ├── LogisticRegressionPredictions.csv
│   ├── NaiveBayesPredictions.csv
│   ├── RandomForestPredictions.csv
│   └── TreePredictions.csv
├── RocPlots/                         # Model bazlı ROC eğrileri
├── CalibrationPlots/                 # Model bazlı kalibrasyon grafikleri
└── PerformanceCurvePlots/            # Model bazlı performans eğrileri
```

## ▶️ Çalıştırma

```bash
pip install pandas numpy scikit-learn

python data_mining.py
```

Bu komut `financial_data.csv` dosyasını okuyup temizler, FBE sınıfını hesaplar ve `train.csv` / `test.csv` / `validation.csv` dosyalarını üretir. Model eğitimi ve karşılaştırması Orange Data Mining iş akışı (`train_validation_analyse.ows`) üzerinden yapılmıştır.

## 📌 Not

Bu proje, Ankara Üniversitesi Yazılım Mühendisliği bölümü **Veri Madenciliği** dersi kapsamında geliştirilmiştir.

## 👤 Geliştirici

Erdem Tahir Özyön — Ankara Üniversitesi, Yazılım Mühendisliği
