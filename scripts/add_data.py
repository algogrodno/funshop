# populate_db.py
import os
import django
from decimal import Decimal
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')  
django.setup()

from shop.models import Category, Product 

# Данные для категорий
cats = [
    ('accessories', 'Аксессуары'),
    ('gaming', 'Гейминг'),
    ('home', 'Дом'),
    ('books', 'Книги'),
    ('kompyutry', 'Компьютеры'),
    ('noutbuki', 'Ноутбуки'),
    ('office', 'Офис'),
    ('sports', 'Спорт'),
    ('telefony', 'Телефоны'),
    ('electronics', 'Электроника'),
]

# Товары для каждой категории
# products_data.py - полные данные со ссылками на разные цвета

products_data = {
    'accessories': [
        {
            'name': 'Беспроводные наушники Sony WH-1000XM5',
            'slug': 'sony-wh-1000xm5',
            'price': 349.99,
            'stock': 15,
            'available': True,
            'is_popular': True,
            'description': 'Высококачественные беспроводные наушники с шумоподавлением. Время работы до 30 часов.',
            'image_url': 'https://placehold.co/600x400/1a1a2e/ffffff?text=Sony+WH-1000XM5&font=montserrat'
        },
        {
            'name': 'Клавиатура Logitech MX Mechanical',
            'slug': 'logitech-mx-mechanical',
            'price': 199.99,
            'stock': 10,
            'available': True,
            'is_popular': True,
            'description': 'Механическая клавиатура с подсветкой и тактильными переключателями',
            'image_url': 'https://placehold.co/600x400/2d2d44/ffffff?text=Logitech+MX&font=montserrat'
        },
        {
            'name': 'Мышь Apple Magic Mouse',
            'slug': 'apple-magic-mouse',
            'price': 89.99,
            'stock': 20,
            'available': True,
            'is_popular': False,
            'description': 'Стильная беспроводная мышь с сенсорной поверхностью',
            'image_url': 'https://placehold.co/600x400/e0e0e0/333333?text=Apple+Magic+Mouse&font=montserrat'
        },
        {
            'name': 'Чехол для телефона Spigen',
            'slug': 'spigen-phone-case',
            'price': 29.99,
            'stock': 50,
            'available': True,
            'is_popular': False,
            'description': 'Защитный чехол с военной сертификацией MIL-STD-810G',
            'image_url': 'https://placehold.co/600x400/4a4e69/ffffff?text=Spigen+Case&font=montserrat'
        },
    ],
    'gaming': [
        {
            'name': 'Игровая приставка PlayStation 5',
            'slug': 'ps5',
            'price': 499.99,
            'stock': 5,
            'available': True,
            'is_popular': True,
            'description': 'Новейшая игровая приставка с SSD накопителем и поддержкой 4K',
            'image_url': 'https://placehold.co/600x400/0a2463/ffffff?text=PlayStation+5&font=montserrat'
        },
        {
            'name': 'Игровая мышь Razer Viper Ultimate',
            'slug': 'razer-viper-ultimate',
            'price': 149.99,
            'stock': 12,
            'available': True,
            'is_popular': True,
            'description': 'Беспроводная мышь с оптическими переключателями и весом 74г',
            'image_url': 'https://placehold.co/600x400/1e1e2f/00ff00?text=Razer+Viper&font=montserrat'
        },
        {
            'name': 'Игровая клавиатура HyperX Alloy',
            'slug': 'hyperx-alloy',
            'price': 129.99,
            'stock': 8,
            'available': True,
            'is_popular': False,
            'description': 'Механическая клавиатура с RGB подсветкой и алюминиевым корпусом',
            'image_url': 'https://placehold.co/600x400/2a2a2a/ff4444?text=HyperX+Alloy&font=montserrat'
        },
        {
            'name': 'Игровой монитор ASUS ROG 27"',
            'slug': 'asus-rog-monitor',
            'price': 599.99,
            'stock': 3,
            'available': True,
            'is_popular': True,
            'description': '27" монитор с частотой 240Hz и временем отклика 1ms',
            'image_url': 'https://placehold.co/600x400/0d1117/00ffff?text=ASUS+ROG&font=montserrat'
        },
    ],
    'home': [
        {
            'name': 'Умная колонка Яндекс Станция 2',
            'slug': 'yandex-station-2',
            'price': 199.99,
            'stock': 20,
            'available': True,
            'is_popular': True,
            'description': 'Умная колонка с голосовым помощником Алиса и LED-экраном',
            'image_url': 'https://placehold.co/600x400/2b2d42/edf2f4?text=Yandex+Station&font=montserrat'
        },
        {
            'name': 'Робот-пылесос Xiaomi Roborock S7',
            'slug': 'roborock-s7',
            'price': 399.99,
            'stock': 7,
            'available': True,
            'is_popular': True,
            'description': 'Робот-пылесос с функцией влажной уборки и лазерной навигацией',
            'image_url': 'https://placehold.co/600x400/ffffff/333333?text=Roborock+S7&font=montserrat'
        },
        {
            'name': 'Умная лампочка Xiaomi Yeelight',
            'slug': 'yeelight-smart-bulb',
            'price': 24.99,
            'stock': 35,
            'available': True,
            'is_popular': False,
            'description': 'LED лампочка с 16 млн цветов и управлением через Wi-Fi',
            'image_url': 'https://placehold.co/600x400/ffd166/1a1a1a?text=Yeelight&font=montserrat'
        },
        {
            'name': 'Умная розетка TP-Link Tapo',
            'slug': 'tapo-smart-plug',
            'price': 15.99,
            'stock': 40,
            'available': True,
            'is_popular': False,
            'description': 'Умная розетка с контролем энергопотребления',
            'image_url': 'https://placehold.co/600x400/2b5c8f/ffffff?text=TP-Link+Tapo&font=montserrat'
        },
    ],
    'books': [
        {
            'name': 'Django 4 by Example (4th Edition)',
            'slug': 'django-4-by-example',
            'price': 54.99,
            'stock': 25,
            'available': True,
            'is_popular': True,
            'description': 'Полное руководство по Django 4 с примерами реальных проектов',
            'image_url': 'https://placehold.co/600x400/092834/ffffff?text=Django+4+by+Example&font=montserrat'
        },
        {
            'name': 'Python. К вершинам мастерства',
            'slug': 'python-mastery',
            'price': 49.99,
            'stock': 30,
            'available': True,
            'is_popular': True,
            'description': 'Углубленное изучение Python: паттерны, best practices',
            'image_url': 'https://placehold.co/600x400/306998/ffd43b?text=Python+Mastery&font=montserrat'
        },
        {
            'name': 'Clean Code: Роберт Мартин',
            'slug': 'clean-code',
            'price': 59.99,
            'stock': 18,
            'available': True,
            'is_popular': True,
            'description': 'Искусство написания чистого кода. Бестселлер №1',
            'image_url': 'https://placehold.co/600x400/1a472a/ffffff?text=Clean+Code&font=montserrat'
        },
        {
            'name': 'JavaScript: The Good Parts',
            'slug': 'js-good-parts',
            'price': 29.99,
            'stock': 22,
            'available': True,
            'is_popular': False,
            'description': 'Лучшие части JavaScript от Дугласа Крокфорда',
            'image_url': 'https://placehold.co/600x400/f7df1e/323330?text=JavaScript&font=montserrat'
        },
    ],
    'kompyutry': [
        {
            'name': 'Apple Mac mini M2 Pro',
            'slug': 'mac-mini-m2-pro',
            'price': 1299.99,
            'stock': 8,
            'available': True,
            'is_popular': True,
            'description': 'Компактный компьютер с чипом M2 Pro, до 32GB RAM',
            'image_url': 'https://placehold.co/600x400/555555/ffffff?text=Mac+mini+M2&font=montserrat'
        },
        {
            'name': 'Dell XPS Desktop',
            'slug': 'dell-xps-desktop',
            'price': 1499.99,
            'stock': 5,
            'available': True,
            'is_popular': False,
            'description': 'Мощный настольный компьютер с Intel Core i9',
            'image_url': 'https://placehold.co/600x400/0078d4/ffffff?text=Dell+XPS&font=montserrat'
        },
        {
            'name': 'HP Envy Desktop',
            'slug': 'hp-envy-desktop',
            'price': 899.99,
            'stock': 6,
            'available': True,
            'is_popular': False,
            'description': 'Универсальный компьютер с AMD Ryzen 7',
            'image_url': 'https://placehold.co/600x400/0096d6/ffffff?text=HP+Envy&font=montserrat'
        },
    ],
    'noutbuki': [
        {
            'name': 'Apple MacBook Pro 16" M3 Pro',
            'slug': 'macbook-pro-m3-pro',
            'price': 2499.99,
            'stock': 10,
            'available': True,
            'is_popular': True,
            'description': 'Мощный ноутбук с чипом M3 Pro и 18 часами работы',
            'image_url': 'https://placehold.co/600x400/333333/ffffff?text=MacBook+Pro+16&font=montserrat'
        },
        {
            'name': 'Dell XPS 15',
            'slug': 'dell-xps-15-2024',
            'price': 1899.99,
            'stock': 7,
            'available': True,
            'is_popular': True,
            'description': 'Ноутбук премиум-класса с OLED дисплеем',
            'image_url': 'https://placehold.co/600x400/2c3e50/ffffff?text=Dell+XPS+15&font=montserrat'
        },
        {
            'name': 'ASUS ROG Zephyrus G14',
            'slug': 'asus-rog-g14',
            'price': 1399.99,
            'stock': 5,
            'available': True,
            'is_popular': True,
            'description': 'Игровой ноутбук с AMD Ryzen 9 и RTX 4060',
            'image_url': 'https://placehold.co/600x400/1a1a1a/ff3366?text=ROG+Zephyrus&font=montserrat'
        },
        {
            'name': 'Lenovo ThinkPad X1 Carbon',
            'slug': 'thinkpad-x1-carbon',
            'price': 1699.99,
            'stock': 4,
            'available': True,
            'is_popular': False,
            'description': 'Бизнес ноутбук из карбона, вес 1.1кг',
            'image_url': 'https://placehold.co/600x400/1a1a1a/ff0000?text=ThinkPad+X1&font=montserrat'
        },
    ],
    'office': [
        {
            'name': 'Офисное кресло Metta S-Class',
            'slug': 'metta-s-class',
            'price': 249.99,
            'stock': 12,
            'available': True,
            'is_popular': True,
            'description': 'Эргономичное кресло с поддержкой поясницы и подголовником',
            'image_url': 'https://placehold.co/600x400/2c2c2c/ffffff?text=Metta+S-Class&font=montserrat'
        },
        {
            'name': 'МФУ Brother DCP-L3550CDW',
            'slug': 'brother-dcp-l3550cdw',
            'price': 399.99,
            'stock': 8,
            'available': True,
            'is_popular': True,
            'description': 'Цветной лазерный МФУ с двусторонней печатью',
            'image_url': 'https://placehold.co/600x400/0066b3/ffffff?text=Brother+MFP&font=montserrat'
        },
        {
            'name': 'Ламинатор Fellowes Saturn 3',
            'slug': 'fellowes-saturn-3',
            'price': 119.99,
            'stock': 15,
            'available': True,
            'is_popular': False,
            'description': 'Профессиональный ламинатор A3 с 4 валами',
            'image_url': 'https://placehold.co/600x400/4a4a4a/ffffff?text=Fellowes+Saturn&font=montserrat'
        },
        {
            'name': 'Уничтожитель бумаг Rexel',
            'slug': 'rexel-shredder',
            'price': 89.99,
            'stock': 10,
            'available': True,
            'is_popular': False,
            'description': 'Шреддер для уничтожения документов уровня P-4',
            'image_url': 'https://placehold.co/600x400/3a6b4b/ffffff?text=Rexel+Shredder&font=montserrat'
        },
    ],
    'sports': [
        {
            'name': 'Умные часы Garmin Fenix 7',
            'slug': 'garmin-fenix-7',
            'price': 699.99,
            'stock': 8,
            'available': True,
            'is_popular': True,
            'description': 'GPS часы для спорта с солнечной зарядкой',
            'image_url': 'https://placehold.co/600x400/1a1a1a/00ff88?text=Garmin+Fenix+7&font=montserrat'
        },
        {
            'name': 'Беговая дорожка HouseFit Pro',
            'slug': 'housefit-pro-treadmill',
            'price': 799.99,
            'stock': 4,
            'available': True,
            'is_popular': True,
            'description': 'Электрическая беговая дорожка с 12 программами',
            'image_url': 'https://placehold.co/600x400/333333/ff6600?text=HouseFit+Pro&font=montserrat'
        },
        {
            'name': 'Велотренажер NordicTrack',
            'slug': 'nordictrack-bike',
            'price': 599.99,
            'stock': 6,
            'available': True,
            'is_popular': False,
            'description': 'Стационарный велотренажер с iFit тренировками',
            'image_url': 'https://placehold.co/600x400/2c3e50/ecf0f1?text=NordicTrack&font=montserrat'
        },
        {
            'name': 'Фитнес-браслет Xiaomi Mi Band 8',
            'slug': 'mi-band-8',
            'price': 39.99,
            'stock': 50,
            'available': True,
            'is_popular': True,
            'description': 'Фитнес-трекер с AMOLED экраном и NFC',
            'image_url': 'https://placehold.co/600x400/ff6b35/ffffff?text=Mi+Band+8&font=montserrat'
        },
    ],
    'telefony': [
        {
            'name': 'Apple iPhone 15 Pro Max',
            'slug': 'iphone-15-pro-max',
            'price': 1299.99,
            'stock': 15,
            'available': True,
            'is_popular': True,
            'description': 'Титановый корпус, A17 Pro, USB-C, 5x оптический зум',
            'image_url': 'https://placehold.co/600x400/555555/ffffff?text=iPhone+15+Pro+Max&font=montserrat'
        },
        {
            'name': 'Samsung Galaxy S24 Ultra',
            'slug': 'samsung-s24-ultra',
            'price': 1199.99,
            'stock': 12,
            'available': True,
            'is_popular': True,
            'description': '200MP камера, S Pen, Titanium корпус',
            'image_url': 'https://placehold.co/600x400/1a1a2e/ffffff?text=Galaxy+S24+Ultra&font=montserrat'
        },
        {
            'name': 'Google Pixel 8 Pro',
            'slug': 'google-pixel-8-pro',
            'price': 999.99,
            'stock': 10,
            'available': True,
            'is_popular': True,
            'description': 'Лучшая камера, чистый Android, AI функции',
            'image_url': 'https://placehold.co/600x400/4285f4/ffffff?text=Pixel+8+Pro&font=montserrat'
        },
        {
            'name': 'Xiaomi 14 Ultra',
            'slug': 'xiaomi-14-ultra',
            'price': 899.99,
            'stock': 18,
            'available': True,
            'is_popular': False,
            'description': 'Камера Leica, Snapdragon 8 Gen 3',
            'image_url': 'https://placehold.co/600x400/ff6900/ffffff?text=Xiaomi+14+Ultra&font=montserrat'
        },
    ],
    'electronics': [
        {
            'name': 'Телевизор Samsung Neo QLED 65"',
            'slug': 'samsung-neo-qled-65',
            'price': 1599.99,
            'stock': 5,
            'available': True,
            'is_popular': True,
            'description': '4K телевизор с Mini-LED и квантовыми точками',
            'image_url': 'https://placehold.co/600x400/000000/00ffff?text=Samsung+Neo+QLED&font=montserrat'
        },
        {
            'name': 'Дрон DJI Mini 4 Pro',
            'slug': 'dji-mini-4-pro',
            'price': 759.99,
            'stock': 7,
            'available': True,
            'is_popular': True,
            'description': 'Компактный дрон с 4K камерой и датчиками препятствий',
            'image_url': 'https://placehold.co/600x400/2b2b2b/ffd700?text=DJI+Mini+4+Pro&font=montserrat'
        },
        {
            'name': 'Фотоаппарат Sony A7 IV',
            'slug': 'sony-a7-iv',
            'price': 2499.99,
            'stock': 3,
            'available': True,
            'is_popular': True,
            'description': 'Полнокадровая беззеркалка 33MP, видео 4K 60p',
            'image_url': 'https://placehold.co/600x400/1a1a1a/ff4444?text=Sony+A7+IV&font=montserrat'
        },
        {
            'name': 'Экшн-камера GoPro Hero 12',
            'slug': 'gopro-hero-12',
            'price': 399.99,
            'stock': 12,
            'available': True,
            'is_popular': False,
            'description': 'Водонепроницаемая камера, 5.3K видео, стабилизация',
            'image_url': 'https://placehold.co/600x400/222222/ffffff?text=GoPro+Hero+12&font=montserrat'
        },
    ],
}

