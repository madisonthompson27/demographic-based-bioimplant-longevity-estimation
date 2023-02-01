"""
Code template for creating a GUI using bpy. Importing buttons, dropdown menus, checkboxes, sliders, inputs, and misc. values. 
"""

#importing bpy for usage in dot notation
import bpy

#importing needed properties to define values
from bpy.props import (StringProperty, BoolProperty, IntProperty, FloatProperty, EnumProperty, FloatVectorProperty, IntVectorProperty, PointerProperty)


from bpy.types import (Panel, Operator, Menu, PropertyGroup, AddonPreferences)

#import collections
#import importlib

#import mathutils
#import math


#StringProperty : character inputs, filepaths
#BoolProperty : checkboxes
#IntProperty // FloatProperty : sliders
#EnumProperty : dropdown menu
#FloatVectorProperty // IntVectorProperty : misc. values


##TEMPLATE FOR DOC HEADERS##
bl_info = {
    "name": "",
    "description": "",
    "author": "",
    "version": (0, 0, 0),
    "blender": (2, 80, 0),
    "location": "",
    "warning": "", # used for warning icon and text in addons panel
    "category": ""
}


##LABELS FOR USAGE WHEN PACKAGE IS IMPORTED##
addon_name = __name__ #used when the file is executing independently
#addon_name = __package__ #when used as module


##DEFAULT ADD ON SETTINGS##
def _update_panel_fnc (self, context):
    
    #generates custom preferences for each variable call
    print( addon_name, ': update pref.panel function called' )

    main_panel =  ObjectPanel
    
    main_panel.bl_category = context.preferences.addons[addon_name].preferences.tab_label
    # re-register for update 
    unregister(main_panel)
    register(main_panel)


class PREFS_PT_MyPrefs(AddonPreferences):
    ''' Custom Addon Preferences Panel - in addon activation panel -
    menu / edit / preferences / add-ons  
    '''
    
    bl_idname = addon_name
    
    tab_label: StringProperty(
            name="Tab Label",
            description="Choose a label-name for the panel tab",
            default="New Addon",
            update=_update_panel_fnc
    )

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col = row.column()
        col.label(text="Tab Label:")
        col.prop(self, "tab_label", text="")



#custom panel for adding preferences (activates panel):
    #location: menu/edit/preferences/add-ons
class PanelSettings(AddonPreferences):
    
    #name of addon 
    bl_idname = addon_name
    
    #label for tabs in custom menu
    tab_label: StringProperty(
            name="Tab Label",
            description="Choose a label-name for the panel tab",
            default="New Addon",
            update=_update_panel_fnc
            )

    #packing and placing widgets
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col = row.column()
        col.label(text="Tab Label:")
        col.prop(self, "tab_label", text="")


##CLASS FOR DEFAULT PROPERTIES, SIMILAR TO TKINTER##
class defaultParams(PropertyGroup):

    ##TEMPLATE FOR CHARACTER INPUTS AND FILE PATHS##
    default_string : StringProperty(
        name = "default label",
        description= "describe entry field",
        default = "", #prevents accidental activations
        maxlen = 1000 #maximum num of chars
    )

    ##TEMPLATE FOR LABELING A DIRECTORY##
    default_path: StringProperty(
        name = "Directory",
        description="Choose a directory: ",
        default="",
        maxlen=1000,
        subtype='DIR_PATH'
    )


    ##TEMPLATE FOR CHECKBOXES##
    default_bool : BoolProperty(
        name = "this or that",
        description= "Select an option",
        default = False
    )


    ##TEMPLATE FOR SLIDERS##
    default_slider : IntProperty( #could also use float property
        name = "slider name",
        description= "describe quantities measured by slider",
        default = 0,
        min = 0,
        max = 20
    )


    ##TEMPLATE FOR DROPDOWN MENUS##
    default_dropdown: EnumProperty(
        name="Dropdown menu ",
        description="Populate menu options",
        items=[ ('OP1', "Option 1", ""),
                ('OP2', "Option 2", ""),
                ('OP3', "Option 3", ""),]
        )

    ##TEMPLATE FOR DEFAULT FLOAT VECTOR##
        #can also be used for normal vector
    default_float_vector : FloatVectorProperty(
        name = "value",
        description="Enter vector quantities",
        default=(0.0, 0.0, 0.0), 
        min= 0.0, # float
        max = 0.1
        ) 
    
    ##TEMPLATE FOR FLOAT VALUES##
    default_float : FloatProperty(
        name = "Float Value",
        description = "purpose of float",
        default = 23.7,
        min = 0.01,
        max = 30.0
        )


##TEMPLATE FOR RENDERING OBJECTS### 
    #uses bpy import
verts = [(0, 0, 0), (0, 2, 0), (2, 2, 0), (2, 0, 0), (0, 0, 2), (0, 2, 2), (2, 2, 2), (2, 0, 2)]

faces = [(0, 1, 2, 3), (7, 6, 5, 4), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 9)]

mesh = bpy.data.meshes.new("Plane")
object = bpy.data.objects.new("Plane", mesh)

bpy.context.collection.objects.link(object)

mesh.from_pydata(verts,[],faces)

mesh.update(calc_edges=True)


##TEMPLATE FOR OPERATORS##
class WM_OT_HelloWorld(Operator):
    bl_label = "Print Values Operator"
    bl_idname = "wm.hello_world"

    def execute(self, context):
        scene = context.scene
        tool = scene.tool

        # print the values to the console
        print("bool state:", tool.default_checkboxes)
        print("string value:", tool.default_string)
        print("path value:", tool.default_path)
        print("slider value:", tool.default_slider)
        print("dropdown state:", tool.default_dropdown)
        print("vector value:", tool.default_float_vector)
        print("float value:", tool.default_float)

        return {'FINISHED'}


##TEMPLATE FOR CUSTOM MENUS##
class CustomMenu(bpy.types.Menu):
    bl_label = "Select"
    bl_idname = "custom_menu"

    def draw(self, context):
        layout = self.layout

        #built-in operators
        layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        layout.operator("object.select_random", text="Random")


##TEMPLATE FOR PANEL THAT APPEARS WHEN IN OBJECT MODE##
class ObjectPanel(Panel):
    
    #default settings and system view parameters
    bl_label = "Object Panel"
    bl_idname = "object_panel"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "Tools"
    bl_context = "objectmode"   


    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "my_bool")
        layout.prop(mytool, "my_enum", text="") 
        layout.prop(mytool, "my_int")
        layout.prop(mytool, "my_float")
        layout.prop(mytool, "my_float_vector", text="")
        layout.prop(mytool, "my_string")
        layout.prop(mytool, "my_path")
        layout.operator("wm.hello_world")
        layout.menu(CustomMenu.bl_idname, text="Presets", icon="SCENE")
        layout.separator()


##TEMPLATE FOR REGISTERING CLASSES TO ALLOW CODE TO RUN##
classes = (
    defaultParams,
    WM_OT_HelloWorld,
    CustomMenu,
    ObjectPanel
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.my_tool = PointerProperty(type=defaultParams)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()