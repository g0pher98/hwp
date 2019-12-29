def load():
	f = open("test.hwp",'rb')
	return f.read()

def make_stream_chain(raw, block_number, property_start):
	'''
	@author : Lee Jae Seung
	
	체인을 구성하는 함수.
	'''
	block_raw = get_block(raw, block_number)
	block_list = [block_raw[i:i+4] for i in range(0, len(block_raw), 4)]
	idx = property_start
	chain = [idx]
	while True:
		idx = int.from_bytes(block_list[idx], "little")
		if idx == int.from_bytes(b'\xfd\xff\xff\xff', "little"):
			# special block
			break
		elif idx == int.from_bytes(b'\xfe\xff\xff\xff', "little"):
			# end
			break
		elif idx == int.from_bytes(b'\xff\xff\xff\xff', "little"):
			# non used block
			break
		else:
			chain.append(idx)
	return chain

def chain2stream(raw, chain):
	'''
	@author : Lee Jae Seung
	
	만들어진 체인 정보를 이용하여 블록을 이어서 스트림을 구성하는 함수.
	'''
	stream = b''
	for block_number in chain:
		stream += get_block(raw, block_number)
	return stream
		
		
		

def header(raw):
	'''
	[INFO]
	@author : Lee Jae Seung
	
	[DESCRIPTION]
	OLE 헤더를 딕셔너리화 하는 함수. 각 키와 설명은 다음과 같다.
	
	[MORE]
	signature : OLE 파일 시그니처
	number_of_BBAT_Depot : BBAT(Big Block Allocation Table)의 Depot(보관소)의 개수
	number_of_SBAT_Depot : SBAT(Small Block Allocation Table)의 Depot의 개수
	property_start : 스토리지와 스트림에 대한 정보가 담긴 블록 번호
	SBAT_start : SBAT 시작블록 번호
	BBAT_array : BBAT의 블록 정보가 담긴 배열(각 4bytes)
	'''
	data = {}
	data['signature'] = raw[0:8]
	data['number_of_BBAT_Depot'] = int.from_bytes(raw[44:48], "little")
	data['number_of_SBAT_Depot'] = int.from_bytes(raw[64:68], "little")
	data['property_start'] = int.from_bytes(raw[48:52], "little")
	data['SBAT_start'] = int.from_bytes(raw[60:64], "little")
	data['BBAT_array'] = []
	bbat_array_length = data['number_of_BBAT_Depot']*4
	bbat_array = raw[76:76 + bbat_array_length]
	for idx in range(0, len(bbat_array), 4):
		data['BBAT_array'].append(int.from_bytes(bbat_array[idx:idx + 4], "little"))
	return data


def get_block(raw, number):
	'''
	@author : Lee Jae Seung
	
	특정 번호에 해당하는 블록 데이터를 리턴하는 함수.
	'''
	idx = (number+1) * 512
	return raw[idx:idx + 512]


# ======= 여기부터는 문서만 보고 우선적으로 개발한 부분 ====

def fileheader(raw):
	data = {}
	data['signature'] = raw[0:32]
	data['version'] = {
		'MM' : raw[32],
		'nn' : raw[33],
		'PP' : raw[34],
		'rr' : raw[35]
	}
	data['']