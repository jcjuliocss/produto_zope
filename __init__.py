"""init do site."""
import minimal2


def initialize(context):
    """site."""
    context.registerClass(
        minimal2.Minimal2,
        constructors=(
            minimal2.manage_add_minimal2_form,
            minimal2.manage_add_minimal2,
        ),
        icon='img/icon.png'
    )
