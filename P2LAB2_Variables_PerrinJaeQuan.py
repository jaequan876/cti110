user_int = int(input('Enter integer (32 - 126):\n'))

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
userfloat = float(input('Enter float:\n'))
userchar = input('Enter character:\n')
userstr = input('Enter string:\n')
print("%d %.2f %s %s" % (user_int, userfloat, userchar, userstr))


# FIXME (2): Output the four values in reverse
print("%s %s %.2f %d" % (userstr, userchar, userfloat, user_int))

# FIXME (3): Convert the integer to a characer, and output that character
print('%d converted to a character is %s' % (user_int, chr(user_int)))
