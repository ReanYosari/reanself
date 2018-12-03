# -*- rean_bots.coding: utf-8 -*- 

import REAN
from REAN import *
from RBOTS.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, tweepy, pafy, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl

rean = LineClient(authToken='TOKEN KAMU DISINI')
rean.log("Auth Token : " + str(rean.authToken))

print ("==================== R-BOTS RUNING SUCCES ====================")

poll = LinePoll(rean)
creator = ["u50a276d6b4571941fa524c6cae200cd7"]
owner = ["u50a276d6b4571941fa524c6cae200cd7"]
admin = ["MID KAMU DISINI"]
Captain = rean.getProfile().mid
KAC = [rean]
Bots = [Captain]

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
leavegroup = []
simisimi = []
translateen = []
translatetr = []
translateid = []
translateth = []
translatetw = []
translatear = []

contact = rean.getProfile()
mybackup = rean.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

reanProfile = rean.getProfile()
myProfile["displayName"] = reanProfile.displayName
myProfile["statusMessage"] = reanProfile.statusMessage
myProfile["pictureStatus"] = reanProfile.pictureStatus

msg_dict = {}
msg_dict1 = {}
bl = [""]
settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "detectUnsend":True,
    "changePicture":False,
    "autoJoinTicket":False,
    "reread":False,
    "autoRead":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "protection": {},
    "lang":"JP",
    "addadmin":False,
    "unsendMessage":True,
    "detectUnsend":True,
    "mimic":False,
    "delladmin":False,
    "staff":{},
    "winvite":False,
    "unsend":True,
    "addstaff":False,
    "dellstaff":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "contact":False,
    'autoJoin':False,
    'autoAdd':True,
    'autoCancel':{"on":True,"members": 2},
    'autoLeave':False,
    'autoRead':False,
    'autoLeave1':False,
    "detectMention":False,
    "detectMention1":False,
    "detectMention2":False,
    "detectMention3":False,
    "Mentionkick":False,
    "welcomeOn":True,
    "sticker":False,
    "selfbot":True,
    "mention":"hayoo ngintip -_-",
    "Respontag":"Ada yang bisa saya bantu -_-",
    "welcome":"Selamat datang & semoga betah",
    "comment":"Like like & like by ",
    "Stickermessage":" Ngetag mulu ,q kasih gift tuh ..cek pm -_-",
    "leave":"lah cabut doi, baper x yak 😂",
    "message":"Terimakasih sudah add saya \n my creator http://line/me/ti/p~reanyosari040",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
 
with open('owner.json', 'r') as fp:
    owner = json.load(fp)   
with open('creator.json', 'r') as fp:
    creator = json.load(fp)    
        
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))


