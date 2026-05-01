import os
import time
import subprocess
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class WatcherHandler(FileSystemEventHandler):
  def __init__(self):
    self.last_run_time = 0
    self.cooldown = 1 # 防抖1秒
  def on_modified(self, event):
    # 忽略目录
    if event.is_directory:
       return

    filepath = os.path.abspath(event.src_path)  # 获取文件的绝对路径
    filename = os.path.basename(event.src_path)  # 获取文件名

    # 忽略非.py文件
    if not filename.endswith('.py'):
      return
    
    # 忽略watcher文件
    if filename == 'watchers.py':
      return
    
    # 防抖
    now = time.time()
    if now - self.last_run_time < self.cooldown:
      return
    self.last_run_time = now

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print('\n=======================')
    print(f'🕒 {now_str} | 🚀 文件变更: {filename}')
    print('⚡ 正在执行...\n')

    try:
      result = subprocess.run(['python3', filepath], capture_output=True, text=True)
      if result.stdout:
        print('执行结果:👉' + result.stdout)

      if result.stderr:
        print('错误信息:👉' + result.stderr)
    except Exception as e:
      print(f'执行失败: {e}')
  
if __name__ == "__main__":
  path = "."
  event_handler = WatcherHandler()
  observer = Observer()
  observer.schedule(event_handler, path, recursive=True)
  observer.start()

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()
