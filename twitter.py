from collections import OrderedDict

dict = {'1111 dddd' : 3, '1111 bbbb' : 1, '1111 aaaa' : 2, '2222 bbbb' : 3, '2222 aaaa' : 1, '3333 cccc' : 3, '4444 bbbb' : 1}


ordered_dict = OrderedDict (sorted(
        dict.items(), key = lambda k: (
            -int(k[0][:4]), k[0][5:]
        )
    ))


for key in ordered_dict:
    print (ordered_dict._OrderedDict__map[key])