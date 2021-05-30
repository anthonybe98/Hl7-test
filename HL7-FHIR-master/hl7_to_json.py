from hl7apy.parser import parse_message

def hl7_str_to_json(s, use_long_name=True):

    #s = s.replace("\n", "\r")
    m = parse_message(s)
    return hl7_message_to_json(m, use_long_name=use_long_name)

def hl7_message_to_json(m, use_long_name=True):

    if m.children:
        d = {}
        for c in m.children:
            name = str(c.name).lower()
            if use_long_name:
                name = str(c.long_name).lower() if c.long_name else name
            dic = hl7_message_to_json(c, use_long_name=use_long_name)
            if name in d:
                if not isinstance(d[name], list):
                    d[name] = [d[name]]
                d[name].append(dic)
            else:
                d[name] = dic
        return d
    else:
        return m.to_er7() 

