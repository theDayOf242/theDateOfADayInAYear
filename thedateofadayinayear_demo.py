import thedateofadayinayear
import day242, day101, day42

if __name__ == '__main__':
    print("== Generic days")
    print(thedateofadayinayear.dateofdayinyear())
    print(thedateofadayinayear.dateofdayinyears(2022, 4))
    print(thedateofadayinayear.dateofdayinyears(2021, 4, 200))
    print(thedateofadayinayear.dateofdayinyears(2021, 10, 201))
    print("== Front days")
    print(day242.dayofyears(2021, 4))
    print("== DM days")
    print(day101.dayofyears(2021, 4))
    print("== Towel days")
    print(day42.dayofyears(2021, 4))