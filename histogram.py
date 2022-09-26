from collections import Counter
import matplotlib.pyplot as plt
import collections

text = "FPPBEBEJFNQTVUAGDEMHBPHBMPAEBEJFGLDEDQEDJBMDENAGMGQTNPYKPKPBSNADJNAMDENABRABPKBMMNPPPBZBEDHMDSNABHXEAMJFPGPXDEGNFQLGMKRGPUAGDBPGRGNPMBRUJFNGQEKUAGDFPHXMXDNPVPQGNPBERNPHUAGHQJFRMKNPEGZVKEKGGNEKNTGFTUAGDBPEBKZQJFBRQFTBNAEKSDMJQ"

frequencies = Counter(text)
sorted_frequencies = collections.OrderedDict(sorted(frequencies.items()))

plt.bar(list(sorted_frequencies.keys()), sorted_frequencies.values(), color='g')
plt.show()