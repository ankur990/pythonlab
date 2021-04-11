  if str_size % n != 0:
        print "Invalid Input: String size is not divisible by n"
        return
    part_size = str_size/n
    k = 0
    for i in string:
        if k%part_size==0:
            print "\n",
        print i,
        k += 1
