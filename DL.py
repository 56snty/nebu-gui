import flet as ft

# Shared list to keep track of executed commands
command_log = []

def update_logs(command):
    command_log.append(command)

def dev_logs_page(page: ft.Page):
    # Create a column to hold the logs
    log_column = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=10,  # Add spacing between each log entry
    )

    # Function to update the displayed logs
    def refresh_logs():
        log_column.controls.clear()
        for log in command_log:
            log_entry = ft.Container(
                content=ft.Text(f"User 1: {log}", color=ft.colors.WHITE),  # Hardcode "User 1"
                padding=10,
                border_radius=ft.border_radius.all(8),
                bgcolor=ft.colors.GREY_900,  # Background color for each log
            )
            log_column.controls.append(log_entry)
        page.update()

    # Function to clear logs
    def clear_logs(e):
        command_log.clear()
        refresh_logs()

    # Create the Clear button
    clear_button = ft.FloatingActionButton(
        text="Clear Logs",
        icon=ft.icons.CLEAR,
        bgcolor=ft.colors.RED_ACCENT,
        on_click=clear_logs,  # Link the function to the button click
    )

    # Add the Clear button and log column to the page
    page.add(
        ft.Stack(
            [
                log_column,
                ft.Container(
                    content=clear_button,
                    alignment=ft.alignment.bottom_right,
                    padding=20,
                )
            ]
        )
    )

    # Call refresh_logs to ensure the logs are displayed when the page loads
    refresh_logs()

    # Example usage: Log a new command when the Dev Logs page is loaded
    update_logs("Application started")
    refresh_logs()
