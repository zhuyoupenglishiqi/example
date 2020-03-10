#encoding=utf-8
import tkinter
import tkinter.filedialog
from PIL import Image, ImageTk
import requests
import base64
import tkinter.filedialog


def get_access_token(client_id, client_secret):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    # 帮助文档
    # https://ai.baidu.com/docs#/Auth/top
    # 帮助文档中python代码基于python2,本文已经转换为python3x调试通过。
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
    header = {'Content-Type': 'application/json; charset=UTF-8'}
    response1 = requests.post(url=host, headers=header)  # <class 'requests.models.Response'>
    json1 = response1.json()  # <class 'dict'>
    access_token = json1['access_token']

    return access_token


def open_pic2base64():
    # 本地图片地址，根据自己的图片进行修改
    # 打开本地图片，并转化为base64
    root = tkinter.Tk()  # 创建一个Tkinter.Tk()实例
    root.withdraw()  # 将Tkinter.Tk()实例隐藏
    file_path = tkinter.filedialog.askopenfilename(title=u'选择文件')
    f = open(file_path, 'rb')
    img = base64.b64encode(f.read()).decode('utf-8')
    return img


def bd_rec_face(client_id, client_secret):
    # 识别人脸，给出性别、年龄、人种、颜值分数、是否带眼镜等信息
    # 帮助文档中python代码基于python2,本文已经转换为python3x调试通过。

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params = {"image": open_pic2base64(), "image_type": "BASE64",
              "face_field": "age,beauty,glasses,gender,race"}
    header = {'Content-Type': 'application/json'}

    access_token = get_access_token(client_id, client_secret)  # '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token

    request_url = request_url + "?access_token=" + access_token
    response1 = requests.post(url=request_url, data=params, headers=header)
    json1 = response1.json()
    print("性别为", json1["result"]["face_list"][0]['gender']['type'])
    print("年龄为", json1["result"]["face_list"][0]['age'], '岁')
    print("人种为", json1["result"]["face_list"][0]['race']['type'])
    print("颜值评分为", json1["result"]["face_list"][0]['beauty'], '分/100分')
    print("是否带眼镜", json1["result"]["face_list"][0]['glasses']['type'])


def fiel(e):
    selectFileName = tkinter.filedialog.askopenfilename(title='选择文件')  # 选择文件
    e.set(selectFileName)


def showImg(img1):
    try:
        load = Image.open(img1)
    except:
        print("routeError")
        return "routeError"
    render = ImageTk.PhotoImage(load)
    img = tkinter.Label(image=render)
    img.image = render

    img.place(x=0, y=100)


def regimg(img2, l=[]):
    # //识别图片的年龄
    try:
        f = open(img2, 'rb')
    except:
        print('routeError')
        return
    img = base64.b64encode(f.read()).decode('utf-8')
    client_id = 'GvIeCoxnNYW6zup71ZKIn6fA'
    client_secret = 'TYHWWRoCZ605108HXHMM81zIXzeZsUPH'
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params = {"image": img, "image_type": "BASE64",
              "face_field": "age,beauty,glasses,gender,race"}
    header = {'Content-Type': 'application/json'}

    access_token = get_access_token(client_id, client_secret)  # '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token

    request_url = request_url + "?access_token=" + access_token
    response1 = requests.post(url=request_url, data=params, headers=header)
    json1 = response1.json()
    #print("性别为", json1["result"]["face_list"][0]['gender']['type'])

    sex = json1["result"]["face_list"][0]['gender']['type']
    if sex == 'male':
        sex = "男"
    else:
        sex = "女"
    print("性别为", sex)

    age = json1["result"]["face_list"][0]['age']
    print("年龄为", age, '岁')

    race = json1["result"]["face_list"][0]['race']['type']
    print("人种为", race)

    beauty = json1["result"]["face_list"][0]['beauty']+15
    if beauty > 100:
        print('太酷了！已经不是人类该有的颜值了！超100分！')
    else:
        print("颜值评分为", beauty, '分/100分')

    glasses = json1["result"]["face_list"][0]['glasses']['type']
    print("是否带眼镜", glasses)


def Tk():
    tk1 = tkinter.Tk()
    return tk1


def route(top):
    e = tkinter.StringVar()
    e_entry = tkinter.Entry(top, width=68, textvariable=e)
    e_entry.pack()
    return [e, e_entry]


def button(top,  e,  text, l=[]):
    if "选择" in text:
        button1 = tkinter.Button(top, text="选择文件", command=lambda: fiel(e[0]))
    elif "上传" in text:
        e_entry = e[1]
        button1 = tkinter.Button(top, text="上传", command=lambda: showImg(e_entry.get()))
    elif "识别" in text:
        e_entry = e[1]
        button1 = tkinter.Button(top, text="识别图片", command=lambda: regimg(e_entry.get(), l))
    return button1


def route_check(route):
    try:
        load = Image.open(route)
        mess = '路径正确'
    except:
        mess = 'routeError'
    if mess == "routeError":
        return mess

