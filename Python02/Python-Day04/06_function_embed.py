def fn_outer():
    print("fn_outer被调用！")

    def fn_inner():
        print("fn_inner被调用！")

    fn_inner()
    fn_inner()
    print('fn_outer调用结束')
    return fn_inner

fn_outer()

print('===================')
fx = fn_outer()
fx()