from System.Windows.Forms import Clipboard

import rhinoscriptsyntax as rs

__commandname__ = "GetBlockName"


def format_block_names(block_names):
  
  tmp_text = ""
  
  for i in xrange(len(block_names)):
    
    block_name = block_names[i]
    
    if i == 0:
      tmp_text = tmp_text + block_name
    else:
      tmp_text = tmp_text + "\n" + block_name
      
  return tmp_text


def objs_to_block_name(objs):
  
  block_names = []
  
  ### Get Block Name
  for obj in objs:
    
    if rs.IsBlockInstance(obj):
      block_names.append(rs.BlockInstanceName(obj))
  
  ### Remove Duplicate
  block_names_set = list(set(block_names))
  
  ### Sorted
  block_names_set_sorted = sorted(block_names_set)
  
  return block_names_set_sorted


def to_clipboad(block_names):
    
    text_copy = format_block_names(block_names)
    Clipboard.SetText(text_copy)
    
    print(text_copy)


# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
  
  VERSION = "1.0.0.0"
  print("***RUN GetBlockName (ver {})".format(VERSION))
  
  objs = rs.SelectedObjects()
  
  ### Case A
  if len(objs) >= 1:
    
    block_names_set = objs_to_block_name(objs)
    if block_names_set != []:
      to_clipboad(block_names_set)

  ### Case B
  else:
    
    objs_new = rs.GetObjects(message="***Please Select Blocks :")
    ### print(objs_new)
    
    ### to Ignore Case
    ###     - When processing is interrupted (Press ESC key)
    ###     - Not Selected
    
    if objs_new != None:
      block_names_set = objs_to_block_name(objs_new)
      if block_names_set != []:
        to_clipboad(block_names_set)

  
  # you can optionally return a value from this function
  # to signify command result. Return values that make
  # sense are
  #   0 == success
  #   1 == cancel
  # If this function does not return a value, success is assumed
  return 0
