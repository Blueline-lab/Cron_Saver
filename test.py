from filecmp import dircmp 


a = dircmp("test1", "test2")
print(a.report())