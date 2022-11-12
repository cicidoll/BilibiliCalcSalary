from interval import Interval

# 目标流水与对应底薪（可根据自己情况修改）
BASICSALARY: list = [
    { 20000: 2000 },
    { 50000: 5000 },
    { 100000: 10000 },
    { 300000: 30000 },
    { 500000: 50000 },
]

def get_basic_salary(amount: int) -> int:
    """ 获取流水对应的底薪值 """
    # 底薪
    basic_salary: int
    # 最低底薪
    min_basic_salary: int = list(BASICSALARY[0].keys())[0]
    # 最高底薪
    max_basic_salary: int = list(BASICSALARY[len(BASICSALARY)-1].keys())[0]
    if amount < list(BASICSALARY[0].keys())[0]:
        # 流水小于最低底薪，赋值0
        basic_salary = 0
    elif min_basic_salary <= amount < max_basic_salary:
        # 计算流水所在底薪区间
        for i in range(len(BASICSALARY)-1):
            if amount in Interval(
                    list(BASICSALARY[i].keys())[0],
                    list(BASICSALARY[i+1].keys())[0],
                    upper_closed=False):
                # 区间[, ) 赋值底薪
                basic_salary = list(BASICSALARY[i].values())[0]
    elif amount >= max_basic_salary:
        # 流水超出最高底薪
        basic_salary = list(BASICSALARY[len(BASICSALARY)-1].values())[0]
    return basic_salary

def calc_amount_with_tax(amount: int) -> int:
    """ 计算收益(扣税&获取底薪) """
    # 获取底薪
    basic_salary: int = 0
    if amount < 0: return 0
    else:
        basic_salary = get_basic_salary(amount)
    # 扣税
    return int(basic_salary*0.9 + amount * 0.5 * 0.9)
