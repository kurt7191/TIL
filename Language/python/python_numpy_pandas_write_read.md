# 파이썬,넘파이,판다스 입출력



### python



```python
with open('pdsample/gosu3.txt','wb') as c:
    c.write(b'aaa')
    c.write(b'bbb')
    
```



```python
with open('pdsample/gosu3.txt','rb') as c:
    c.readline()
```



```python
with open('pdsample/gosu3.txt') as c:
    print(c.read())
```



### Numpy



```python
import numpy as np
a = np.arange(5)

#t.npy로 저장이 됨
np.save('pdsample/t', a)

#t.npy 읽어오기
b = np.load('pdsample/t.npy')

```



```python
b = np.array([1,2,3,4,5])
c = np.array([6,7,8,9,10])

np.savez('pdsample/s',b,c)
x = np.load('pdsample/s.npz')
x.files
x['arr_0']
x['arr_1']
```



`savez()` 는 여러 개의 배열을 저장

확장자는 `.npz`  로 저장

x.files로 보니 `arr_0` , `arr_1` 확인 가능



```python
np.loadtxt('pdsample/num.txt', delimiter=',')
```



txt파일 중에 구분자가 `,` 인 값을 delimiter 매개변수로 조정해서 읽어올 수 있음.



### Pandas



```python
import pandas as pd
a =  pd.read_csv('pdsample/num.txt', header = None)

```



읽고



```python
a.to_csv('pdsample/num2.csv',sep=',')
```



csv로 내보내고

구분자를 설정 해줘야한다.



