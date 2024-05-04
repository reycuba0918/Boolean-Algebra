from typing import Any

class my_dictionary(dict):
    def __init__(self, table, *args, **kwargs):
        self.table = table
        self.initialing = True
        self.valid = True
        super().__init__(*args, **kwargs)

    def __setitem__(self, key: Any, value: Any) -> None:
        super().__setitem__(key, value)
        if not self.initialing:
            self.valid = False
            self.table.update_inputs()
    
    def __delitem__(self, value):
        super().__delitem__(value)
        if not self.initialing:
            self.valid = False
            self.table.update_inputs()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        if not self.initialing:
            self.valid = False
            self.table.update_inputs()

    def clear(self) -> None:
        super().clear()
        self.table.update_inputs()
        self.table.make_table()
