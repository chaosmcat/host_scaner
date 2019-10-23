import tkinter
import threading
import subprocess


def multi_ping(tmp_ip):
    thread_list = []
    for init in range(0, 256):
        tmp_ip[3] = str(init)
        test_ip = '.'.join(tmp_ip)
        thread_list.append(threading.Thread(target=single_ping, args=(test_ip,)))
    for item in thread_list:
        item.start()


def single_ping(test_ip):
    cmd_str = "ping {0} -n 1 -w 200 -4".format(test_ip)
    detached_process = 0x00000008
    init = test_ip.split(".")
    try:
        subprocess.run(cmd_str, creationflags=detached_process, check=True)
    except subprocess.CalledProcessError as e:
        globals()["lb" + str(init[3])]["bg"] = 'red'
        print(str(init[3]) + " Close")
    else:
        globals()["lb" + str(init[3])]["bg"] = 'green'
        print(str(init[3]) + "  Alive")


def ip_address_analysis():
    default_ip = ip_entry.get()
    start_ip = default_ip.split(".")
    multi_ping(tmp_ip=start_ip)


ui = tkinter.Tk()
ui.title('')

area_lf1 = tkinter.LabelFrame(ui)

frame_operate = tkinter.Frame(area_lf1)
tkinter.Label(frame_operate, text="输入需扫描的IP段（如127.0.0.*）：").grid(row=0, column=0)
ip_entry = tkinter.Entry(frame_operate, width=11)
ip_entry.grid(row=0, column=1)
tkinter.Button(frame_operate, text="Load", command=ip_address_analysis, width=8).grid(row=0, column=2, padx=6)
frame_operate.grid(row=0, column=0, pady=5)

frame_ip_pool = tkinter.Frame(area_lf1)
for i in range(0, 16):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=0, column=i)
for i in range(16, 32):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=1, column=i-16)
for i in range(32, 48):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=2, column=i-32)
for i in range(48, 64):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=3, column=i-48)
for i in range(64, 80):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=4, column=i-64)
for i in range(80, 96):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=5, column=i-80)
for i in range(96, 112):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=6, column=i-96)
for i in range(112, 128):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=7, column=i-112)
for i in range(128, 144):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=8, column=i-128)
for i in range(144, 160):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=9, column=i-144)
for i in range(160, 176):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=10, column=i-160)
for i in range(176, 192):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=11, column=i-176)
for i in range(192, 208):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=12, column=i-192)
for i in range(208, 224):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=13, column=i-208)
for i in range(224, 240):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=14, column=i-224)
for i in range(240, 256):
    locals()["lb" + str(i)] = tkinter.Label(frame_ip_pool, text=str(i), bg="gray", width=3, relief="sunken")
    locals()["lb" + str(i)].grid(row=15, column=i-240)

frame_ip_pool.grid(row=1, column=0, padx=5, pady=5)
tkinter.Label(area_lf1, text="颜色为绿色表示有链接；颜色为红色表示无连接").grid(row=2, column=0)
area_lf1.grid(row=0, column=0, padx=5, pady=5)

ui.mainloop()
