import flet as ft
from time import sleep
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello', ['Hello!', 'Hi there!', 'Greetings!']),
    (r'how are you', ['I am good, thank you!', 'I am fine. How can I assist you?']),
    
    (r'What programs/majors does the college offer?', ['Our college offers a wide range of programs and majors, including business, engineering, arts and humanities, sciences, social sciences, and more. You can explore the complete list on our website.']),
    (r'What is the admission process like?', ['The admission process involves submitting an online application, providing supporting documents, such as transcripts and test scores, and paying the application fee. After that, applications are reviewed by our admissions committee.']),
    (r'What are the admission requirements?', ['Admission requirements typically include a completed application form, high school transcripts, standardized test scores (e.g., SAT or ACT), letters of recommendation, and a personal statement or essay. Please check our website for specific requirements for each program.']),
    (r'Is there an application deadline?', ['Yes, we have specific application deadlines for each admission cycle. The deadlines can be found on our website. We encourage you to submit your application before the deadline to ensure full consideration.']),
    (r'How can I schedule a campus tour or visit?', ['To schedule a campus tour or visit, please visit our website and navigate to the "Visit Us" section. You will find options to schedule a tour or attend an open house event.']),
    (r'Are there any scholarships or financial aid available?', ['Yes, we offer scholarships and financial aid options to eligible students. Our financial aid office can provide you with information on scholarships, grants, work-study programs, and loans. We encourage you to explore the financial aid section on our website and contact our office for further assistance.']),
    
    (r'How do I apply to the college?', ['You can apply to our college by visiting our website and completing the online application form. The application portal will guide you through the process and provide instructions for submitting supporting documents.']),
    (r'Is there an online application portal?', ['Yes, we have an online application portal that allows you to submit your application, upload documents, and track the status of your application.']),
    (r'Are there any application fees?', ['Yes, there is an application fee for submitting your application. The fee amount and payment instructions can be found on our website or within the online application portal.']),
    (r'What documents are required for the application?', ['The typical documents required for the application include high school transcripts, standardized test scores, letters of recommendation, and a personal statement or essay. Please refer to our website or the application portal for detailed document requirements.']),
    (r'Can I submit additional materials, such as a portfolio or recommendation letters?', ['Yes, in some cases, additional materials like portfolios or extra recommendation letters may be accepted. Please review the program-specific requirements on our website or contact our admissions office for further guidance.']),
    (r'How can I check the status of my application?', ['You can check the status of your application by logging into the online application portal. There, you will find updates regarding the receipt of documents and the review process. You may also receive notifications via email.']),

    (r'What GPA or test scores are required for admission?', ['The GPA and test score requirements for admission vary depending on the program and level of study. Generally, we look for a competitive GPA and standardized test scores, but we also consider other factors such as extracurricular activities and personal achievements. Please refer to our website or contact our admissions office for specific admission criteria for your desired program.']),
    (r'Are there any specific course requirements for certain programs?', ["Yes, some programs may have specific course requirements or prerequisites. These requirements can be found on our website or within the program descriptions. It's essential to review the program-specific requirements to ensure you meet all the necessary criteria."]),
    (r'Do you consider extracurricular activities and community service?', ['Yes, we value extracurricular activities and community service as they demonstrate your involvement, leadership, and commitment outside of academics. Your participation in these activities will be considered during the admission evaluation process.']),
    (r'Are there any specific admission criteria for international students?', ['International students follow a similar admission process as domestic students, but there may be additional requirements, such as demonstrating English language proficiency through exams like TOEFL or IELTS. Please visit our website or contact our international admissions office for detailed information.']),

    (r'What is the campus like?', ['Our campus provides a vibrant and inclusive environment with state-of-the-art facilities, modern classrooms, research labs, libraries, recreational areas, and student support services. It offers a blend of academic, social, and cultural experiences.']),
    (r'Are there on-campus housing options?', ['Yes, we offer on-campus housing options for students. Our residential facilities provide a comfortable and supportive living environment, fostering community engagement and convenience. Availability and details can be found on our website.']),
    (r'What are the dining facilities like?', ['Our campus has various dining facilities offering a wide range of cuisines and dining options, including cafeterias, food courts, and specialty dining areas. We strive to accommodate diverse dietary preferences and provide a satisfying dining experience for all students.']),
    (r'What extracurricular activities or clubs are available?', ['We have a vibrant array of extracurricular activities and clubs to cater to diverse interests, including academic, cultural, artistic, athletic, and service-oriented organizations. Students can explore these opportunities during their time at the college.']),
    (r'Are there any sports teams or fitness facilities?', ['Yes, we have sports teams that compete in intercollegiate sports. Additionally, our campus provides fitness facilities, such as gyms, sports fields, and recreational centers, where students can engage in various physical activities.']),
    (r'How can I get involved in student organizations?', ['Getting involved in student organizations is easy. We have a dedicated office for student involvement that can provide information about different clubs and organizations on campus. They can guide you on how to join and participate in the groups that align with your interests.']),
    
    # (r'', ['']),
]

chatbot = Chat(patterns, reflections)

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
            response = chatbot.respond(new_message.value)
            new_message.value = ""
            if response:
                # p = ChatMessage("ROBO", response)
                # chat.controls.append(p)
                chat.controls.append(ft.Text(response, weight="bold"))
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