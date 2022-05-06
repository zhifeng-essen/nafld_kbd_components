import os
import streamlit.components.v1 as components

_RELEASE = True
# _RELEASE = False

component_name = "nafld_kbd_nav"

if not _RELEASE:
    _component_func = components.declare_component(
        component_name,
        url="http://localhost:3000",  # vite dev server port
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(component_name, path=build_dir)

def nafld_kbd_nav(nav_click_time, name=component_name, key=None):
    component_value = _component_func(nav_click_time=nav_click_time, name=name, key=key, default=0)
    return component_value

