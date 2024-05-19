import flet as ft
from response_generator import Response
from input_handler import InputHandler

class ChatMessage(ft.Row):
    def __init__(self, user_name: str, text: str):
        super().__init__()
        self.vertical_alignment="start"
        self.controls=[
                ft.CircleAvatar(
                    content=ft.Text(self.get_initials(user_name)),
                    color=ft.colors.WHITE,
                    bgcolor=self.get_avatar_color(user_name),
                ),
                ft.Column(
                    [
                        ft.Text(user_name, weight="bold"),
                        ft.Text(text, selectable=True),
                    ],
                    tight=True,
                    spacing=2,
                    expand=True,
                ),
            ]

    def get_initials(self, user_name: str):
        return user_name[:1].capitalize()

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]

def main(page: ft.Page):
    page.horizontal_alignment = "stretch"
    page.title = "Virtual Chat Box"
    response = Response()
    input_handler = InputHandler()

    def join(e):
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        else:
            user_name = join_user_name.value
            page.dialog.open = False
            new_message.prefix = ft.Text(f"{user_name}: ")
            page.update()

    def send_message_click(e):
        if new_message.value != "":
            m = ChatMessage(join_user_name.value, new_message.value)
            chat.controls.append(m)
            corrected_input = input_handler.get_corrected_input(new_message.value)
            response_text = response.generate_response(corrected_input)
            new_message.value = ""
            if response_text:
                # p = ChatMessage("ROBO", response)
                # chat.controls.append(p)
                chat.controls.append(ft.Text(response_text, weight="bold"))
            else:
                chat.controls.append(ft.Text(f"Sorry {join_user_name.value}, I can't Understand what you are saying!", weight="bold"))
            page.update()

    join_user_name = ft.TextField(
        label="Enter your name",
        autofocus=True,
        on_submit=join,
    )

    dlg = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.ElevatedButton(text="Lets Chat", on_click=join)],
        actions_alignment="end",
    )

    def open_dlg(e):
        if join_user_name.value == "":
            page.dialog = dlg
            dlg.open = True
            page.update()

    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    new_message = ft.TextField(
        hint_text="Ask a Question...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
        on_focus=open_dlg,
    )

    page.add(
        ft.Container(
            content=chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.icons.SEND_ROUNDED,
                    tooltip="Send message",
                    on_click=send_message_click,
                ),
            ]
        )
    )

ft.app(target=main)