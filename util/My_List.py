from typing import Any, Iterable, SupportsIndex


class my_list(list):
    def __init__(self, table, *args):
        super().__init__(*args)
        self.table = table

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.table.make_table()

    def __delitem__(self, value):
        super().__delitem__(value)
        self.table.make_table()
    
    def append(self, object: Any):
        super().append(object)
        self.table.make_table()

    def insert(self, index: SupportsIndex, object: Any):
        super().insert(index, object)
        self.table.make_table()
    
    def extend(self, iterable: Iterable):
        super().extend(iterable)
        self.table.make_table()
    
    def clear(self) -> None:
        super().clear()
        self.table.make_table()