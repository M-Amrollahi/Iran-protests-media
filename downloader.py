
import thread_download
from multiprocessing import Pool

pool_download = Pool(4)

if __name__ == '__main__':
    
    print("pool start...")
    
    #Create a thread poold out of not-downloaded urls
    pool_download.map(thread_download.f_download, thread_download.f_getIndeces())

    
    thread_download.f_updateStatus()
    thread_download.f_saveData()
    print("pool end.")