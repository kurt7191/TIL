scores =c(95,96,85,68,58,90,95,70,70,50,
          90,90,90,83,82,95,95,90,65,76,
          86,100,70,90,56,95,93,60,55,59,
          85,95,81,71,41,95,95,91,73,65,
          93,75,90,60,68,90,93,83,58,29)

######1
#1
mean(data1)
#2
median(data1)
#3
mean(data1,0.1)
#4
var(data1)
#5
sd(data1)
#6
min(data1)
#7
max(data1)
#8
range(data1)
#9
quantile(data1, 0.25)
#10
quantile(data1, 0.5)
#11
quantile(data1, 0.75)
#12
IQR(data1)
#13
sd(data1) / mean(data1) * 100

######2

shapiro.test(data1)
