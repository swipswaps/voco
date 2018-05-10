




#
# Parser rules implementation
#


XDO_TOOL = '/usr/bin/xdotool'

def r_type_character(variables,context):
    # "SIGNATURE": ["CHARACTER"],

    char = variables[0]

    return [XDO_TOOL,"key",char]


def r_type_uppercase_character(variables,context):
    # "SIGNATURE": ["CHARACTER"],
    char = variables[1].upper()

    return [XDO_TOOL,"key",char]



def r_modifier_single(variables,context):
    # "SIGNATURE": ["MODIFIER","CHARACTER"],


    mod = variables[0]
    char = variables[1]

    return [XDO_TOOL,"key",mod + "+" + char]

def r_modifier_double(variables,context):
    # "SIGNATURE": ["MODIFIER","MODIFIER","CHARACTER"],

    mod1 = variables[0]
    mod2 = variables[1]
    char = variables[2]

    return [XDO_TOOL,"key",mod1 + "+" + mod2 + "+" + char]

def r_switch_application(variables,context):
    # "SIGNATURE": ["ACTION", "APPLICATION"],

    return [XDO_TOOL,"search","--name",variables[1],"windowactivate"]

def r_repeat_movement(variables,context):

    print(variables)
    key_seq = [XDO_TOOL]
    for x in range(0,int(variables[1])):
        key_seq.append("key")
        key_seq.append(variables[0])


    return key_seq


def r_repeat_character(variables,context):

    print(variables)
    key_seq = [XDO_TOOL]
    for x in range(0,int(variables[1])):
        key_seq.append("key")
        key_seq.append(variables[0])


    return key_seq



def r_static_emacs_keys(variables,context):
    print(variables)
    key_seq = [XDO_TOOL]
    for key in variables[0]:
        key_seq.append("key")
        key_seq.append(key)

    return key_seq


def r_emacs_jump_letter(variables,context):

    key_seq = [XDO_TOOL,"key","space","key","j","key","j","key",variables[1]]


    return key_seq


def r_emacs_jump_line_2(variables,context):

    key_seq = [XDO_TOOL]
    for key in variables[1:]:
        key_seq.append("key")
        key_seq.append(key)

    key_seq.append("key")
    key_seq.append("G")

    return key_seq


def r_emacs_jump_line_3(variables,context):

    key_seq = [XDO_TOOL]
    for key in variables[1:]:
        key_seq.append("key")
        key_seq.append(key)

    key_seq.append("key")
    key_seq.append("G")

    return key_seq





def r_test():
    print("Test")
