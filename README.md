# AutoCloser

AutoCloser 是一個簡單的自動進程管理器，允許用户通過配置文件指定需要監控的進程和時間。當到達指定的時間時，該程序將自動終止相應的進程。

## 特性

- 讀取兩個配置文件：`process.config` 和 `time.config`。
- 根據配置文件中的時間自動監控並終止指定的進程。
- 兼容 Windows 系統。

## 安裝

1. 確保您的系統上已安裝 Python 3。
2. 下載或克隆本項目到您的本地計算機。

    ```bash
    git clone https://github.com/yourusername/AutoCloser.git
    ```

3. 導航到項目目錄：

    ```bash
    cd AutoCloser
    ```

## 配置

### 創建配置文件

1. 創建 `process.config` 文件，用於指定要終止的進程名稱。每個進程名稱佔一行。例如：

    ```
    notepad
    calc
    ```

2. 創建 `time.config` 文件，用於指定要檢查的時間。每個時間佔一行，格式為 HH:MM。例如：

    ```
    14:30
    18:00
    ```

## 使用

1. 在管理員權限下運行腳本：

    ```bash
    python auto_closer.pyw
    ```

2. 程序將在後台運行，並會在指定的時間自動終止配置文件中列出的進程。

## 貢獻

歡迎任何形式的貢獻！如果您有改進建議或發現問題，請提交 issue 或 pull request。

## 許可證

此項目採用 Apache 許可證，詳細信息請查看 [LICENSE](LICENSE) 文件。
