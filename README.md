# 📱 PhoneStoreProject

Website bán điện thoại di động được xây dựng bằng **Django Framework** (Python).

## 📋 Giới thiệu

**PhoneStore** là một dự án website thương mại điện tử chuyên về lĩnh vực bán lẻ điện thoại. Dự án hỗ trợ đầy đủ các chức năng cơ bản của một cửa hàng trực tuyến, từ hiển thị sản phẩm đến quản lý giỏ hàng và đặt hàng.

Dự án được phát triển với mục tiêu học tập và thực hành **Django Web Framework**, bao gồm các khái niệm: Models, Views, Templates, Authentication, Admin Panel, và quản lý database.

## ✨ Tính năng chính

- **Trang chủ** với sản phẩm nổi bật
- **Danh mục sản phẩm** (Category & Sub-category)
- **Chi tiết sản phẩm** (giá, mô tả, hình ảnh, nhà cung cấp)
- **Đăng ký / Đăng nhập** (Custom User Model)
- **Giỏ hàng** (Add to Cart, Update, Remove)
- **Đặt hàng** và quản lý đơn hàng
- **Quản trị viên** (Django Admin)
- **Tìm kiếm** sản phẩm
- **Upload hình ảnh** sản phẩm
- **Responsive** trên nhiều thiết bị

## 🛠 Công nghệ sử dụng

- **Backend**: Django 5.0.4
- **Ngôn ngữ**: Python
- **Database**: SQLite (có thể chuyển sang PostgreSQL/MySQL)
- **Frontend**: HTML, CSS, JavaScript + Bootstrap
- **Thư viện chính**:
  - Pillow (xử lý hình ảnh)
  - Whitenoise (static files)
  - XlsxWriter (xuất file Excel)

## 📁 Cấu trúc dự án

```
PhoneStoreProject/
├── PhoneStore/                  # Project chính
│   ├── phone/                   # Django App
│   │   ├── migrations/
│   │   ├── static/phone/        # CSS, JS, Images
│   │   ├── templates/phone/     # HTML templates
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── ...
│   ├── .ebextension/            # Cấu hình Elastic Beanstalk (AWS)
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt
├── .vscode/
├── .gitignore
└── README.md
```

## 📋 Các Model chính

- **CustomerUser**: Kế thừa User (thêm phone, address)
- **Category**: Hỗ trợ danh mục cha - con
- **Product**: Sản phẩm (tên, giá, số lượng, hình ảnh, mô tả...)
- **Order**: Đơn hàng
- **OrderItem**: Chi tiết đơn hàng

## 🚀 Hướng dẫn cài đặt & chạy

### 1. Clone repository
```bash
git clone https://github.com/HoangQuyCoder/PhoneStoreProject.git
cd PhoneStoreProject/PhoneStore
```

### 2. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 3. Migrate database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Tạo superuser
```bash
python manage.py createsuperuser
```

### 5. Chạy server
```bash
python manage.py runserver
```

Truy cập: `http://127.0.0.1:8000`

**Admin panel**: `http://127.0.0.1:8000/admin`

## 📷 Một số tính năng nổi bật

- Hệ thống phân loại sản phẩm linh hoạt (Category/Sub-category)
- Custom User Model
- Giỏ hàng sử dụng Session
- Upload và hiển thị hình ảnh sản phẩm
- Giao diện quản trị mạnh mẽ của Django

## 🔧 Cải tiến có thể thực hiện

- Thanh toán online (VNPay, Momo, PayPal)
- Xác thực OTP
- Review & đánh giá sản phẩm
- Gửi email xác nhận đơn hàng
- Deploy lên Heroku / AWS / PythonAnywhere
- Tích hợp REST API (Django REST Framework)

## 👤 Tác giả

**HoangQuyCoder**
