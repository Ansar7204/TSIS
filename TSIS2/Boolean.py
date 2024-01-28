
#False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0 

myobj = myclass()
print(bool(myobj))



#True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


x = 200
print(isinstance(x, int))