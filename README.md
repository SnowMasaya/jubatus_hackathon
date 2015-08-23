Jubatus Tutorial in Python
==========================

* Jubatus Python Client is required for this tutorial (`pip install jubatus`).

Brief Usage
-----------

```
$ jubaclassifier --configpath pa.json 
$ python election.py
```

Note
----

If you encounter following problem,

```
socket.error: [Errno 99] Cannot assign requested address
```

try this:

```
$ sudo /sbin/sysctl -w net.ipv4.tcp_tw_recycle=1
```
