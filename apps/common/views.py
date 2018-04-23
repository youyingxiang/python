from flask import Blueprint,request
from utils.captche.captche import Captcha
bp = Blueprint("common",__name__,url_prefix='/common')



@bp.route('/')
def test():
    c = Captcha()
    code = request.args.get('code')
    print(c.check(code))
    return '123'
    # return c.entry()
    # print(c.imageW)
    # return '123'
@bp.route('/index/')
def test2():
    c = Captcha()
    return c.entry()