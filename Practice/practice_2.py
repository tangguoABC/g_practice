#!/usr/bin/python
# -*- coding: UTF-8 -*-
# class UnderAge(Exception):
#     pass
# def verify_age(age):
#     if int(age) < 18:
#         raise UnderAge
#     else:
#         print("age:"+str(age))
# # verify_age(23)
# verify_age(17)

class UnderAge(Exception):
    pass


def verify_age(age):
    if int(age) < 18:
        raise UnderAge
    else:
        print('Age: ' + str(age))


# main program
# verify_age(23)  # won't raise exception
verify_age(17)  # will raise exception