def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf-8') as fp:
        json.dump(msg_dict, fp, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)
            time.sleep(0.1)
            page = page[end_content:]
    return items

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        rean.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "✍ Total Sider User[{}]\n✍ Haii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(rean.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        rean.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        rean.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "✍ Total Member Masuk [{}]\n✍ Haii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\n✍ Nama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(rean.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        rean.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        rean.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Keluar「{}」\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nGrup İsmi : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(rean.getGroup(to).name))
                except:
                    no = "\n Success "
        rean.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        rean.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = rean.getAllContactIds()
        gid = rean.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"✍ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n✍ Group : "+str(len(gid))+"\n✍ Teman : "+str(len(teman))+"\n✍ Expired : In "+hari+"\n✍ Version : v1.06\n✍ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n✍ Runtime : \n • "+bot
        rean.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        rean.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = ""
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    rean1 = "╭══════════════════╮" + "\n" + \
                  "     ༺༽།☤ⵓʀᴇᴀɴ-sᴇʟғⵓ☤།༼༻" + "\n" + \
                  "╰══════════════════╯" + "\n" + \
                  "╠╔═════════════════╗" + "\n" + \
                  "║     ๑۩ ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅ ۩๑" + "\n" + \
                  "╠╚═════════════════╝" + "\n" + \
                  "╠🛡 Me" + "\n" + \
                  "╠🛡 Mid @" + "\n" + \
                  "╠🛡 Info @" + "\n" + \
                  "╠🛡 Mymid" + "\n" + \
                  "╠🛡 Mybio" + "\n" + \
                  "╠🛡 Myname" + "\n" + \
                  "╠🛡 Myvid" + "\n" + \
                  "╠🛡 Mycover" + "\n" + \
                  "╠🛡 Getpic @" + "\n" + \
                  "╠🛡 Getcontact @" + "\n" + \
                  "╠🛡 Getname @" + "\n" + \
                  "╠🛡 Getbio @" + "\n" + \
                  "╠🛡 Getmid @" + "\n" + \
                  "╠🛡 Getcover @" + "\n" + \
                  "╠🛡 Ginfo" + "\n" + \
                  "╠🛡 Creator" + "\n" + \
                  "╠🛡 About" + "\n" + \
                  "╠🛡 Self on/off" + "\n" + \
                  "╠🛡 Clearchat" + "\n" + \
                  "╠🛡 Set" + "\n" + \
                  "╠🛡 Sp" + "\n" + \
                  "╠🛡 Runtime" + "\n" + \
                  "╠🛡 Rtime" + "\n" + \
                  "╠🛡 Mygroups" + "\n" + \
                  "╠🛡 Reboot" + "\n" + \
                  "╠🛡 Infomem [ no group ]" + "\n" + \
                  "╠🛡 Tag" + "\n" + \
                  "╠🛡 Ourl" + "\n" + \
                  "╠🛡 Curl" + "\n" + \
                  "╠🛡 Gurl" + "\n" + \
                  "╠🛡 Staffadd @" + "\n" + \
                  "╠🛡 Staffdell @" + "\n" + \
                  "╠🛡 Mystaff" + "\n" + \
                  "╠🛡 Ban @" + "\n" + \
                  "╠🛡 Unban @" + "\n" + \
                  "╠🛡 Banlist" + "\n" + \
                  "╠🛡 Clearban" + "\n" + \
                  "╠🛡 Talkban @" + "\n" + \
                  "╠🛡 Untalkban @" + "\n" + \
                  "╠🛡 Talkbanlist" + "\n" + \
                  "╠🛡 Broadcast: [ text ]" + "\n" + \
                  "╠🛡 Translate" + "\n" + \
                  "╠🛡 Reject" + "\n" + \
                  "╠🛡 Prolist" + "\n" + \
                  "╠🛡 Memlist" + "\n" + \
                  "╠🛡 Upbio [ text ]" + "\n" + \
                  "╠🛡 Upname [ text ]" + "\n" + \
                  "╠🛡 Upgroup" + "\n" + \
                  "╠🛡 Upimage" + "\n" + \
                  "╠🛡 Jinlip" + "\n" + \
                  "╠╔═════════════════╗" + "\n" + \
                  "║            ๑۩ sᴇᴛᴛɪɴɢs ۩๑" + "\n" + \
                  "╠╚═════════════════╝" + "\n" + \
                  "╠🛡 Settag: [ jumlah ]" + "\n" + \
                  "╠🛡 Setcall: [ jumlah ]" + "\n" + \
                  "╠🛡 Cek spam" + "\n" + \
                  "╠🛡 Set spam [ text ]" + "\n" + \
                  "╠🛡 Cek respon" + "\n" + \
                  "╠🛡 Set respon [ text ]" + "\n" + \
                  "╠🛡 Cek pesan" + "\n" + \
                  "╠🛡 Set pesan [ text ]" + "\n" + \
                  "╠🛡 Cek welcome" + "\n" + \
                  "╠🛡 Set welcome [ text ]" + "\n" + \
                  "╠🛡 Cek left" + "\n" + \
                  "╠🛡 Set left [ text ]" + "\n" + \
                  "╠🛡 Cek sider" + "\n" + \
                  "╠🛡 Set sider [ text ]" + "\n" + \
                  "╠🛡 Respon:on/off" + "\n" + \
                  "╠🛡 Unsend:on/off" + "\n" + \
                  "╠🛡 Welcome:on/off" + "\n" + \
                  "╠🛡 Left:on/off" + "\n" + \
                  "╠🛡 Sider:on/off" + "\n" + \
                  "╠🛡 Notag:on/off" + "\n" + \
                  "╠🛡 Lurk:on" + "\n" + \
                  "╠🛡 Lurk:off" + "\n" + \
                  "╠🛡 Lurkers" + "\n" + \
                  "╠🛡 Setkey [ text ]" + "\n" + \
                  "╠🛡 Resetkey" + "\n" + \
                  "╠╔═════════════════╗" + "\n" + \
                  "║             ๑۩ ʜɪʙᴜʀᴀɴ ۩๑" + "\n" + \
                  "╠╚═════════════════╝" + "\n" + \
                  "╠🎵 Playlist [ nama penyanyi ]" + "\n" + \
                  "╠🎵 Ytmp3: [ judul lagu ]" + "\n" + \
                  "╠🎵 Ytmp4: [ judul video ]" + "\n" + \
                  "╠🎵 Profilesmule: [ id smule ]" + "\n" + \
                  "╠🎵 Cekig: [ nama IG ]" + "\n" + \
                  "╠🎵 Profileig: [ nama IG ]" + "\n" + \
                  "╠🎵 Gimage: [ keyword ]" + "\n" + \
                  "╔═════════════════╗" + "\n" + \
                  "║         ๑۩ ᴅᴇsᴛʀᴏʏᴇʀ ۩๑" + "\n" + \
                  "╚═════════════════╝" + "\n" + \
                  "╠☠ Gift: [ mid ]+[ jumlah ]" + "\n" + \
                  "╠☠ Spam: [ mid ]+[ jumlah ]" + "\n" + \
                  "╠☠ Spamtag @" + "\n" + \
                  "╠☠ Call" + "\n" + \
                  "╠☠ Kickall" + "\n" + \
                  "╠☠ Fuck @" + "\n" + \
                  "╠☠ Siri@block" + "\n" + \
                  "╠☠ Cancell" + "\n" + \
                  "╔═════════════════╗" + "\n" + \
                  "║         ๑۩ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ۩๑" + "\n" + \
                  "╚═════════════════╝" + "\n" + \
                  "╠☬🚦 Protectkick on/off" + "\n" + \
                  "╠☬🚦 Protectinvite on/off" + "\n" + \
                  "╠☬🚦 Protectcancel on/off" + "\n" + \
                  "╠☬🚦 Protectqr on/off" + "\n" + \
                  "╠☬🚦 Protectjoin on/off" + "\n" + \
                  "╠☬🚦 Allprotect on/off" + "\n" + \
                  "╔═══════════════════╗" + "\n" + \
                  "║     ༽ʀ-ʙᴏᴛs ᴍᴏɴsᴛᴇʀ ᴛᴇᴀᴍ༼" + "\n" + \
                  "║           ༽ᴘʏᴛʜᴏɴ3 ᴠ1.06༼" + "\n" + \
                  "╚═══════════════════╝"  
    return rean1
    
