def int_to_roman(arithmos):
   if type(arithmos) != type(1):
      raise TypeError, "expected integer, got %s" % type(arithmos)
   if not 0 < arithmos < 1000000:
      raise ValueError, "Argument must be between 1 and 100000"
   result = ""
   nums = ('/M', '/D', '/C', '/L', '/X', '/V','M', 'D', 'C', 'L', 'X', 'V', 'I')
   ints = (1000000, 500000,100000, 50000, 10000,5000, 1000, 500, 100, 50,  10,  5,   1)
   places = [0,] * len(nums)
   for i in range(len(ints)):
      value = ints[i]
      count = arithmos / value
      places[i] = count
      if count: arithmos -= count * value
   for i in range(len(places)):
      if places[i] < 4:
         result += nums[i] * places[i]
      else:
         if places[i -1] == 0:
            result += nums[i] + nums[i -1]
         else:
            result = result[:-1] + nums[i] + nums[i -2]
   return result

arithmos = input("Dose ena arithmo mexri to 1000000: ")
print int_to_roman(arithmos)
