import json
import flet as ft
from droptreef import Droptreef


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    nodes_data = [
        {
            "value": "工作区AA",
            "children": [
                {
                    "value": "PIC1-1",
                    "children": [
                        {
                            "value": "VN1-1-1",
                            "children": None,
                            "url": "https://example.com/pic1-1-1"
                        },
                        {
                            "value": "VN1-1-2",
                            "children": None,
                            "url": "https://example.com/pic1-1-2"
                        },
                        {
                            "value": "VN1-1-3",
                            "children": None,
                            "url": "https://example.com/pic1-1-3"
                        }
                    ],
                    "url": None,
                }
            ],
            "url": None,
        },
        {
            "value": "工作区2",
            "children": [
                {
                    "value": "PIC2-1",
                    "children": [
                        {
                            "value": "VN2-1-1",
                            "children": None,
                            "url": "https://example.com/pic2-1-1"
                        },
                        {
                            "value": "VN2-1-2",
                            "children": None,
                            "url": "https://example.com/pic2-1-2"
                        }
                    ],
                    "url": None,
                }
            ],
            "url": None,
        },
    ]

    nodes_widgets = [
        {
            "widget": ft.Text("工作区1"),
            "children": [
                {
                    "widget": ft.Text("PIC1-1"),
                    "children": [
                        {
                            "widget":ft.Button(text="VN1-1-1", on_click=lambda: print("VN1-1-1 clicked")),
                            "children": None
                        },
                        {
                            "widget":ft.Button(text="VN1-1-2", on_click=lambda: print("VN1-1-2 clicked")),
                            "children": None
                        }
                    ]
                }
            ]
        },
        {
            "widget": ft.Text("工作区2"),
            "children": [
                {
                    "widget": ft.Text("PIC2-1"),
                    "children": [
                        {
                            "widget":ft.Button(text="VN2-1-1", on_click=lambda: print("VN1-1-1 clicked")),
                            "children": None
                        },
                        {
                            "widget":ft.Button(text="VN2-1-2", on_click=lambda: print("VN1-1-2 clicked")),
                            "children": None
                        }
                    ]
                }
            ]
        }
    ]
    
    my_widget = ft.Text("This is a custom widget", size=20)

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.PURPLE_200,
            content=Droptreef(
                nodesdata=json.dumps(nodes_data),
                mywidget=my_widget
            ),

        )
    )


ft.app(main)
