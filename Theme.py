# Theme.py

import flet as ft

def theme_page(page: ft.Page):
    # Title Section
    title_text = ft.Text(
        "Customize Theme",
        size=30,
        color=ft.colors.WHITE if page.theme_mode == ft.ThemeMode.DARK else ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
    )

    # Theme Mode Toggle (Light/Dark letters stay red)
    theme_mode_toggle = ft.Switch(
        label="Switch lights",
        value=page.theme_mode == ft.ThemeMode.DARK,
        label_style=ft.TextStyle(color=ft.colors.BLUE if page.theme_mode == ft.ThemeMode.DARK else ft.colors.RED),
        on_change=lambda e: toggle_theme_mode(e, page)
    )

    # Add everything to the page
    page.add(
        ft.Column(
            [
                title_text,
                theme_mode_toggle,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()

# Function to toggle theme mode
def toggle_theme_mode(e, page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK if e.control.value else ft.ThemeMode.LIGHT
    # Update page background and text color based on theme
    page.bgcolor = ft.colors.BLACK if page.theme_mode == ft.ThemeMode.DARK else ft.colors.WHITE
    for control in page.controls:
        if isinstance(control, ft.Text):
            control.color = ft.colors.WHITE if page.theme_mode == ft.ThemeMode.DARK else ft.colors.BLACK
    page.update()