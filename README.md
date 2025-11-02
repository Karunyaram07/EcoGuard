# EcoGuard

Modern complaint management for municipal/environmental issues with AI-assisted image classification and robust duplicate prevention.

- Flask + SQLAlchemy + MySQL
- AI category suggestions with ResNet50 and zero-shot models
- Duplicate prevention using text fingerprint, image MD5, and perceptual hashing (phash)
- Gamification (points, badges), NGO assignment, email notifications

---

## 1) Prerequisites

- Windows 10/11 (PowerShell)
- Python 3.10–3.12 (64-bit)
- Git
- MySQL Community Server 8.x

Optional (for faster installs): Visual Studio Build Tools on Windows

---

## 2) Install MySQL (Windows)

- Download MySQL Community Server: https://dev.mysql.com/downloads/mysql/
- Install and note the root password
- Open MySQL shell (Command Prompt or PowerShell):

```sql
-- login as root
mysql -u root -p

-- create database
CREATE DATABASE msw CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- (optional) create a dedicated user
CREATE USER 'ecoguard'@'localhost' IDENTIFIED BY 'strong_password_here';
GRANT ALL PRIVILEGES ON msw.* TO 'ecoguard'@'localhost';
FLUSH PRIVILEGES;
```

Note your connection string; examples:
- root: mysql+pymysql://root:YOUR_ROOT_PASSWORD@localhost:3306/msw
- user: mysql+pymysql://ecoguard:strong_password_here@localhost:3306/msw

---

## 3) Clone the repo

```powershell
git clone https://github.com/Karunyaram07/EcoGuard.git
cd EcoGuard
```

---

## 4) Python setup

Create and activate a virtual environment (recommended):

```powershell
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Notes on Torch/TorchVision:
- The requirements list plain `torch` and `torchvision`. If the default wheel fails, install the CPU-only wheel appropriate to your Python/version from https://pytorch.org/get-started/locally/

---

## 5) Configure environment (.env)

Create a `.env` file in the project root with at least:

```env
# Database
SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:YOUR_ROOT_PASSWORD@localhost:3306/msw

# Mail (Gmail example)
MAIL_USERNAME=your_gmail@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_DEFAULT_SENDER=your_gmail@gmail.com
```

Gmail requires an App Password if 2FA is on.

---

## 6) First run

Start the app:

```bash
python main1.py
```

On first request, the app will:
- Create tables (SQLAlchemy `create_all`)
- Seed default badges
- Auto-create an admin user:
  - email: admin@ecoguard.com
  - password: admin123

Visit: http://localhost:5000

---

## 7) Using the app

- User signup/login
- Submit a complaint (image + text + pincode required)
- AI verification and category suggestion happen automatically (best-effort if models available)
- NGO auto-assignment by pincode + category
- Email notifications when AI-verified or status changes

Admin dashboard: http://localhost:5000/admin_dashboard
- View complaints, leaderboards
- Manual assignment to NGOs
- Dedupe Review: http://localhost:5000/admin/dedupe_review
- Backfill hash fields: http://localhost:5000/admin/backfill_hashes?limit=500
- Mark duplicates (sets status=Duplicate, links `duplicate_of`, deducts 5 points)

User “My Complaints”: http://localhost:5000/prcomplaint
- Shows your complaints and earned badges

---

## 8) Duplicate prevention details

Computed at submit time:
- text_fingerprint: normalized SHA1 of title + message + pincode
- image_md5: MD5 of uploaded file
- image_phash: perceptual hash (phash), robust to simple resizes/re-encodes

Duplicate detection checks (within last ~60 days, recent rows):
- Exact text duplicate: same text_fingerprint
- Exact image duplicate: same image_md5
- Near-duplicate image: phash Hamming distance <= 5 (same pincode preferred)

Admin tools:
- Backfill hashes for older rows
- Dedupe review lists candidates by text fingerprint, image MD5, and phash pairs
- Mark duplicate creates link and prevents further status changes on duplicates

---

## 9) Database schema notes

Tables are created automatically, but these columns and indexes are recommended (added by recent migrations/manual SQL):

```sql
ALTER TABLE complaints ADD COLUMN image_md5 VARCHAR(32) NULL;
ALTER TABLE complaints ADD COLUMN image_phash VARCHAR(32) NULL;
ALTER TABLE complaints ADD COLUMN text_fingerprint VARCHAR(40) NULL;
ALTER TABLE complaints ADD COLUMN duplicate_of INT NULL;

CREATE INDEX idx_complaints_image_md5 ON complaints(image_md5);
CREATE INDEX idx_complaints_text_fp  ON complaints(text_fingerprint);
CREATE INDEX idx_complaints_duplicate_of ON complaints(duplicate_of);
```

Uploads:
- Images saved to `static/uploads` (configurable via `UPLOAD_FOLDER`)

---

## 10) Troubleshooting

- Torch/TorchVision install fails on Windows
  - Use CPU-only wheels from PyTorch’s official site matching your Python/OS.

- BuildError: url_for('admin_backfill_hashes')
  - Ensure the route `@app.route('/admin/backfill_hashes')` exists and the server is restarted.

- “duplicate_of column not present” warning
  - Run the SQL in section 9, then restart the server. Mark-duplicate now uses an ORM+raw-SQL fallback to persist.

- ResNet init failed / CLIP zero-shot errors
  - These are optional. App runs without them. Check internet access or install versions compatible with your Python.

- Email not sending
  - Verify `.env` values and that your mail provider allows SMTP; for Gmail, use an App Password.

---

## 11) Development scripts

Common commands (PowerShell):

```powershell
# activate venv
.\.venv\Scripts\Activate.ps1

# install deps
pip install -r requirements.txt

# run app
python main1.py
```

---

## 12) Contributing

- Fork → Branch → PR
- Follow the project’s Python code style and avoid adding secrets to source

---

## 13) Generate locked requirements (Windows, exact versions)

Create a pinned snapshot of your current environment to ensure reproducible installs.

```powershell
.\.venv\Scripts\Activate.ps1
pip freeze | Out-File -Encoding ASCII requirements.lock.txt
```

Use the lock file for deployments:
```powershell
pip install -r requirements.lock.txt
```

Note: Torch/TorchVision wheels are platform-specific. If your `pip freeze` captures an index URL, keep it or reinstall Torch/TorchVision per https://pytorch.org/get-started/locally/ for the target machine.

---

## 14) License

This project is provided as-is under the repository’s license (see LICENSE if present).

