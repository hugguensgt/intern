# intern

## 環境構築とサーバー起動
### 前提条件
- **Python 3.x**
- **Git**
---

###  環境構築

**1. プロジェクトのクローン:**
```bash
git clone git@github.com:hugguensgt/intern.git
cd intern
```
**2. 仮想環境の作成:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### サーバーの起動

```bash
cd backend\Healthcheck Endpoint
python server.py
```
実行後、ブラウザまたはPostmanで http://localhost:8000/api/health のURLにアクセスして
{"status": "ok"}の結果と表示されると完了。