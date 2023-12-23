from visidata import vd, Sheet

@Sheet.api
def hint_rename_col(sheet):
    if vd.cleanName(sheet.cursorCol.name) != sheet.cursorCol.name:
        return 5, f"[:hint]The current column can't be used in an expression because [:code]{sheet.cursorCol.name}[/] is not a valid Python identifier. [:onclick rename-col]Rename the column[/] with `^`.[/]"


Sheet.addCommand('^', 'rename-col', 'vd.addUndoColNames([cursorCol]); cursorCol.name = editCell(cursorVisibleColIndex, -1, value=cleanName(cursorCol.name))', 'rename current column')
Sheet.addCommand('z^', 'rename-col-selected', 'updateColNames(selectedRows or [cursorRow], [sheet.cursorCol], overwrite=True)', 'rename current column to combined contents of current cell in selected rows (or current row)')
Sheet.addCommand('g^', 'rename-cols-row', 'updateColNames(selectedRows or [cursorRow], sheet.visibleCols)', 'rename all unnamed visible columns to contents of selected rows (or current row)')
Sheet.addCommand('gz^', 'rename-cols-selected', 'updateColNames(selectedRows or [cursorRow], sheet.visibleCols, overwrite=True)', 'rename all visible columns to combined contents of selected rows (or current row)')


vd.addMenuItems('''
    Column > Rename > current column > rename-col
    Column > Rename > from selected cells > current column > rename-col-selected
    Column > Rename > from selected cells > unnamed columns > rename-cols-row
    Column > Rename > from selected cells > all columns > rename-cols-selected
''')