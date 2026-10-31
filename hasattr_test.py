class CommandHandler:
    def cmd_start(self):
        print("系统启动中...")

    def cmd_stop(self):
        print("系统停止中...")

    def cmd_help(self):
        print("可用命令: start, stop, help")

    def run(self, command):
        # 拼接方法名
        method_name = f"cmd_{command}"

        # 利用反射查找方法
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            method()
        else:
            print(f"未知命令: {command}")


handler = CommandHandler()
user_input = "start"  # 模拟用户输入
handler.run(user_input)  # 输出: 系统启动中...