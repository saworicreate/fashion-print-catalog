fashion-print-catalog：新PC/新クローン初期セットアップ（WSL）
シェル：WSL(Ubuntu) の bash

権限：通常権限（管理者不要）

ターミナル：開いたままでOK

0)（新PCだけ）WSLが未導入なら
PowerShell（管理者）

powershell
コードをコピーする
wsl --install -d Ubuntu
再起動 → Ubuntu 初期設定（ユーザー作成）

1) WSLに入る
PowerShell（通常権限）または Cursor のターミナルで

powershell
コードをコピーする
wsl -d Ubuntu
2) 作業ディレクトリへ（必要なら好きなパスに変更）
bash
コードをコピーする
mkdir -p /home/sawory/Projects && cd /home/sawory/Projects
3) クローン → 入る
bash
コードをコピーする
git clone https://github.com/saworicreate/fashion-print-catalog.git
bash
コードをコピーする
cd fashion-print-catalog
4) 共有フックを有効化（大容量ミスコミット防止）
bash
コードをコピーする
git config core.hooksPath .githooks
bash
コードをコピーする
chmod +x .githooks/pre-commit
5) 動作確認（読み取り）
bash
コードをコピーする
git status -s
bash
コードをコピーする
git remote -v
6)（任意）フックのテスト（失敗すれば成功）
bash
コードをコピーする
truncate -s 96000000 .tmp_96mb.bin && git add .tmp_96mb.bin && git commit -m "test large file (should fail)"
bash
コードをコピーする
git reset HEAD .tmp_96mb.bin && rm .tmp_96mb.bin
7) 日々の更新（例：動画を埋め込んだHTMLの追加）
bash
コードをコピーする
git add -A
bash
コードをコピーする
git commit -m "update: add new video catalog"
bash
コードをコピーする
git push origin main
8) GitHub Pages の前提
リポジトリ設定はmain / (root) 配信。新PCでも設定は引き継がれる。UI確認のみ：
GitHub → repo → Settings → Pages で main / (root) になっていることを目視。

9) トラブル時の最速リカバリ
汚れた気がしたら削除せず退避→再クローン

bash
コードをコピーする
cd /home/sawory/Projects
bash
コードをコピーする
mv fashion-print-catalog fashion-print-catalog_backup_$(date +%Y%m%d_%H%M%S)
bash
コードをコピーする
git clone https://github.com/saworicreate/fashion-print-catalog.git && cd fashion-print-catalog
bash
コードをコピーする
git config core.hooksPath .githooks && chmod +x .githooks/pre-commit
10) 注意（実務）
100MB超のファイルはGitHubがサーバ側でも拒否（フックでもブロック）。

動画は .mp4（H.264/AAC推奨）、相対パスで埋め込む：
例）<video src="./media/xxxx.mp4" controls></video>

Reactを使う案件は別リポで。ここは静的カタログ専用を維持。

おまけ：CursorでWSLをデフォルトにする（毎回 wsl 入力を省く）
Cursor → Settings → Terminal → Integrated: Default Profile → Ubuntu(WSL) を選択。

