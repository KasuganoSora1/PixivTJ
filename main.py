from concurrent.futures import ThreadPoolExecutor,wait
import web
pool=ThreadPoolExecutor(10)
for i in range(1,100000):
        all_task=[pool.submit(web.write_from_page_id,str(k)) for k in range((i-1)*1000+1,i*1000)]
        print("put to "+str((i-1)*1000+1)+","+str(i*1000)+" pool")
        wait(all_task)