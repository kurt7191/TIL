# ggplot2 연습

> barplot, histogram, boxplot, plot.... etc



### barplot



```R
library(ggplot2)
month <- 1:6
rain <- c(55,50,45,50,60,70)
df <- data.frame(month, rain)
df
#barplot
ggplot(df, aes(x=month,y=rain)) +
  geom_bar(stat='identity', width = 0.7,
           col='red', fill='steelblue')
```





![barPlotTest](C:/Users/user/Desktop/TIL/R/barPlotTest.png)

### histogram



```R
ggplot(iris, aes(x=Petal.Length)) +
  geom_histogram

ggplot(iris, aes(x=Sepal.Width,fill=Species, col = Species))+
  geom_histogram(binwidth = 0.5,position = 'dodge') +
  theme(legend.position = 'bottom')

```



![종류별히스토](C:/Users/user/Desktop/TIL/R/%EC%A2%85%EB%A5%98%EB%B3%84%ED%9E%88%EC%8A%A4%ED%86%A0.png)





fill 에 범주데이터를 넣으면 자동으로 범주데이터에 맞게 색을 분류



### plot



```r
library(tidyverse)
library(showtext)
showtext_auto()
ggplot(iris, aes(Petal.Length,Petal.Width,col=Species)) +
  geom_point(size=3) +
  ggtitle('iris dataset')
```

![종류별산점도](C:/Users/user/Desktop/TIL/R/%EC%A2%85%EB%A5%98%EB%B3%84%EC%82%B0%EC%A0%90%EB%8F%84.png)



#### boxplot



```r
ggplot(iris, aes(y=Petal.Length)) +
  geom_boxplot()
```



![boxplot](C:/Users/user/Desktop/TIL/R/boxplot.png)



### 세계지도



```r
library(maps)

m <- map_data('world')
head(m)
m2 <- m[m$region %in% c('South Korea','North Korea', 'Japan'),]

qplot(long, lat, data=m2, geom='polygon', fill = group,
      group = group)

```

![korJapan](C:/Users/user/Desktop/TIL/R/korJapan.png)



위도와 경도 데이터를 가져와서 사용

`qplot` 함수 사용



