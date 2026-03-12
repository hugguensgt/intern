### 1. [Python (メニュー管理コンソールアプリ)](./backend/Python)

**概要:** カフェ・飲食店向けのメニュー管理コンソールアプリケーションです。

**アピールポイント:**
- 辞書 (Dictionary) とリストを用いたCRUD処理（追加・更新・削除・検索）の実装。
- `pickle` モジュールによるデータの保存・読み込み機能。

**成果物イメージ:**

**1. 商品追加**

<img width="366" height="360" alt="Screenshot 2026-03-12 230859" src="https://github.com/user-attachments/assets/8053902e-0aa1-45a5-8fcb-47a86a0a9a0d" />

**2. 一覧表示 & 更新**

<img width="371" height="353" alt="Screenshot 2026-03-12 231020" src="https://github.com/user-attachments/assets/382c885a-cc4e-4d04-82b7-e1219d57917e" />

**3. フィルタ・検索・状態変更**

<img width="377" height="400" alt="Screenshot 2026-03-12 231113" src="https://github.com/user-attachments/assets/004a50de-828e-4d6c-ba3a-e1bd88ba26d7" />

**4. 削除 & データ保存**

<img width="380" height="366" alt="Screenshot 2026-03-12 231144" src="https://github.com/user-attachments/assets/04034c84-56f5-4616-a04f-39da5ad06760" />

*(※詳細コードはこちら [Pythonフォルダへ](./backend/Python/app))*

---

### 2. [FastAPI (商品管理API)](./backend/FastAPI)

**概要:** ECサイト向け商品管理システムのRESTful APIです。

**アピールポイント:**
- `SQLModel` (SQLite) を用いた商品のCRUD処理（作成・取得・更新・削除）。
- JWT認証によるログイン機能と、セキュアなAPIエンドポイントの保護。

**成果物イメージ:**

**1. ユーザー登録 (Register)**

<img width="477" height="427" alt="Screenshot 2026-03-12 235722" src="https://github.com/user-attachments/assets/fad67a14-1efd-47bd-b33d-2152297245ad" />

**2. ログイン & JWT認証 (Login)**

<img width="482" height="397" alt="Screenshot 2026-03-12 235858" src="https://github.com/user-attachments/assets/0a718782-f780-42c9-af52-e53bfadd435b" />

**3. データ取得 (GET)**

<img width="476" height="400" alt="Screenshot 2026-03-13 000422" src="https://github.com/user-attachments/assets/1288a740-f7ec-4eb1-802e-aad7a13173df" />

**4. データ登録 (POST)**

<img width="478" height="432" alt="Screenshot 2026-03-13 000526" src="https://github.com/user-attachments/assets/1e939ae2-a759-4d7e-befa-068ed81e87c5" />

**5. データ更新 (PUT)**

<img width="477" height="434" alt="Screenshot 2026-03-13 000635" src="https://github.com/user-attachments/assets/0bbf9926-11f1-4de1-be9d-d03ca6f27c7f" />

**6. データ削除 (DELETE)**

<img width="476" height="280" alt="Screenshot 2026-03-13 000723" src="https://github.com/user-attachments/assets/ef85849c-b158-44a9-9d46-16742743038a" />

*(※詳細コードはこちら [FastAPIフォルダへ](./backend/FastAPI/app))*
