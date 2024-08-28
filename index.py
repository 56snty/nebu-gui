import flet as ft
from DL import dev_logs_page
from GS import general_settings_page
from Theme import theme_page
from Auth import auth_page  # Correct import

def main(page: ft.Page):

    page.title = "Custom NavigationBar Example"
    page.theme_mode = ft.ThemeMode.DARK  # Set dark mode
    page.bgcolor = ft.colors.BLACK  # Set background color to black

    # Function to load the selected page
    def load_page(index):
        page.controls.clear()  # Clear existing content
        page.add(tab_bar)  # Add the navigation bar
        if index == 0:  # If "Dev Logs" is selected
            dev_logs_page(page)  # Load the Dev Logs page
        elif index == 1:  # If "Auth" is selected
            auth_page(page)  # Load the Auth page
        elif index == 4:  # If "General Settings" is selected
            general_settings_page(page)  # Load the General Settings page
        elif index == 5:  # If "Theme" is selected
            theme_page(page)  # Load the Theme page
        else:
            page.add(ft.Text(f"Content for tab {index}", color=ft.colors.WHITE))  # Placeholder content for other tabs
        page.update()

    # Create a TabBar to simulate the navigation bar
    tab_bar = ft.Tabs(
        selected_index=0,  # Assuming "Dev Logs" is selected by default
        tabs=[
            ft.Tab(text="Dev Logs", icon=ft.icons.CODE),
            ft.Tab(text="Auth", icon=ft.icons.LOCK),  # Auth Tab
            ft.Tab(text="Bots", icon=ft.icons.ANDROID),
            ft.Tab(text="Abuse", icon=ft.icons.WARNING),
            ft.Tab(text="General Settings", icon=ft.icons.SETTINGS),
            ft.Tab(text="Theme", icon=ft.icons.PALETTE),
            ft.Tab(text="Packet Logs", icon=ft.icons.BAR_CHART),
            ft.Tab(text="Proxies", icon=ft.icons.SWITCH_ACCOUNT),
            ft.Tab(text="Bin", icon=ft.icons.DELETE),
        ],
        on_change=lambda e: load_page(e.control.selected_index),
        indicator_color=ft.colors.RED,  # Set indicator color to red
    )

    page.add(tab_bar)
    load_page(0)  # Load "Dev Logs" by default
    page.update()

ft.app(target=main)
