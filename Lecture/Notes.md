## lecture2 Function
```python
print(print(1), print(2)) # 思考其输出
```
有用的工具网站：https://pythontutor.com/visualize.html#mode=edit

python整除符号是 //

## lecture3 Control

交互模式 : python -i .\L3_ex.py

doctest

```
PS C:\Users\Sanchez\Desktop\CS61A\CS61A-Assignments\Lecture> python -m doctest .\L3_ex.py
PS C:\Users\Sanchez\Desktop\CS61A\CS61A-Assignments\Lecture> python -m doctest -v .\L3_ex.py
Trying:
    q, r = divide_exact(2026, 10)
Expecting nothing
ok
Trying:
    q
Expecting:
    202
ok
Trying:
    r
Expecting:
    6
ok
1 items had no tests:
    L3_ex
1 items passed all tests:
   3 tests in L3_ex.divide_exact
3 tests in 2 items.
3 passed and 0 failed.
Test passed.

```

当手动修改注释中的内容,将r的输出修改成错的之后:

```
PS C:\Users\Sanchez\Desktop\CS61A\CS61A-Assignments\Lecture> python -m doctest -v .\L3_ex.py
Trying:
    q, r = divide_exact(2026, 10)
Expecting nothing
ok
Trying:
    q
Expecting:
    202
ok
Trying:
    r
Expecting:
    5
**********************************************************************
File "C:\Users\Sanchez\Desktop\CS61A\CS61A-Assignments\Lecture\L3_ex.py", line 8, in L3_ex.divide_exact
Failed example:
    r
Expected:
    5
Got:
    6
1 items had no tests:
    L3_ex
**********************************************************************
1 items had failures:
   1 of   3 in L3_ex.divide_exact
3 tests in 2 items.
2 passed and 1 failed.
***Test Failed*** 1 failures.
```

## Lecture4 Higher-Order Functions
assert 
```
>>> assert 2 > 3, 'That is false'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: That is false
```
本质是函数作为传入参数和返回值的运用，体现了抽象的思想