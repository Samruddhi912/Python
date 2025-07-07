import psutil
import time
import os
import sys
import smtplib
from email.message import EmailMessage

def ProcInfoLog():
    process=[]
    for proc in psutil.process_iter():
        info=proc.as_dict(attrs=["name","pid","username"])
        info["vms"]=proc.memory_info().vms/(1024*1024)
        process.append(info)

    return process
    
def Directory(DName,ProcessInfo):
    border="-"*80
    timestamp=time.ctime()
    FName="ProcessInformation%s.log" %timestamp
    FName=FName.replace("/","_")
    FName=FName.replace(":","_")
    FName=FName.replace(" ","_")

    if not os.path.exists(DName):
        os.makedirs(DName)
    FilePath=(os.path.join(DName,FName))

    Fobj=open(FilePath,"w")
    Fobj.write(f"File is created at: {timestamp}\n")
    Fobj.write(border+"\n")
    for proc in ProcessInfo:
        Fobj.write(f"Name:{proc["name"]},PID:{proc["pid"]},User:{proc["username"]},VMS:{proc["vms"]:2f}MB")
    Fobj.write("\n\n")
    Fobj.write(border+"\n")

    return FilePath

def SendEmail(ToEmail,Attachment):
    sender_email="samruddhi2049@gmail.com"
    sender_pass="jkxdiehtwfsejday"
    msg=EmailMessage()
    msg["From"]=sender_email
    msg["To"]=ToEmail
    msg["Subject"]="Process Info Log File"
    msg.set_content("Please find the attached process log file")

    mobj=open(Attachment,"rb")
    file_data=mobj.read()
    filename=os.path.basename(Attachment)
    msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=filename)

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(sender_email,sender_pass)
        smtp.send_message(msg)
    
    print(f"Email sent successfully to{ToEmail}")
    

def main():
    if len(sys.argv)!=3:
        print("Usage: ProcInfo.py <DirectoryName> <EmailId>")
    Dirname=sys.argv[1]
    Email=sys.argv[2]
    Result=ProcInfoLog()
    DPath=Directory(Dirname,Result)
    SendEmail(Email,DPath)




if __name__=="__main__":
    main()