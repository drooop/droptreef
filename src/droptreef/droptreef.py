from typing import Any, List, Optional
from flet.core.constrained_control import ConstrainedControl
import flet as ft


class Droptreef(ConstrainedControl):
    def __init__(
        self,
        opacity: Optional[int] = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        left: Optional[int] = None,
        top: Optional[int] = None,
        right: Optional[int] = None,
        bottom: Optional[int] = None,
        nodesdata: Optional[str] = "",
        mywidget: Optional[ft.Control] = None
    ):
        super().__init__(
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )
        self.nodesdata = nodesdata
        self.mywidget = mywidget

    def _get_control_name(self):
        return "droptreef"
    
    def _get_children(self):
        children = []
        if self.mywidget:
            children.append(self.mywidget)  # 添加 mywidget 作为子控件
        return children
        
    @property
    def nodesdata(self):
        # print("nodesdata", self.__testdata)
        return self._get_attr("nodesdata")

    @nodesdata.setter
    def nodesdata(self, value):
        # print("set nodesdata", value)
        self._set_attr("nodesdata", value)
        
    @property
    def mywidget(self) -> Optional[ft.Control]:
        return self.__mywidget

    @mywidget.setter
    def mywidget(self, value: Optional[ft.Control]):
        self.__mywidget = value
