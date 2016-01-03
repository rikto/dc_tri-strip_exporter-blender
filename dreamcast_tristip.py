bl_info = {
            "name" : "Triangle-strip exporter for the PVR2 graphic processor (Dreamcast)",
            "description": "Should export Blender geometry to triangle-strips. Written specially for the legacy PVR2 processor powering Dreamcast console.",
            "category" : "Import-Export",
            "author" : "Dev",
            "blender": (2, 76, 0),
            "location": "File > Export > Dreamcast (.3dc)",
            "warning": "Very early work. Save your scene before running.",
            }

#You may see bits and pieces of other Blender exporters
import bpy
from bpy.props import StringProperty, EnumProperty, BoolProperty
import os
import mathutils

def menu_func(self, context):
        #Adds this script to the list in the Export menu
        self.layout.operator(triStripMenu.bl_idname, text="Dreamcast (.3dc)")
        
def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_export.append(menu_func)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_export.remove(menu_func)

if __name__ == "__main__":
    register()



def execute(self, context):
    
    config = {
            
            

            self.layout.operator("mesh.primitive_monkey_add")

            #layout.operator("objec.duplicate_move")     
        
     }
     
     
     
class triStripMenu(bpy.types.Operator):
        bl_idname = "export.3dc"
        bl_label = "Export for DC"
        filepath = StringProperty(subtype='FILE_PATH')
        
            