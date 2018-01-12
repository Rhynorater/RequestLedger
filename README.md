# RequestLedger
A program designed to log http requests handed to a server to help with detecting host HTTP Header issues.

```
[justin@RhynoDroplet RequestLedger]$ python RequestLedger.py -h
usage: RequestLedger.py [-h] [-p PORT] [--host HOST]

Request Ledger: A program to log and gracefully deal with incoming HTTP
connections and present the user with a log of these for their review.

optional arguments:
  -h, --help   show this help message and exit
  -p PORT      What port should I bind to?
  --host HOST  What host should I bind to?
```

Log result output:

```
[justin@RhynoDroplet RequestLedger]$ cat logfile.txt 
----- Incoming Request - Request ID 20180112_1 ----->
Client Address:11.11.11.11
Client Hostname:superSecrethostName.com
----- *Request Start* -----
/
Host: NOTsuperSecrethostName.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8,it;q=0.6
<----- *Request End* -----
```
