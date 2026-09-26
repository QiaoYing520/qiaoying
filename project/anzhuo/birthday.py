import flet as ft


def main(page: ft.Page):
    # 页面基础设置
    page.title = "生日快乐！"
    page.bgcolor = "#2c003e"  # 深紫背景
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 400
    page.window.height = 700

    # 祝福语（可修改名字）
    name = "亲爱的然然"
    wish_text = ft.Text(
        f"祝 {name} 生日快乐！\n愿你岁岁平安，万事胜意！",
        size=28,
        color=ft.colors.PINK_200,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        no_wrap=False
    )

    # 蛋糕图标
    cake_icon = ft.Text("🎂", size=120)

    # 吹蜡烛互动逻辑
    def blow_candle(e):
        cake_icon.value = "🕯️💨"
        wish_text.value = "愿望已许下！\n一定会实现的！✨"
        wish_text.color = ft.colors.YELLOW
        page.bgcolor = "#000000"  # 模拟关灯
        btn.visible = False
        page.update()

    # 按钮样式
    btn = ft.ElevatedButton(
        "点击吹灭蜡烛 🌬️",
        on_click=blow_candle,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PINK_600,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=30)
        )
    )

    # 布局
    page.add(
        ft.Column(
            [
                cake_icon,
                ft.Container(height=30),
                wish_text,
                ft.Container(height=60),
                btn
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)