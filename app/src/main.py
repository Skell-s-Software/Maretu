# Importaciones
import flet as ft
import requests
# import json
# from rich import print

# Texto donde se muestra la respuesta de la API
respuesta: ft.Text = ft.Text(
    "Presiona el boton para realizar la consulta a la API"
)

# Input donde se escribe la URL:PUERTO
url: ft.TextField = ft.TextField(
    label="URL de API a consultar"
)

def consultaHTTP(url: str) -> dict[str] | str | None:
    print(f"URL de API: {url}")
    try:
        respuesta: requests.Response = requests.get(url)
        print(respuesta.content)
    except Exception as e:
        return f"Ocurrio un error al consultar la API: {e}"
    print(respuesta.content.decode("utf-8"))
    return respuesta.content.decode("utf-8")

def actualizarRespuesta(e, page: ft.Page) -> None:
    respuesta.value = f"{consultaHTTP(url.value)}"
    page.update()
    return None

def main(page: ft.Page):
    page.title = "Maretu's Client"
    page.scroll = ft.ScrollMode.ADAPTIVE

    titulo: ft.Text = ft.Text(
        "Maretu's API Test",
        size=24,
        weight=ft.FontWeight.BOLD
    )

    boton: ft.FilledButton = ft.FilledButton(
        text="Filled button",
        expand=True,
        on_click=lambda e: actualizarRespuesta(e, page)
    )

    page.add(
        titulo,
        url,
        boton,
        respuesta
    )

# Iniciar la aplicación Flet
ft.app(target=main)