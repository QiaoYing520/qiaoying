import flet as ft

def main(page: ft.Page):
    # 添加一行居中的文字
    page.add(ft.Text("Hello, Flet!", size=30, color="blue"))

ft.app(target=main)