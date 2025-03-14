Tên: Phan Công Chiến
MSSV: 22685651

# Task Management System

Hệ thống quản lý công việc được xây dựng bằng Django Framework.

## Tính năng

- Đăng ký, đăng nhập người dùng
- Tạo, chỉnh sửa, xóa công việc
- Phân công công việc cho người dùng
- Theo dõi trạng thái công việc
- Upload files đính kèm

## Yêu cầu hệ thống

- Python 3.8+
- pip (Python package installer)

## Cài đặt

1. Clone repository:

```bash
git clone https://github.com/chien24/ptud-gk-de-2.git
cd task_project
```

2. Tạo và kích hoạt môi trường ảo:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Cài đặt dependencies:

```bash
pip install -r requirements.txt
```

4. Thực hiện migrate database:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Tạo superuser:

```bash
python manage.py createsuperuser
```

6. Chạy development server:

```bash
python manage.py runserver
```

## Cấu trúc Project

- `taskapp/`: Ứng dụng quản lý công việc
- `userapp/`: Ứng dụng quản lý người dùng
- `templates/`: Templates chung
- `static/`: Static files (CSS, JS, Images)
- `media/`: User uploaded files

## Sử dụng

1. Truy cập http://localhost:8000
2. Đăng ký tài khoản mới hoặc đăng nhập
3. Bắt đầu tạo và quản lý công việc

## Contributing

Mọi đóng góp đều được hoan nghênh. Vui lòng tạo issue hoặc pull request.
