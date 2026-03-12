### 1. [Python (メニュー管理コンソールアプリ)](./backend/Python)

**概要:** カフェ・飲食店向けのメニュー管理コンソールアプリケーションです。

**アピールポイント:**
- 辞書 (Dictionary) とリストを用いたCRUD処理（追加・更新・削除・検索）の実装。
- `pickle` モジュールによるデータの保存・読み込み機能。

**成果物イメージ:**

**1. 商品追加**

<img width="366" height="360" alt="Screenshot 2026-03-12 230859" src="https://github.com/user-attachments/assets/771acfb6-3b3d-476e-b051-49d3ea0c5ec3" />

**2. 一覧表示 & 更新**

<img width="371" height="353" alt="Screenshot 2026-03-12 231020" src="https://github.com/user-attachments/assets/5623535e-44e4-4a55-991a-af55030ee812" />

**3. フィルタ・検索・状態変更**

<img width="377" height="400" alt="Screenshot 2026-03-12 231113" src="https://github.com/user-attachments/assets/2cbb4cec-0b70-4e27-bccd-3b63b7eefa8c" />

**4. 削除 & データ保存**

<img width="380" height="366" alt="Screenshot 2026-03-12 231144" src="https://github.com/user-attachments/assets/f7f94155-9df5-404e-950d-dae165f6f725" />

*(※詳細コードはこちら [Pythonフォルダへ](./backend/Python/app))*

---

### 2. [FastAPI (商品管理API)](./backend/FastAPI)

**概要:** ECサイト向け商品管理システムのRESTful APIです。

**アピールポイント:**
- `SQLModel` (SQLite) を用いた商品のCRUD処理（作成・取得・更新・削除）。
- JWT認証によるログイン機能と、セキュアなAPIエンドポイントの保護。

**成果物イメージ:**

**1. ユーザー登録 (Register)**

<img width="477" height="427" alt="Screenshot 2026-03-12 235722" src="https://github.com/user-attachments/assets/bd539e69-8376-404e-85cf-cf295a7639e8" />

**2. ログイン & JWT認証 (Login)**

<img width="482" height="397" alt="Screenshot 2026-03-12 235858" src="https://github.com/user-attachments/assets/9888cdff-f2f9-428e-904f-a0bc2fb1e84c" />

**3. データ取得 (GET)**

<img width="476" height="400" alt="Screenshot 2026-03-13 000422" src="https://github.com/user-attachments/assets/5a25e740-58c5-4363-860d-8c70489399b6" />

**4. データ登録 (POST)**

<img width="478" height="432" alt="Screenshot 2026-03-13 000526" src="https://github.com/user-attachments/assets/29cff509-9f7b-4b03-bcec-0f8a5da48f41" />

**5. データ更新 (PUT)**

<img width="477" height="434" alt="Screenshot 2026-03-13 000635" src="https://github.com/user-attachments/assets/5c666802-25ee-4b65-a16e-b449be3c5f02" />

**6. データ削除 (DELETE)**

<img width="476" height="280" alt="Screenshot 2026-03-13 000723" src="https://github.com/user-attachments/assets/12c862c7-be06-472b-9316-53b5489cf637" />

*(※詳細コードはこちら [FastAPIフォルダへ](./backend/FastAPI/app))*
