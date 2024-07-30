from flask import render_template

font_tag_start = '<font style="color:rgb(17, 153, 231)">'
font_tag_end ='</font>'

def make_html_highlight(string:str,lighted_words:list) -> str:
    new_str_list = string.split(" ")
    result = ""
    lighted_words = set(lighted_words)
    for i in new_str_list:
        if i in lighted_words:
            result = result + font_tag_start + i + font_tag_end 
        else:
            result += i 
        result += " "
    return result

def list_2_html_str(items:list) -> str:
    result = ""
    for i in items:
        result = result + font_tag_start + i + font_tag_end
        if i == items[-1]:
            break
        result = result + '<font style="color:whitesmoke">' + ", " + "</font>"
    return render_template(result)