# -*- coding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import io
def gen_s_word(word):
		suffixes ={
		1:[u"ो",u"ः",u"े",u"ं",u"ौ",u"ा"],
		2:[u"ाः",u"ेण",u"ेन​",u"ान्",u"णी",u"व​े",u"ोः",u"न​े",u"िन​",u"ाय",u"ेव",u"म्",u"ैः",u"ेन",u"णा",u"ना"],
		3:[u"​ात्",u"ेणु",u"ेह​ी",u"ेषु",u"ात्",u"याः",u"ान्",u"ेणा",u"िभः",u"ियों","ानि",u"ाणि",u"य​ोः",u"स्य",u"णां",u"यै",u"यां"],
		4:[u"भ​ीः",u"ेभ्यः",u"ायोः",u"िय​े",u"ियै",u"ानां"],
		
		
}
		l=[u"ियों",u"ियै"] #for ekarant striling
		l1=[u"िय​े"]
		l2=[u"व​े",u"ोः"]
	#print(len(word))
		for L in 4,3,2,1:
			if len(word) >L+1:
				for s in suffixes[L]:
					if word.endswith(s):	
							word=word.replace(s," ")
							#print(s)
							if s in l: #for ekarant striling
								word=word+"ी"
							elif s in l1:
								word=word+"ि"
							elif s in l2:
								word=word+"ु"

						
		return word

if __name__=="__main__":
	with io.open('input1.txt','r',encoding='utf-8') as f:
		#print("enter the input")
		text=f.read().strip()
		for word in text.split():
			temp=gen_s_word(word)
			print(word+'	'+temp)
