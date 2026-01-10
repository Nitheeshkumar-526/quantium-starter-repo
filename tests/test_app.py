from app import app
from dash import html, dcc

def find_component(component, component_type, component_id):
    if isinstance(component, component_type):
        if component.id == component_id:
            return True

    if hasattr(component, "children"):
        children = component.children
        if isinstance(children, list):
            for child in children:
                if find_component(child, component_type, component_id):
                    return True
        else:
            return find_component(children, component_type, component_id)

    return False


def test_header_is_present():
    assert find_component(
        app.layout,
        html.H1,
        "app-header"
    )


def test_visualisation_is_present():
    assert find_component(
        app.layout,
        dcc.Graph,
        "sales-line-chart"
    )


def test_region_picker_is_present():
    assert find_component(
        app.layout,
        dcc.RadioItems,
        "region-selector"
    )
