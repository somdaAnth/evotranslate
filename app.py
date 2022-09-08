
from flask import Flask,render_template,request

app = Flask(__name__,template_folder='template')

@app.route("/evo",methods=['POST','GET'])


def caculate():
    The_dict = {
     'A':'ฤ',
     'a':'ฟ', 
     'B':'ฺ', 
     'b':'ิ', 
     'C':'ฉ', 
     'c':'แ', 
     'D':'ฏ', 
     'd':'ก', 
     'E':'ฎ', 
     'e':'ำ', 
     'F':'โ', 
     'f':'ด', 
     'G':'ฌ', 
     'g':'เ', 
     'H':'็', 
     'h':'้', 
     'I':'ณ', 
     'i':'ร', 
     'J':'๋', 
     'j':'่', 
     'K':'ษ', 
     'k':'า', 
     'L':'ศ', 
     'l':'ส', 
     'M':'?', 
     'm':'ท', 
     'N':'์', 
     'n':'ื', 
     'O':'ฯ', 
     'o':'น', 
     'P':'ญ', 
     'p':'ย', 
     'Q':'๐', 
     'q':'ๆ', 
     'R':'ฑ', 
     'r':'พ', 
     'S':'ฆ', 
     's':'ห', 
     'T':'ธ', 
     't':'ะ', 
     'U':'๊', 
     'u':'ี', 
     'V':'ฮ', 
     'v':'อ', 
     'W':'"', 
     'w':'ไ', 
     'X':')', 
     'x':'ป', 
     'Y':'ํ', 
     'y':'ั', 
     'Z':'(', 
     'z':'ผ', 
     '!':'+', 
     '1':'ๅ', 
     '@':'๑', 
     '2':'/', 
     '#':'๒', 
     '3':'-', 
     '$':'๓', 
     '4':'ภ', 
     '%':'๔', 
     '5':'ถ', 
     '^':'ู', 
     '6':'ุ', 
     '&':'฿', 
     '7':'ึ', 
     '*':'๕', 
     '8':'ค', 
     '(':'ต', 
     '9':'๖', 
     ')':'๗', 
     '0':'จ', 
     '_':'๘', 
     '-':'ข', 
     '+':'๙', 
     '=':'ช', 
     '{':'ฐ', 
     '[':'บ', 
     '}':',', 
     ']':'ล', 
     '|':'ฅ', 
     '\\':'ฃ', 
     ':':'ซ', 
     ';':'ว', 
     '"':'.', 
     "'":'ง', 
     '<':'ฒ', 
     ',':'ม', 
     '>':'ฬ', 
     '.':'ใ', 
     '?':'ฦ', 
     '/':'ฝ'
     }
     
    txt = ''
    if request.method=='POST' and 'txt' in request.form:
        txt = str(request.form.get('txt'))
        trans = txt.maketrans(The_dict)
        txt = txt.translate(trans)
        
    return render_template('index.html', txt = txt)

@app.route('/THtoENG',methods=['POST','GET'])    
def pedo():
    The_dict = {
     'A':'ฤ',
     'a':'ฟ', 
     'B':'ฺ', 
     'b':'ิ', 
     'C':'ฉ', 
     'c':'แ', 
     'D':'ฏ', 
     'd':'ก', 
     'E':'ฎ', 
     'e':'ำ', 
     'F':'โ', 
     'f':'ด', 
     'G':'ฌ', 
     'g':'เ', 
     'H':'็', 
     'h':'้', 
     'I':'ณ', 
     'i':'ร', 
     'J':'๋', 
     'j':'่', 
     'K':'ษ', 
     'k':'า', 
     'L':'ศ', 
     'l':'ส', 
     'M':'?', 
     'm':'ท', 
     'N':'์', 
     'n':'ื', 
     'O':'ฯ', 
     'o':'น', 
     'P':'ญ', 
     'p':'ย', 
     'Q':'๐', 
     'q':'ๆ', 
     'R':'ฑ', 
     'r':'พ', 
     'S':'ฆ', 
     's':'ห', 
     'T':'ธ', 
     't':'ะ', 
     'U':'๊', 
     'u':'ี', 
     'V':'ฮ', 
     'v':'อ', 
     'W':'"', 
     'w':'ไ', 
     'X':')', 
     'x':'ป', 
     'Y':'ํ', 
     'y':'ั', 
     'Z':'(', 
     'z':'ผ', 
     '!':'+', 
     '1':'ๅ', 
     '@':'๑', 
     '2':'/', 
     '#':'๒', 
     '3':'-', 
     '$':'๓', 
     '4':'ภ', 
     '%':'๔', 
     '5':'ถ', 
     '^':'ู', 
     '6':'ุ', 
     '&':'฿', 
     '7':'ึ', 
     '*':'๕', 
     '8':'ค', 
     '(':'ต', 
     '9':'๖', 
     ')':'๗', 
     '0':'จ', 
     '_':'๘', 
     '-':'ข', 
     '+':'๙', 
     '=':'ช', 
     '{':'ฐ', 
     '[':'บ', 
     '}':',', 
     ']':'ล', 
     '|':'ฅ', 
     '\\':'ฃ', 
     ':':'ซ', 
     ';':'ว', 
     '"':'.', 
     "'":'ง', 
     '<':'ฒ', 
     ',':'ม', 
     '>':'ฬ', 
     '.':'ใ', 
     '?':'ฦ', 
     '/':'ฝ'
     }
    TH_TO_ENG_Dict = dict(map(reversed, The_dict.items()))
    txteng = ''
    if request.method=='POST' and 'txteng' in request.form:
        txteng = str(request.form.get('txteng'))
        trans = txteng.maketrans(TH_TO_ENG_Dict)
        txteng = txteng.translate(trans)

    return render_template('indextheng.html', txteng = txteng)    

@app.route('/about')  
def about():

    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)