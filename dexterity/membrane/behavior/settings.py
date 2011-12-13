from zope.interface import Interface
from zope import schema

from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.z3cform import layout


class IDexterityMembraneSettings(Interface):
    """ Enables through-the-web configuration of some aspects of the
        dexterity.membrane behaviours.
    """

    local_roles = schema.Set(
        title = u'Local Roles',
        description = u'The list of additional local roles members will be granted in the context of their own profile objects',
        required = True,
        value_type = schema.TextLine(),
        default=set([u'Reader',
                     u'Editor',
                     u'Creator',]))


class DexterityMembraneControlPanelForm(RegistryEditForm):
    schema = IDexterityMembraneSettings


DexterityMembraneControlPanelView = layout.wrap_form(
    DexterityMembraneControlPanelForm, ControlPanelFormWrapper)