def func1(arg1, arg2):
    if arg2 < arg1:
        var7 = class2()
    else:
        var7 = class4()
    for var8 in xrange(23):
        var9 = var7.func3
        var9(arg1, arg1)
    var53 = var12(arg1, arg2)
    var54 = ((((arg2 | arg2 & (arg2 + (var53 + arg2 - 128)) ^ ((var53 & (var53 - (-992 - arg2) + arg2 - arg1 & (var53 | 892))) ^ arg1) - -1769638392) + (2142672951 | arg1)) - arg2) & -270683359) - var53 ^ var53
    var55 = (var53 - var54) - arg2
    var56 = (var53 - (arg1 ^ arg1)) & ((var55 | arg1 - (arg2 - var53 - (var53 + var55 | ((var55 ^ 650916633) & arg2))) - arg1 - (-427 & var53 + -1193273465)) - arg2 + var53 | arg2) + arg2 ^ 867777346 ^ arg1
    var57 = (var56 + -580540231 + (arg2 ^ (-112 + (var54 & (((arg2 ^ (var53 ^ (var56 - var53) ^ (var56 | 387))) | ((var56 - var55 - var54) - arg1) + arg1) ^ var54 ^ arg1) - (var53 & var56)) | 1362874527))) & var54
    result = 1274266267 | var56 & (var57 - var53)
    return result
def func8(arg13, arg14):
    var42 = func9(arg14, arg13)
    var47 = func12(var42, arg13)
    var51 = func13(arg13, var47)
    if var51 < var51:
        var52 = var42 + arg13
    else:
        var52 = arg13 ^ (((68 - 625353311 + var47 + (arg13 + (var47 - var47)) & var51 ^ var51) & arg13 ^ var47) | var42 | ((-1224184370 - (var47 ^ (arg13 & (var51 ^ arg13 | -2051078950 & arg14) + var42))) & var51 - var47))
    result = -239 + arg13
    return result
def func12(arg43, arg44):
    var45 = 0
    for var46 in range(17):
        var45 += arg43 | var45
    return var45
def func11(arg17, arg18):
    var19 = (820 & arg18) & 33 | -491
    if var19 < arg17:
        var20 = (1789156684 - arg17) | (var19 ^ -324)
    else:
        var20 = 692 + 537679868
    var21 = -646911018 - (arg18 & 483175718) ^ 381
    var22 = arg18 | var19 + var19 & 619287290
    var23 = -1507662860 + arg18
    var24 = arg17 + var21 | var19 ^ 649
    var25 = (23319954 ^ (var19 | var24)) | arg17
    var26 = var21 + var23
    var27 = var19 & 248
    var28 = 403 | (var25 - var23 + var25)
    var29 = arg18 - (var21 - var25)
    var30 = var28 - var24 - var21 - var23
    var31 = arg17 ^ var25 - (arg17 & var28)
    if var23 < var26:
        var32 = (var23 - (arg18 | var26)) & var25
    else:
        var32 = 85 ^ var21
    var33 = (var26 ^ (var27 + var30)) - 1060825635
    var34 = (arg17 | var28) | var26
    var35 = var31 ^ ((-153042942 ^ var26) - 276)
    var36 = var22 + -396
    var37 = (var25 ^ var33) | var19
    var38 = (arg17 ^ var23) | var37
    if arg17 < var37:
        var39 = -891004287 & var35
    else:
        var39 = var37 + var38 & var29
    var40 = var27 - arg18 & var28 & var37
    result = var30 + arg18 & -1358974288
    return result
def func7():
    closure = [9]
    def func6(arg10, arg11):
        closure[0] += func8(arg10, arg11)
        return closure[0]
    func = func6
    return func
var12 = func7()
class class4(object):
    def func3(self, arg5, arg6):
        return 0
class class2(object):
    def func3(self, arg3, arg4):
        result = (0 | (-1509989613 ^ (0 - 538764042)) + (arg4 - arg3)) + 1636583478
        return result
def func9(arg15, arg16):
    def func10(acc, rest):
        var41 = func11(9, acc)
        if acc == 0:
            return var41
        else:
            result = func10(acc - 1, var41)
            return result
    result = func10(10, 0)
    return result
def func13(arg48, arg49):
    def func14(acc, rest):
        var50 = 6 + acc - rest
        if acc == 0:
            return var50
        else:
            result = func14(acc - 1, var50)
            return result
    result = func14(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 15'
    print 'arg_number: 58'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
