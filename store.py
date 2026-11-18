class ToolStore:

    def __init__(self):
        self.next_id = 1
        self.tools = {}

    def add(self, tool_name,category):
        tool = {"id":self.next_id, "name":tool_name,"category":category}
        self.tools[self.next_id] = tool
        self.next_id += 1
        return tool

    def get_all(self):
        return list(self.tools.values())


    def get(self, key):
        return self.tools.get(key)


    def update(self,key):
        self.
        tool = ts.get(key)
        if(tool == 0):
            return None
        else:
            return tool

    def remove():
        a