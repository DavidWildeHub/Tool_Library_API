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


    def update(self,key,updateName=None,updateCategory=None):
        tool = self.tools.get(key)
        if(tool is None):
            return None
        if updateName is not None:
            tool["name"] = updateName
        if updateCategory is not None:
            tool["category"] = updateCategory
        return tool

    
    def remove(self,key):
        return self.tools.pop(key, None)