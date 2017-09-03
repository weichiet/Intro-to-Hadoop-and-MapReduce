# Web Server Log Data
The data set we're using is an anonymized Web server log file from a public relations company whose clients were DVD distributors. Each line in the file represents a hit to the Web server. It includes the IP address which accessed the site, the date and time of the access, and the name of the page which was visited. It can be downloaded [here](/access_log.gz)

The logfile is in [Common Log Format](http://en.wikipedia.org/wiki/Common_Log_Format):

```
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

%h %l %u %t \"%r\" %>s %b
```
Where:

* %h is the IP address of the client
* %l is identity of the client, or "-" if it's unavailable
* %u is username of the client, or "-" if it's unavailable
* %t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
* %r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
* %>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes [in W3C.org](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html).
* %b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.

## List of Questions

Write some Mappers and Reducers to answer the following questions:  
1. [Find the number of hits for each different files on the website.](/01-hits-to-page)
2. [Find the number of hits to the site made by each different IP address.](/02-hits-from-ip)
3. [Find the most popular file on the website](/03-most-popular): that is, the file whose path occurs most often in access_log. Your reducer should output the file's path and the number of times it appear in the log.