def translate():
    rean2 =     "╭══════════════════╮" + "\n" + \
                       "     ༺༽།☤ⵓʀᴇᴀɴ-sᴇʟғⵓ☤།༼༻" + "\n" + \
                       "╰══════════════════╯" + "\n" + \
                       "╠╔═════════════════╗" + "\n" + \
                       "║          ๑۩ ᴛʀᴀɴsʟᴀᴛᴏʀ ۩๑" + "\n" + \
                       "╠╚═════════════════╝" + "\n" + \
                       "╠☬ af : afrikaans" + "\n" + \
                       "╠☬ sq : albanian" + "\n" + \
                       "╠☬ en : inggris" + "\n" + \
                       "╠☬ ar : arabic" + "\n" + \
                       "╠☬ hi : hindi" + "\n" + \
                       "╠☬ haw : hawai" + "\n" + \
                       "╠☬ id : indonesia" + "\n" + \
                       "╠☬ it : italia" + "\n" + \
                       "╠☬ ja : jepang" + "\n" + \
                       "╠☬ jw : jawa" + "\n" + \
                       "╠☬ ko : korea" + "\n" + \
                       "╠☬ ca : catalan" + "\n" + \
                       "╠☬ kn : kanada" + "\n" + \
                       "╠☬ ms : malay" + "\n" + \
                       "╠☬ zh-cn : chinese (simplified)" + "\n" + \
                       "╠☬ zh-tw : chinese (traditional)" + "\n" + \
                       "╠☬ pa : punjabi" + "\n" + \
                       "╠☬ hr : croatian" + "\n" + \
                       "╠☬ cs : czech" + "\n" + \
                       "╠☬ da : danish" + "\n" + \
                       "╠☬ pt : portugis" + "\n" + \
                       "╠☬ my : myanmar" + "\n" + \
                       "╠☬ eo : esperanto" + "\n" + \
                       "╠☬ su : sunda" + "\n" + \
                       "╠☬ tl : filipino" + "\n" + \
                       "╠☬ fi : finnish" + "\n" + \
                       "╠☬ fr : french" + "\n" + \
                       "╠☬ es : spanyol" + "\n" + \
                       "╠☬ gl : galician" + "\n" + \
                       "╠☬ ka : georgian" + "\n" + \
                       "╠☬ de : german" + "\n" + \
                       "╠☬ el : greek" + "\n" + \
                       "╠☬ gu : gujarati" + "\n" + \
                       "╠☬ ht : haitian creole" + "\n" + \
                       "╠☬ th : thailand" + "\n" + \
                       "╚══[ Dilarang Typo😁😁 ]" + "\n" + "\n\n" + \
                         "Contoh : tr-en Rean-Bots"
    return rean2
groupParam = ""
def SiriGetOut(targ):
    rean.kickoutFromGroup(groupParam,[targ])
    #rean.kickoutFromGroup(groupParam,[targ])
    #rean.kickoutFromGroup(groupParam,[targ])
