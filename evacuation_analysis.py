import os
import random

input_txt = os.path.join("evacuation", "evacuation_tweets.txt")
fr = open(input_txt)
output_txt = os.path.join("evacuation", "subset.txt")
fw = open(output_txt, 'a')
total = 27649

select = random.sample(range(total), 100)
for idx, line in enumerate(fr):
    if idx in select:
        print line
        fw.write(line)
fw.close()
fr.close()

    