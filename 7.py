test_str = "this is a really big test to know the frequency"

all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
 
print ("Frequency is :\n "+  str(all_freq))
