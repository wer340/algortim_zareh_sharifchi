# note 

#mutable vs  immutable  
```python
a=[1,2,3,4,5,6]
print(id(a))
a=a.append(9)
print(id(a)).
b=a      
c=list(a)   #this id deffrent with a id

```
# class

```python
class Animal:
  pass
  

class Camel(Animal):
  def __init__(self)
    super(Animal,self).__init() #both init run    
```

# time

```python
start = time.time()
for i in range(0, 35):
    print(i)

print(f" start time :{start} and end time : {time.time()}")

```
# skip char   and utf-8

```python
string=r"c:\\users/pc/"
fa_sentance=u"سلام"
print(f"adress={string} and farsi sentance: {fa_sentance} ")
```
