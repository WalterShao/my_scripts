import os
import smtplib
import socket
import traceback

def send_email(user, pwd, recipient, subject, body):
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail, title = "' + subject + '"'
    except Exception as e:
        tb_msg = traceback.format_exc()
        print "failed to send mail, ex=" + str(e)
        print tb_msg


def get_my_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("gmail.com",80))
    my_ip = sock.getsockname()[0]
    sock.close()
    return my_ip


def get_disk_usage(path):
    """Return disk usage statistics about the given path.
    """
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return free, used, total

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

my_ip = get_my_ip()
free, used, total = get_disk_usage('/home')
ratio = used * 100 / float(total)
show_str = ('(Free, used, total, ratio) = (%s, %s, %s, %.2f%%)' 
    % (sizeof_fmt(free), sizeof_fmt(used), sizeof_fmt(total), ratio))

user = 'waltershao@gmail.com'
pwd = 'no9147wa'
recipient = 'waltershao@gmail.com' 
subject = 'IP of my Ubuntu VM: ' + my_ip
body = 'The IP of my Ubuntu VM is ' + my_ip + '\n'
body = body + "Usage of '/home' directory -> "
body = body + show_str

print body

send_email(user, pwd, recipient, subject, body)