# Importaciones necesarias
import flet as ft
from modules.database import MaretuDataBase
from modules.lecturaEnv import obtenerEnv

def main(page: ft.Page):
    """
    Funcion Principal de Ejecucion
    """
    page.title = "Skell's Maretu"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    MaretuDB: MaretuDataBase = MaretuDataBase(obtenerEnv())
    consulta = ft.TextField(value="", text_align=ft.TextAlign.LEFT, width=None)
    t = ft.Text(value=MaretuDB.Query(consulta.value))

    def query(e):
        t.value = MaretuDB.Query(consulta.value)
        page.update()

    page.add(
        ft.Row(
            [
                consulta,
                ft.IconButton(ft.Icons.ADD, on_click=query),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [t],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

ft.app(main)
