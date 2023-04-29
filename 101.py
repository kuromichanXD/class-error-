import dropbox
class data:
    def __init__ (quaso,access_token):
        quaso.access_token = access_token
    
    def upload_file(quaso,filefrom,fileto):
        ddx=dropbox.Dropbox(quaso.access_token)
        f=open(filefrom,"rb")
        ddx.files_upload(f.read(),fileto)

def main():
    access_token="sl.BdYmv8H7Ey4H05aNDGCThVCA1UYpYbf-z4sbKDkGTCoyJHnYELMGwdsE_9pKb8y1EodhALNvDomtftQCCn3b3Gs4cojNJmMsIYe2d8rfvlVr8tbemZPlZN7xsi1LaO8KXEEPNHQ"
    transferdata=data(access_token)
    filefrom=input("enter the file path to transfer")
    fileto=input("enter the full path to upload")
    transferdata.upload_file(filefrom,fileto)
    print("file has been moved")
    
main()
