import flet as ft
from DL import update_logs  # Import only update_logs function

def general_settings_page(page: ft.Page):

    # Title Section
    logo = ft.Image(src="images.jpeg", width=100, height=100)  # Placeholder for the logo
    title_text = ft.Text(
        "NebulouS",
        size=40,
        color=ft.colors.RED,
        weight=ft.FontWeight.BOLD,
    )
    subtitle_text = ft.Text(
        "ADMINISTRATOR TOOL",
        size=16,
        color=ft.colors.RED_ACCENT,
        weight=ft.FontWeight.BOLD,
    )

    # Combine logo and title
    title_section = ft.Column(
        [
            logo,
            title_text,
            subtitle_text,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # General Settings Toggles
    moderators_switch = ft.Switch(label="Detect Moderators", value=False, label_style=ft.TextStyle(color=ft.colors.RED))
    script_users_switch = ft.Switch(label="Detect Other Script Users", value=False, label_style=ft.TextStyle(color=ft.colors.RED))
    trace_packets_switch = ft.Switch(label="Trace Packets", value=False, label_style=ft.TextStyle(color=ft.colors.RED))
    auto_save_switch = ft.Switch(label="Auto-Save Config", value=False, label_style=ft.TextStyle(color=ft.colors.RED))

    toggles = ft.Column(
        [
            moderators_switch,
            script_users_switch,
            trace_packets_switch,
            auto_save_switch,
        ],
        spacing=10,
    )

    # Function to handle the Save Config button click
    def save_config(e):
        # Combine the log into a single message
        log_message = (
            "Save Config executed\n"
            f"Detect Moderators: {'ON' if moderators_switch.value else 'OFF'}\n"
            f"Detect Other Script Users: {'ON' if script_users_switch.value else 'OFF'}\n"
            f"Trace Packets: {'ON' if trace_packets_switch.value else 'OFF'}\n"
            f"Auto-Save Config: {'ON' if auto_save_switch.value else 'OFF'}"
        )
        # Log the combined message
        update_logs(log_message)

    # Save Config Button
    save_button = ft.ElevatedButton(
        text="Save Config",
        icon=ft.icons.SAVE,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.RED_ACCENT,
            color=ft.colors.WHITE,
            padding=10,
        ),
        on_click=save_config,  # Link the function to the button click
    )

    # Add everything to the page
    page.add(
        ft.Column(
            [
                title_section,
                ft.Divider(),
                toggles,
                ft.Container(
                    content=save_button,
                    alignment=ft.alignment.center,
                    padding=20,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
