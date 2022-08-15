import speedtest    #adding library

test = speedtest.Speedtest()        #adding the speedtest class

print("Loading server list...")
test.get_servers()             #getting lists of servers.
print("Choosing best server...")
best = test.get_best_server()          #choosing best server.

print(f"Found: {best['host']} located in {best['country']}")      #finding the best host and country for test

print("Download test in progress...")
download_result = test.download()       #downloading test
print("Upload test in progress...")
upload_result = test.upload()           #uploading test

ping_result = test.results.ping

print(f"Download speed: {download_result / 1024 / 1024: 2f} Mb/s")         #printing and converting bit/s to mb/s
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mb/s")             #printing and converting bit/s to mb/s
print(f"Ping: {ping_result:.2f} ms")
