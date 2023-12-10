from visidata import GuideSheet, vd

class MenuGuide(GuideSheet):
    guide_text = '''# The Menu System

Located at the [:black on 68]very top of the screen[/], it contains a collection of commands organised within submenu trees.

The menu can be navigated both as a standard, clickable GUI menu, and via keystrokes.

To navigate via keystrokes, `Alt+H` will open the **Help** menu, and from there `↑ ↓ → ←` keys can be used to move between submenus.

Additionally, each top-level menu name has a single letter underlined. `Alt+<underlined letter>` will open that menu. For example, `Alt+F` will open the **File** menu.

`{vd.options.disp_menu_more}` indicates a submenu, which can be traversed with the `→` or a mouse-click. The leaf node of every menu tree is a command.

When the cursor is on a command, the menu throws up its [:color_menu_help]helpbox[/]. This contains the description of the command, the keyboard shortcut if available, and its command longname. Clicking on the command in the menu, or pressing `Enter`, will execute the actual command.

`{vd.options.disp_menu_push}` indicates that the command will push a sheet onto sheet stack. `{vd.options.disp_menu_input}` indicates that input will be required for the command.

[:color_menu_spec]Sheet-specific commands[/] will only appear in the menu when that specific sheet type is loaded.

## Options

- {help.options.disp_menu}
- {help.options.disp_menu_fmt}
- {help.options.color_menu}
'''

vd.addGuide('MenuGuide', MenuGuide)
