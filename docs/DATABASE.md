# Veritabanı ve Meeting Veri Modeli

## Teknoloji
- Veritabanı: SQLite (dosya: `meeting_agent.db`)
- Bağlantı katmanı: SQLAlchemy
- Not: Geçici/basit seçim. İleride PostgreSQL'e geçilebilir.

## Dosyalar
- `app/database.py`: bağlantı, oturum (session) ve `get_db` fonksiyonu
- `app/models.py`: veri modelleri
- `test_db.py`: kayıt ekleme/okuma testi

## Tablo: meetings

| Alan | Tip | Açıklama |
|---|---|---|
| id | String (UUID) | Benzersiz kimlik, backend üretir |
| title | String | Toplantı başlığı (zorunlu) |
| meeting_at | DateTime | Toplantı zamanı (boş olabilir) |
| status | String | created, audio_uploaded, processing, completed, failed |
| created_at | DateTime | Oluşturulma zamanı (UTC) |
| updated_at | DateTime | Son güncelleme zamanı (UTC) |

## Test
`python test_db.py` bir toplantı kaydeder ve tekrar okur.