def populate_database():
    """Заполнение базы данных категориями и товарами"""
    
    print("Начинаем заполнение базы данных...")
    print("-" * 50)
    
    # Создаем категории
    categories = {}
    for slug, name in cats:
        category, created = Category.objects.get_or_create(
            slug=slug,
            defaults={'name': name}
        )
        categories[slug] = category
        status = "Создана" if created else "Уже существует"
        print(f"{status} категория: {name} (slug: {slug})")
    
    print("\n" + "=" * 50)
    print("Добавление товаров:")
    print("-" * 50)
    
    # Создаем товары
    total_products = 0
    for category_slug, products in products_data.items():
        if category_slug in categories:
            category = categories[category_slug]
            category_products_count = 0
            
            for product_data in products:
                # Проверяем, существует ли товар с таким slug
                product, created = Product.objects.get_or_create(
                    slug=product_data['slug'],
                    defaults={
                        'category': category,
                        'name': product_data['name'],
                        'price': Decimal(str(product_data['price'])),
                        'stock': product_data['stock'],
                        'available': product_data['available'],
                        'is_popular': product_data['is_popular'],
                        'description': product_data['description'],
                    }
                )
                
                if created:
                    category_products_count += 1
                    total_products += 1
                    print(f"  ✓ {category.name}: {product.name} - ${product.price}")
            
            if category_products_count == 0:
                print(f"  Все товары в категории '{category.name}' уже существуют")
    
    print("\n" + "=" * 50)
    print(f"Итог: Создано {total_products} новых товаров")
    print(f"Всего категорий: {Category.objects.count()}")
    print(f"Всего товаров: {Product.objects.count()}")
    print("-" * 50)
    print("База данных успешно заполнена!")

def clear_database():
    """Очистка базы данных (опционально)"""
    confirm = input("Вы уверены, что хотите удалить все товары и категории? (yes/no): ")
    if confirm.lower() == 'yes':
        Product.objects.all().delete()
        Category.objects.all().delete()
        print("База данных очищена!")
    else:
        print("Очистка отменена.")

if __name__ == "__main__":            
    clear_database()
    populate_database()