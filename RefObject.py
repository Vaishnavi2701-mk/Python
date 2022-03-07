#----------------------------------------------------------------------------------------
#	Copyright © 2021 Tangible Software Solutions, Inc.
#	This class can be used by anyone provided that the copyright notice remains intact.
#
#	This class is used to replicate the ability to pass arguments by reference in Python.
#----------------------------------------------------------------------------------------
class RefObject(object):
    def __init__(self, ref_arg):
        arg_value = ref_arg