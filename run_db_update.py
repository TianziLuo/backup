import os
import mysql.connector

def execute_sql_file():
    # 获取桌面路径
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    sql_file_path = os.path.join(desktop_path, "db_update_filtered.sql")

    try:
        # 检查SQL文件是否存在
        if not os.path.exists(sql_file_path):
            print(f"SQL文件不存在: {sql_file_path}")
            return

        # MySQL连接配置（请根据实际情况修改）
        connection = mysql.connector.connect(
            host="127.0.0.1",  # Database host
            port="3308",       # Database port
            user="root",       # Database username
            password="123456"  # Database password
        )

        # 创建游标
        cursor = connection.cursor()

        # 读取SQL文件
        with open(sql_file_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()

        # 将每条SQL语句分割
        sql_statements = sql_script.split(';')

        for statement in sql_statements:
            # 去除多余空格和无效文本
            statement = statement.strip()
            if not statement:
                continue
            try:
                # 执行单条SQL语句
                cursor.execute(statement)
            except mysql.connector.Error as err:
                print(f"SQL语句执行错误: {err}\n错误SQL: {statement}")
            except Exception as e:
                print(f"发生未知错误: {e}\n错误SQL: {statement}")

        # 提交更改
        connection.commit()
        print("SQL脚本执行完成!")

    except mysql.connector.Error as err:
        print(f"MySQL连接错误: {err}")
    except FileNotFoundError:
        print("无法找到SQL文件")
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 关闭游标和连接
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("数据库连接已关闭")

# 主入口
if __name__ == "__main__":
    execute_sql_file()