def byuh(targ):
    rean.kickoutFromGroup(groupParam,[targ])
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return            

        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if rean.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots:
                            rean.reissueGroupTicket(op.param1)
                            X = rean.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            rean.updateGroup(X)
                except:
                    pass
                    
        if op.type == 13:
            if Captain in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        rean.acceptGroupInvitation(op.param1)
                        ginfo = rean.getGroup(op.param1)
                        rean.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        rean.leaveGroup(op.param1)
                    else:
                        rean.acceptGroupInvitation(op.param1)
                        ginfo = rean.getGroup(op.param1)
                        rean.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if Captain in op.param3:
                if op.param2 in owner or admin or staff or Bots:
                    rean.acceptGroupInvitation(op.param1)
                else:
                    rean.acceptGroupInvitation(op.param1)
                    rean.leaveGroup(op.param1)      

        if op.type == 13:
            if op.param2 not in Bots and op.param2 not in admin:
                if op.param2 in Bots:
                    pass
                if op.param1 in protectinvite:
                    wait["blacklist"][op.param2] = True
                    rean.cancelGroupInvitation(op.param1,[op.param3])
                    rean.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots or owner or admin or staff:
                        if op.param2 in admin or Bots or owner or staff:
                            pass
                        if op.param1 in protectcancel:
                            wait["blacklist"][op.param2] = True
                            rean.sendText(msg.to,"eta terangkanlah..!!!")
                            rean.kickoutFromGroup(op.param1,[op.param2])                                                          

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                rean.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
                
        if op.type == 15:
            if op.param1 in leavegroup:
                if op.param2 in Bots:
                    pass
                ginfo = rean.getGroup(op.param1)
                contact = rean.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                rean.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = rean.getGroup(op.param1)
                contact = rean.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                rean.sendImageWithURL(op.param1, image)


        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	rean.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                rean.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    rean.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        rean.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return
                
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        rean.sendText(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in admin:
                    wait["blacklist"][op.param2] = True
                    rean.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 32:
            if op.param2 not in Bots and op.param2 not in admin:
                if op.param2 in Bots:
                    pass
                if op.param1 in protectcancel:
                    wait["blacklist"][op.param2] = True
                    rean.kickoutFromGroup(op.param1,[op.param2])
                else:
                	pass
                                                  
        if op.type == 19:
            if op.param3 in Bots:
            	if op.param2 in Bots or admin:
                    wait["blacklist"][op.param2] = True
                    try:
                        rean.kickoutFromGroup(op.param1,[op.param2])
                        rean.inviteIntoGroup(op.param1, [op.param3])
                    except:
                        pass

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass                       
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                rean.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
                
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = rean.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = rean.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        rean.sendImageWithURL(op.param1, image)
                        
                        
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = rean.getGroup(at)
                                rbots = rean.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(rbots.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':rbots.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                rean.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                rean.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = rean.getGroup(at)
                                rbots = rean.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(rbots.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                rean.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = rean.getGroup(at)
                                rbots = rean.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(rbots.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                rean.sendMessage(at, str(ret_))
                                rean.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
                    
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://leert.corrykalam.gq/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               rean.sendMessage(msg.to, str(data["answer"]))
                   except Exception as error:
                       pass

               if msg.to in translatetr:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='tr')
                           A = hasil.text
                           rean.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           rean.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           rean.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translateth:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='th')
                           A = hasil.text
                           rean.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translatetw:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='zh-tw')
                           A = hasil.text
                           rean.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           rean.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          rean.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              rean.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              rean.kickoutFromGroup(msg.to, [msg._from])
                              
#====================================BOTS DONE                              


               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   cName = cl.getContact(msg._from).displayName
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           rean.sendMessage(msg.to, "Oit...hadir kak " + cName + wait["Respontag"])
                           rean.sendMessage(msg.to, None, contentMetadata={"STKID":"7839705","STKPKGID":"1192862","STKVER":"1"}, contentType=7)                           
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           rean.mentiontag(msg.to,[msg._from])
                           rean.sendMessage(msg.to, "Jangan tag saya....")
                           rean.kickoutFromGroup(msg.to, [msg._from])
                           break
                           
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    rean.sendMessage(msg.to,"[Cek ID Sticker]\n✍ STKID : " + msg.contentMetadata["STKID"] + "\n✍ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n✍ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n[Link Sticker]" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
                    
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    rean.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = rean.getContact(msg.contentMetadata["mid"])
                        path = rean.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        rean.sendMessage(msg.to,"✍ Nama : " + msg.contentMetadata["displayName"] + "\n✍ MID : " + msg.contentMetadata["mid"] + "\n✍ Status Msg : " + contact.statusMessage + "\n✍ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        rean.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}

            if msg.contentType == 1:
                    path = rean.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = rean.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    rean.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
                    
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    rean.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = rean.getContact(msg.contentMetadata["mid"])
                        path = rean.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        rean.sendMessage(msg.to,"✍ Nama : " + msg.contentMetadata["displayName"] + "\n✍ MID : " + msg.contentMetadata["mid"] + "\n✍ Status Msg : " + contact.statusMessage + "\n✍ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        rean.sendImageWithURL(msg.to, image)
#ADD BLACKLIST
                 if msg._from in admin or owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        rean.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        rean.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        rean.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        rean.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin or owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        rean.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        rean.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        rean.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        rean.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = rean.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            rean.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     rean.updateGroupPicture(msg.to, path)
                     rean.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["RAfoto"]:
                            path = rean.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            rean.updateProfilePicture(path)
                            rean.sendMessage(msg.to,"Foto berhasil dirubah")
                            
#=====≠================================================================
#=====≠================== SCRIFT REMOTE================================
#=====≠================================================================
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        rean.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               rean1 = help()
                               rean.sendMessage(msg.to, str(rean1))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                rean.sendText(msg.to, "Self Turn On")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                rean.sendText(msg.to, "Self Turn Off")
                                
                        if cmd == "unsend:on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                rean.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")

                        if cmd == "unsend:off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                rean.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")
                                
                        elif cmd == "translate":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               rean2 = translate()
                               rean.sendMessage(msg.to, str(rean2))

                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md ="╭══════════════════╮\n     🔰 Settings Only 🔰\n╰══════════════════╯\n╔══════════════════╗\n"
                                if wait["sticker"] == True: md+="╠🔰 Sticker:On 📱\n"
                                else: md+="╠🔰 Sticker:Off 📴\n"
                                if wait["contact"] == True: md+="╠🔰 Contact:On 📱\n"
                                else: md+="╠🔰 Contact:Off 📴\n"
                                if wait["Mentionkick"] == True: md+="╠🔰 Notag:On 📱\n"
                                else: md+="╠🔰 Notag:Off 📴\n"
                                if wait["detectMention"] == True: md+="╠🔰 Respon:On📱\n"
                                else: md+="╠🔰 Respon:Off 📴\n"
                                if wait["autoJoin"] == True: md+="╠🔰 Join:On 📱\n"
                                else: md+="╠🔰 Join:Off 📴\n"
                                if wait["autoAdd"] == True: md+="╠🔰 Add:On 📱\n"
                                else: md+="╠🔰 Add:Off 📴\n"
                                if wait["unsend"] == True: md+="╠🔰 Unsend:On ??\n"
                                else: md+="╠🔰 Unsend:Off 📴\n"
                                if msg.to in welcome: md+="╠🔰 Welcome:On 📱\n"
                                else: md+="╠🔰 Welcome:Off 📴\n"
                                if msg.to in leavegroup: md+="╠🔰 Left:On 📱\n"
                                else: md+="╠🔰 Left:Off 📴\n"
                                if wait["autoLeave"] == True: md+="╠🔰 Leave:On 📱\n"
                                else: md+="╠🔰 Leave:Off 📴\n"
                                if msg.to in protectqr: md+="╠🔰 Protectqr On 📱\n"
                                else: md+="╠🔰 Protectqr Off 📴\n"
                                if msg.to in protectjoin: md+="╠🔰 Protectjoin On 📱\n"
                                else: md+="╠🔰 Protectjoin Off 📴\n"
                                if msg.to in protectkick: md+="╠🔰 Protectkick On 📱\n"
                                else: md+="╠🔰 Protectkick Off 📴\n"
                                if msg.to in protectcancel: md+="╠🔰 Proteckinvite On 📱\n"
                                else: md+="╠🔰 Protectinvite Off 📴\n╔══════════════════╗\n   🔰 Auto Translator 🔰\n╚══════════════════╝\n"
                                if msg.to in translatetr: md+="╠🔰 Turky:On 📱\n"
                                else: md+="╠🔰 Turky:Off 📴\n"
                                if msg.to in translateth: md+="╠🔰 Thailand:On 📱\n"
                                else: md+="╠🔰 Thailand:Off 📴\n"
                                if msg.to in translateen: md+="╠🔰 Inggris:On 📱\n"
                                else: md+="╠🔰 Inggris:Off 📴\n"
                                if msg.to in translateid: md+="╠🔰 Indonesia:On 📱\n"
                                else: md+="╠🔰 Indonesia:Off 📴\n"
                                if msg.to in translatear: md+="╠🔰 Arab:On 📱\n"
                                else: md+="╠🔰 Arab:Off 📴\n"
                                rean.sendMessage(msg.to, md+"╚══════════════════╝\n╔══════════════════╗\n╠🔰 Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠🔰 Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╠🔰 R-bots v1.06\n╚══════════════════╝")
                        
                        elif cmd == "creator":
                            if msg._from in admin:
                                rean.sendText(msg.to,"Creator Rean-Bots") 
                                ma = ""
                                for i in creator:
                                    ma = rean.getContact(i)
                                    rean.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "Type Selfbots\n")
                               rean.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               rean.sendMessage1(msg)

                        elif text.lower() == "mid ":
                               rean.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = rean.getContact(key1)
                               rean.sendMessage(msg.to, "✍ Nama : "+str(mi.displayName)+"\n✍ MID : " +key1)
                               rean.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = rean.getContact(key1)
                               rean.sendMessage(msg.to, "✍ Nama : "+str(mi.displayName)+"\n✍ Mid : " +key1+"\n✍ Status Msg"+str(mi.statusMessage))
                               rean.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   rean.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   rean.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
#================finish control==========================
                        elif text.lower() == "clearchat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   rean.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif cmd.lower().startswith("broadcast "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = rean.getGroupIdsJoined()
                               for group in saya:
                                   rean.sendMessage(group,"===[ Broadcast ]===\n" + str(pesan))
                               
                        elif cmd.lower().startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   rean.sendMessage(msg.to, "Error !")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   rean.sendMessage(msg.to, "Setkey changed {}".format(str(key).lower()))
                                                                      
                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               rean.sendMessage(msg.to, "✍ Setkey\nSetkey mu kembali ke awal")

                        elif cmd == " reboot" or text.lower() == 'reboot':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               rean.sendMessage(msg.to, "I'll come back....")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               rean.sendMessage(msg.to, "Rebooting done..")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Bot has been running\n " +waktu(eltime)
                               rean.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = rean.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                rean.sendMessage(msg.to, "✍ Info Groups\n____________________________\n✍ Nama Group : {}".format(G.name)+ "\n✍ ID Group : {}".format(G.id)+ "\n✍ Pembuat : {}".format(G.creator.displayName)+ "\n✍ Waktu Dibuat : {}".format(str(timeCreated))+ "\n✍ Jumlah Member : {}".format(str(len(G.members)))+ "\n✍ Jumlah Pending : {}".format(gPending)+ "\n✍ Group Qr : {}".format(gQr)+ "\n✍ Group Ticket : {}".format(gTicket))
                                rean.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                rean.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                rean.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin or staff:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = rean.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "🔰  Grup Info\n"
                                ret_ += "\n✍ Nama Group : {}".format(G.name)
                                ret_ += "\n✍ ID Group : {}".format(G.id)
                                ret_ += "\n✍ Pembuat : {}".format(gCreator)
                                ret_ += "\n✍ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n✍ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n✍ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n✍ Group Qr : {}".format(gQr)
                                ret_ += "\n✍ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                rean.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split("infomem ")
                            number = msg.text.replace(separate[0] + "infomem ","")
                            groups = rean.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "✍ "+ str(no) + ". " + mem.displayName
                                rean.sendMessage(to,"✍ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n[Total [%i] Members]" % len(G.members))
                            except: 
                                pass

                        elif cmd.lower() == "mygroups":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = rean.getGroupIdsJoined()
                               for i in gid:
                                   G = rean.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               rean.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
                               
                        elif cmd == "ourl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   Rbots = rean.getGroup(msg.to)
                                   Rbots.preventedJoinByTicket = False
                                   rean.updateGroup(Rbots)
                                   rean.sendMessage(msg.to, "Url Opened")

                        elif cmd == "curl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   Rbots = rean.getGroup(msg.to)
                                   Rbots.preventedJoinByTicket = True
                                   rean.updateGroup(Rbots)
                                   rean.sendMessage(msg.to, "Url Closed")

                        elif cmd == "gurl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   Rbots = rean.getGroup(msg.to)
                                   if Rbots.preventedJoinByTicket == True:
                                      Rbots.preventedJoinByTicket = False
                                      rean.updateGroup(Rbots)
                                   gurl = rean.reissueGroupTicket(msg.to)
                                   rean.sendMessage(msg.to, "Nama : "+str(Rbots.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                                   
                        elif cmd == "spaminvid":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                dan = msg.text.split("|")
                                userid = dan[1]
                                namagrup = dan[2]
                                jumlah = int(dan[3])
                                grups = cl.groups
                                tgb = rean.findContactsByUserid(userid)
                                if jumlah <= 10:
                                    for var in range(0,jumlah):
                                        try:
                                            rean.createGroup(str(namagrup), [tgb.mid])
                                            for i in grups:
                                                grup = rean.getGroup(i)
                                                if grup.name == namagrup:
                                                    rean.inviteIntoGroup(grup.id, [tgb.mid])
                                                    rean.leaveGroup(grup.id)
                                                    sendMention(msg.to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                                        except Exception as e:
                                            rean.sendMessage(msg.to, str(e))
                                else:
                                    sendMention(msg.to, "@! kokean blogg!!", [sender])
                                    
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = rean.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      rean.rejectGroupInvitation(gid)
                                  rean.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  rean.sendMessage(to, "Tidak ada undangan yang tertunda")
#==============================================================================#
                        elif text.lower() == 'crash':
                             if msg._from in admin:
                        	     rean.sendContact(to, "ub621484bd88d2486744123db00551d5e',")
                        elif text.lower() == 'mymid':
                             if msg._from in admin:                        	
                                 rean.sendMessage(msg.to,"[MID]\n" +  mid)
                        elif text.lower() == 'myname':
                             if msg._from in admin:                        	
                                 me = rean.getContact(mid)
                                 rean.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                        elif text.lower() == 'mybio':
                             if msg._from in admin:                        	
                                 me = rean.getContact(mid)
                                 rean.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                        elif text.lower() == 'mypic':
                             if msg._from in admin:                        	
                                 me = rean.getContact(mid)
                                 rean.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                        elif text.lower() == 'myvid':
                             if msg._from in admin:                        	
                                 me = rean.getContact(mid)
                                 rean.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                        elif text.lower() == 'mycover':
                             if msg._from in admin:                        	
                                 cover = rean.getProfileCoverURL(mid)    
                                 cl.sendImageWithURL(to, str(cover))
                             
                        elif msg.text.lower().startswith("getcontact "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = rean.getContact(ls)
                                    mi_d = contact.mid
                                    rean.sendContact(msg.to, mi_d)
                        elif msg.text.lower().startswith("getmid "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = "[ Mid User ]"
                                for ls in lists:
                                    ret_ += "\n{}" + ls
                                rean.sendMessage(msg.to, str(ret_))
                        elif msg.text.lower().startswith("getname "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = rean.getContact(ls)
                                    rean.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                        elif msg.text.lower().startswith("getbio "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = rean.getContact(ls)
                                    rean.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                        elif msg.text.lower().startswith("getpic "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = rean.getContact(ls)
                                    rean.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                        elif msg.text.lower().startswith("getvid "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.cl.naver.jp/" + cl.getContact(ls).pictureStatus + "/vp"
                                    rean.sendImageWithURL(msg.to, str(path))
                        elif msg.text.lower().startswith("getcover "):
                          if msg._from in admin:
                            if line != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        cover = rean.getProfileCoverURL(ls)
                                        rean.sendImageWithURL(to, str(cover))

#===========BOT UPDATE============#
                        elif cmd == "upgroup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                rean.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "upimage":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                rean.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                rean.updateProfile(profile)
                                rean.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.lower().startswith("upbio "):
                          if msg._from in admin:
                            sep = text.split("upbio ")
                            string = text.replace(sep[0] + "upbio ","")
                            if len(string) <= 100000000:
                                profile = rean.getProfile()
                                profile.statusMessage = string
                                rean.updateProfile(profile)
                                rean.sendMessage(to,"Berhasil mengganti status message menjadi {}".format(str(string)))
                         
                        elif text.lower() == 'memlist':
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = rean.getGroup(to)
                                ret_ = "╔══[ Member List ]"
                                no = 0 + 1
                                for mem in group.members:
                                    ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                    no += 1
                                ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                                rean.sendMessage(to, str(ret_))

#===========BOT UPDATE============#
                                   
                        elif text.lower() == 'tag':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = rean.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               k = len(nama)//20
                               for a in range(k+1):
                                   txt = u''
                                   s=0
                                   b=[]
                                   for i in group.members[a*20 : (a+1)*20]:
                                       b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                       s += 7
                                       txt += u'@Alin \n'
                                   rean.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                   rean.sendMessage(to, "[Total {} Mention] ".format(str(len(nama))))
                                   rean.sendMessage(to, " Mention by : R-bot Self ")

                        elif cmd == 'mystaff':
                          if msg._from in admin:
                            if admin == []:
                                rean.sendMessage(msg.to,"The StaffList is empty")
                            else:
                                num=0
                                mc = "Staff list :"
                                for mi_d in admin:
                                    mc += "\n%i. %s" % (num, cl.getContact(mi_d).displayName)
                                    num=(num+1)   
                                rean.sendMessage(msg.to, mc + "\n\n•R-Self V1.06")
                                print ("[Command]Stafflist executed")

                        elif cmd == "prolist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +rean.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +rean.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +rean.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +rean.getGroup(group).name + "\n"
                                rean.sendMessage(msg.to,"🔰 R-Self Protection\n\n🔰 PROTECT URL :\n"+ma+"\n🔰 PROTECT KICK :\n"+mb+"\n🔰 PROTECT JOIN :\n"+md+"\n🔰 PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "invitecreator":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [creator]
                                    rean.inviteIntoGroup(msg.to, anggota)
                                except:
                                    pass

                        elif cmd == " @bye" or text.lower() == 'jinlip':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = rean.getGroup(msg.to)
                                rean.sendText(msg.to, "Gua pamit dulu yeee.. \n"+str(G.name))
                                rean.leaveGroup(msg.to)                               

                        elif cmd == "rtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = rean.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = rean.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = rean.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                rean.sendMessage(msg.to, "Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "sp" or text.lower() == 'sp':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               rean.sendMessage(msg.to, "Proccess....")
                               elapsed_time = time.time() - start
                               rean.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 rean.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking:off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 rean.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(rean.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        rean.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    rean.sendText(msg.to, "User kosong...")
                            else:
                                rean.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider:on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  rean.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider:off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  rean.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  rean.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n☬ Lokasi : " + data[0]
                                         ret_ += "\n☬ " + data[1]
                                         ret_ += "\n☬ " + data[2]
                                         ret_ += "\n☬ " + data[3]
                                         ret_ += "\n☬ " + data[4]
                                         ret_ += "\n☬ " + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  rean.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n☬ Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n☬ Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n☬ Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n☬ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n☬ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                rean.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n☬ Location : " + data[0]
                                    ret_ += "\n☬ Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                rean.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("musik: "):
                          if msg._from in admin:
                            try:
                                search = msg.text.replace("musik: ","")
                                r = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                rean.sendImageWithURL(msg.to, str(data["gambar"]))
                                rean.sendMessage(msg.to, str(hasil))
                                rean.sendMessage(msg.to, "Downloading...")
                                rean.sendMessage(msg.to, "「 Result MP3 」")
                                rean.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                rean.sendMessage(msg.to, "「 Result M4A 」")
                                rean.sendVideoWithURL(msg.to, str(audio["m4a"]))
                                rean.sendMessage(msg.to, str(data["lirik"]))
                                rean.sendMessage(msg.to, "Success Download...")
                            except Exception as error:
                            	rean.sendMessage(msg.to, "「 Result Error 」\n" + str(error))

                        elif cmd.startswith("playlist "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lagu ]━━━━"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n☬「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    ret_ += "\n☬「 {}Lirik {}:nomor 」 ".format(str(),str(search))
                                    rean.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╭━━━━[ Detail Musik ]━━━━"
                                            ret_ += "\n┃ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n┃ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n┃ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n╰━━[ Tunggu Audionya ]━━━"
                                            rean.sendMessage(msg.to, str(ret_))
                                            rean.sendAudioWithURL(msg.to, str(data["result"]["mp3"][0]))
                            except Exception as error:
                                pass

                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                rean.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                rean.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                rean.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass

                        elif cmd.startswith("musik2: "):
                          if msg._from in admin:
                            try:
                                dan = msg.text.replace("musik2: ","")
                                r = requests.get("http://api.ntcorp.us/joox/song_info?sid={}"+urllib.parse.quote(dan))
                                data = r.json()
                                l = data["lyric"].replace("ti:","Judul: ")
                                i = l.replace("ar:","Penyanyi: ")
                                r = i.replace("al:","Album: ")
                                ii = r.replace("[by:]","")
                                k = ii.replace("[offset:0]","")
                                lirik = k.replace("***Lirik didapat dari pihak ketiga***\n","")
                                rean.sendImageWithURL(msg.to, data["image"])
                                t = "[ Music ]"
                                t += "\n\nJudul: "+str(data["title"])
                                t+="\nPenyanyi: "+str(data["singer"])
                                t+="\n\n[ Finish ]\n\n"+str(lirik)
                                rean.sendMessage(msg.to, str(t))
                                rean.sendAudioWithURL(msg.to, data["url"])
                            except Exception as error:
                                pass

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                keyword = msg.text.replace(separate[0] + " ","")
                                r = requests.get("https://farzain.xyz/api/gambarg.php?id="+keyword)
                                data = r.text
                                data = json.loads(data)
                                rean.sendImageWithURL(msg.to, str(data["url"]))
                            except Exception as error:
                            	pass

                        elif cmd.startswith("acaratv: "):
                          if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                channel = msg.text.replace(separate[0] + " ","")
                                r = requests.get("https://farzain.xyz/api/premium/acaratv.php?apikey=al11241519&id="+channel)
                                data = r.text
                                data = json.loads(data)
                                rean.sendMessage(msg.to, "Acara TV Di "+channel+ ":\n" + str(data["url"]))
                            except Exception as error:
                            	pass

                        elif cmd.startswith("meme"):
                          if msg._from in admin:
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            rean.sendImageWithURL(msg.to, image)

                        elif cmd.startswith("al-quran:"):
                            if msg._from in admin:
                                try:
                                    sep = msg.text.split(" ")
                                    search = msg.text.replace(sep[0] + " ","")
                                    with requests.session() as web:
                                        r = requests.get("http://api.alquran.cloud/surah/{}/ar.alafasy".format(str(search)))
                                        data = r.text
                                        data = json.loads(data)
                                        no = 0
                                        ret_ = "Quran Surah {}/{}\nSurah Ke-{}".format(str(data["data"]["englishName"]),str(data["data"]["name"]),str(data["data"]["number"]))
                                        for quran in data["data"]["ayahs"]:
                                            no += 1
                                            ret_ += "\n{}. {}".format(str(no),quran["text"])
                                        rean.sendMessage(msg.to, str(ret_))
                                except Exception as error:
                                     pass

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n☬ Author : ' + str(vid.author)
                                    durasi = '\n☬ Duration : ' + str(vid.duration)
                                    suka = '\n☬ Likes : ' + str(vid.likes)
                                    rating = '\n☬ Rating : ' + str(vid.rating)
                                    deskripsi = '\n☬ Deskripsi : ' + str(vid.description)
                                rean.sendVideoWithURL(msg.to, me)
                                rean.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                rean.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n☬ Author : ' + str(vid.author)
                                    durasi = '\n☬ Duration : ' + str(vid.duration)
                                    suka = '\n☬ Likes : ' + str(vid.likes)
                                    rating = '\n☬ Rating : ' + str(vid.rating)
                                    deskripsi = '\n☬ Deskripsi : ' + str(vid.description)
                                rean.sendImageWithURL(msg.to, me)
                                rean.sendAudioWithURL(msg.to, shi)
                                rean.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                rean.sendMessage(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                tj = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                rean.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                rean.sendImageWithURL(msg.to, tj)
                            except Exception as njer:
                                rean.sendMessage(msg.to, str(njer))

                        elif cmd.startswith("cekig:"):
                            if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/ig_profile.php?apikey=arTdnVbJkW1EuzDNQrIxQDvHtJIDcQ&id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "╭━━[ Profile Instagram ]"
                                        ret_ += "\n┃ Nama : {}".format(str(data["info"]["full_name"]))
                                        ret_ += "\n┃ Username : {}".format(str(data["info"]["username"]))
                                        ret_ += "\n┃ Bio : {}".format(str(data["info"]["bio"]))
                                        ret_ += "\n┃ URL Bio : {}".format(str(data["info"]["url_bio"]))
                                        ret_ += "\n┃ Pengikut : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃ Diikuti : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃ Total Post : {}".format(str(data["count"]["post"]))
                                        ret_ += "\n╰━━[ https://www.instagram.com/{} ]".format(search)
                                        path = data["info"]["profile_pict"]
                                        rean.sendMessage(to, str(ret_))
                                        rean.sendImageWithURL(to, str(path))
                                except Exception as e:
                                    rean.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            rean.sendMessage(msg.to,"🔰 I N F O R M A S I ����\n\n"+"🔰 Date Of Birth : "+lahir+"\n🔰 Age : "+usia+"\n🔰 Ultah : "+ultah+"\n🔰 Zodiak : "+zodiak)

                        elif cmd.startswith("settag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                rean.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("setcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                rean.sendText(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                rean.sendMessage1(msg)
                                            except Exception as e:
                                                rean.sendText(msg.to,str(e))
                                    else:
                                        rean.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "call":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                rean.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        rean.acquireGroupCallRoute(to)
                                        rean.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        rean.sendText(msg.to,str(e))
                                else:
                                    rean.sendText(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      rean.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      rean.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line ','')
                              conn = rean.findContactsByUserid(msgs)
                              if True:
                                  rean.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  rean.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
#==============================================================================#
                        elif msg.text.lower().startswith("tr-af "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='af')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sq "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sq')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-am "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='am')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ar "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ar')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hy "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hy')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-az "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='az')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-eu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='eu')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-be "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='be')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bn')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bs "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bs')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bg "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bg')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ca "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ca')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ceb "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ceb')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ny "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ny')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zh-cn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zh-cn')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zh-tw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zh-tw')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-co "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='co')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hr')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-cs "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='cs')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-da "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='da')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-nl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='nl')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-en "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='en')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-et "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='et')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fi')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fr')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fy "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fy')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-gl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='gl')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ka "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ka')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-de "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='de')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-el "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='el')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-gu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='gu')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ht "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ht')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ha "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ha')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-haw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='haw')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-iw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='iw')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hi')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-id "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='id')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-it "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='it')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ja "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ja')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-jw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='jw')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ko "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ko')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-my "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='my')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-pt "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='pt')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-es "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='es')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-su "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='su')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-th "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='th')
                            A = hasil.text
                            rean.sendMessage(msg.to, A)
#===========Protection============#
                        elif 'Welcome:' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome:','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Simi:' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Simi:','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Turky:' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Turky:','')
                              if spl == 'on':
                                  if msg.to in translatetr:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translatetr.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatetr:
                                         translatetr.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Thailand:' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Thailand:','')
                              if spl == 'on':
                                  if msg.to in translateth:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateth.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateth:
                                         translateth.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Inggris:' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Inggris:','')
                              if spl == 'on':
                                  if msg.to in translateen:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateen.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateen:
                                         translateen.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif 'Indonesia:' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Indonesia:','')
                              if spl == 'on':
                                  if msg.to in translateid:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateid.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateid:
                                         translateid.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Taiwan:' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Taiwan:','')
                              if spl == 'on':
                                  if msg.to in translatetw:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translatetw.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatetw:
                                         translatetw.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Arab:' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Arab:','')
                              if spl == 'on':
                                  if msg.to in translatear:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translatear.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatear:
                                         translatear.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Left:' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Left:','')
                              if spl == 'on':
                                  if msg.to in leavegroup:
                                       msgs = "Left Msg sudah aktif"
                                  else:
                                       leavegroup.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Left Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in leavegroup:
                                         leavegroup.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Left Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Left Msg sudah tidak aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Invite protect sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Invite protect diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Invite protrct dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Invite protect sudah tidak aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectqr ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect qr sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Protect qr diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Protect qr dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect qr sudah tidak aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = rean.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Allprotect ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allprotect ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = rean.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = rean.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  rean.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = rean.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    rean.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#

                        elif ("Fuck " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           rean.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                            
                        elif "Kickall" in msg.text:
                            if wait["selfbot"] == True:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    _name = msg.text.replace("Kickall","")
                                    gs = rean.getGroup(to)
                                    rean.sendMessage(to, "Sorry Broo..")
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        pass
                                    else:
                                        for target in targets:
                                            if not target in Bots:
                                                pass
#                                            else:
                                                try:
                                                    rean.kickoutFromGroup(to, [target])
                                                except:
                                                    pass
                                           
                        elif text.lower() == 'siri@block':
                            if msg._from in admin:
                                gs = rean.getGroup(msg.to)
                            gs = rean.getGroup(msg.to)
                            gs = rean.getGroup(msg.to)
                            sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん","0","1","2","3","4","5","6","7","8","9"])]
                            if sirilist != []:
                                groupParam = msg.to
                                try:
                                    p = Pool(40)
                                    p.map(SiriGetOut,sirilist)
                                    p.close()
                                except:
                                    p.close()

#===========ADMIN ADD============#
                                     
                        elif msg.text.lower().startswith("staffadd "):
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        admin.append(target)
                                        kk = rean.getContact(target).displayName
                                        kw = rean.getContact(msg._from).displayName
                                        rean.sendMessage(msg.to, kk + " has been promoted to staff by " + kw)
                                        break
                                    except:
                                        rean.sendMessage(msg.to,"Added Target failed !")
                                        break
                            else:
                                rean.sendMessage(msg.to,"Staff Permission Required")
                                     
                        elif msg.text.lower().startswith("staffdell "):
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        admin.remove(target)                                       
                                        kk = rean.getContact(target).displayName
                                        kw = rean.getContact(msg._from).displayName
                                        rean.sendMessage(msg.to, kk + " has been staff Expelled by " + kw)
                                        break
                                    except:
                                        rean.sendMessage(msg.to,"Added Target Failed !")
                                        break
                            else:
                                rean.sendMessage(msg.to,"Staff Permission Required")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                rean.sendText(msg.to,"Berhasil di Refresh...")

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                rean.sendText(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag:off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                rean.sendText(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                rean.sendText(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact:off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                rean.sendText(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon:on" or text.lower() == 'respon:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                rean.sendText(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon:off" or text.lower() == 'respon:off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                rean.sendText(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'join:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                rean.sendText(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'join:off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                rean.sendText(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'leave:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                rean.sendText(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'leave:off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                rean.sendText(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'add:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                rean.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'add:off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                rean.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                rean.sendText(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker:off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                rean.sendText(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'ticket:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                rean.sendText(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'ticket:off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                rean.sendText(msg.to,"Notag dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           rean.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           rean.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                reab.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                rean.sendText(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           rean.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           rean.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "banlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                rean.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +rean.getContact(m_id).displayName + "\n"
                                rean.sendMessage(msg.to,"🔰 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                rean.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +rean.getContact(m_id).displayName + "\n"
                                rean.sendMessage(msg.to,"🔰 Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    rean.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = rean.getContact(i)
                                        rean.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = rean.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              rean.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan ','')
                              if spl in [""," ","\n",None]:
                                  rean.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  rean.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set left ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set left ','')
                              if spl in [""," ","\n",None]:
                                  rean.sendMessage(msg.to, "Gagal mengganti Leave Msg")
                              else:
                                  wait["leave"] = spl
                                  rean.sendMessage(msg.to, "「Left Msg」\nLeave Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome ','')
                              if spl in [""," ","\n",None]:
                                  rean.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  rean.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon ','')
                              if spl in [""," ","\n",None]:
                                  rean.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  rean.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam ','')
                              if spl in [""," ","\n",None]:
                                  rean.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  rean.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider ','')
                              if spl in [""," ","\n",None]:
                                  rean.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  rean.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               rean.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               rean.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               rean.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")
                               
                        elif text.lower() == "cek left":
                            if msg._from in admin:
                               rean.sendMessage(msg.to, "「Left Msg」\nLeft Msg mu :\n\n「 " + str(wait["leave"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               rean.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               rean.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
    
                        elif msg.text.lower() == 'cancell':
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = rean.getGroup(msg.to)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    rean.cancelGroupInvitation(msg.to,[_mid])
                                rean.sendText(msg.to,"Success cancell")
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = rean.findGroupByTicket(ticket_id)
                                     rean.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     rean.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)        
        
                
while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass

  