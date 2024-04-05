import statistics as st
data = [5, 4, 1, 3, 2, 4, 5, 4, 5, 6]
print('Mean: ', st.mean(data)) 
print('Median: ', st.median(data)) 
print('Mode: ', st.mode(data))
print('Variance: ', round(st.variance(data),2)) 
print('Standard Deviation: ', round(st.stdev(data),2))