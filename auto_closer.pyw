import os
import time
import datetime
import subprocess

# 读取配置文件中的进程和时间
def read_config():
    process_names = []
    time_points = []

    try:
        with open('process.config', 'r', encoding='utf-8') as f:
            process_names = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print("未找到指定進程配置文件process.config，請修正程序并確保其可用性")

    try:
        with open('time.config', 'r', encoding='utf-8') as f:
            time_points = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print("未找到時間配置文件time.config，請修正程序并確保其可用性")

    return process_names, time_points

def process_exists(process_name):
    """检测进程是否存在"""
    try:
        output = subprocess.check_output(['tasklist'], stderr=subprocess.STDOUT, text=True)
        return process_name in output
    except subprocess.CalledProcessError as e:
        print(f"检查进程时发生错误: {e}")
        return False

def kill_processes(process_names):
    for process_name in process_names:
        if process_exists(f"{process_name}.exe"):
            os.system(f'taskkill /f /im {process_name}.exe')

def main():
    process_names, time_points = read_config()

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time in time_points:
            kill_processes(process_names)
            kill_processes("explorer.exe")
            os.system("start explorer")
            print(f"{current_time}：已殺死指定進程")
            time.sleep(60)  # 等待60秒以避免重复
        time.sleep(1)

if __name__ == "__main__":
    main()