import flet as ft
from DL import command_log  # Import the command log list

def auth_page(page: ft.Page):
    # Title Section
    title_text = ft.Text(
        "Login to Continue",
        size=30,
        color=ft.colors.WHITE if page.theme_mode == ft.ThemeMode.DARK else ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
    )

    # Username and Password Fields
    username_input = ft.TextField(label="Username", width=300)
    password_input = ft.TextField(label="Password", password=True, width=300)

    # Output Text to Display Verification Status
    output_text = ft.Text("", color=ft.colors.GREEN if page.theme_mode == ft.ThemeMode.DARK else ft.colors.RED)

    # Login Function
    def login(e):
        username = username_input.value
        password = password_input.value

        # Check credentials
        if username == "Lowkey" and password == "Lowkey123!":
            output_text.value = "Verified"
            output_text.color = ft.colors.GREEN

            # Log the successful login in Dev Logs
            command_log.append(f"User {username} logged in successfully.")  # Append directly to the log list
        else:
            output_text.value = "Invalid credentials"
            output_text.color = ft.colors.RED
        
        page.update()

    # Login Button
    login_button = ft.ElevatedButton(
        text="Login",
        on_click=login,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
        ),
    )

    # Add elements to the page
    page.add(
        ft.Column(
            [
                title_text,
                username_input,
                password_input,
                login_button,
                output_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
