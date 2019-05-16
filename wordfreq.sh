tr '[A-Z]' '[a-z]' < All-MEPs-2014-2019-2018-05-08--2019-05-08.txt | tr -cd '[A-Za-z0-9_ \012]' | tr -s '[ ]' '\012' | sort | uniq -c | sort -nr
