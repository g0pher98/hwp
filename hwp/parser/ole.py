def get_block(raw, number):
	'''
	특정 번호에 해당하는 블록 데이터를 리턴하는 함수.
	:return: 블록데이터(512bytes)
	'''
	idx = (number+1) * 512
	return raw[idx:idx + 512]


def split_by_size(data, size):
	'''
	데이터를 사이즈로 split 하는 함수.
	:return: split된 리스트
	'''
	return [data[i:i+size] for i in range(0, len(data), size)]


def make_chain(raw, block_number, property_start):
	'''
	chain을 구성하는 함수.
	:return: 체인 덤프
	'''
	block_raw = get_block(raw, block_number)
	block_list = split_by_size(block_raw, 4)
	idx = property_start
	chain_list = [idx]
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
			chain_list.append(idx)
	# chain list to chain
	chain = b''
	for block_number in chain_list:
		chain += get_block(raw, block_number)
	return chain

def chain2properties(chain):
	'''
	chain을 각 property로 분할하고,
	각 property를 딕셔너리화 하는 함수.
	
	:return: 프로퍼티 정보 딕셔너리
	'''
	elements = split_by_size(chain, 126)
	properties = {}
	
	for p in elements:
		info = {
			'name' : p[0:64],
			'name_length': int.from_bytes(p[64:66], "little"),
			'type' : int.from_bytes(p[66], "little"), # 1:Storage, 2:Stream, 5:root
			'prevProperty' : int.from_bytes(p[68:72], "little"),
			'nextProperty' : int.from_bytes(p[72:76], "little"),
			'innerProperty' : int.from_bytes(p[76:80], "little")
		}
		name = info['name'][0:info['name_length']] 
		properties[name] = info

	return properties

def header(raw):
	'''
	OLE 헤더를 딕셔너리화 하는 함수. 각 키와 설명은 다음과 같다.
	
	[MORE]
	signature : OLE 파일 시그니처
	number_of_BBAT_Depot : BBAT(Big Block Allocation Table)의 Depot(보관소)의 개수
	number_of_SBAT_Depot : SBAT(Small Block Allocation Table)의 Depot의 개수
	property_start : 스토리지와 스트림에 대한 정보가 담긴 블록 번호
	SBAT_start : SBAT 시작블록 번호
	BBAT_array : BBAT의 블록 정보가 담긴 배열(각 4bytes)
	'''
	data = {
		'signature' : raw[0:8],
		'number_of_BBAT_Depot' : int.from_bytes(raw[44:48], "little"),
		'number_of_SBAT_Depot' : int.from_bytes(raw[64:68], "little"),
		'property_start' : int.from_bytes(raw[48:52], "little"),
		'SBAT_start' : int.from_bytes(raw[60:64], "little"),
		'BBAT_array' : []
	}
	bbat_array_length = data['number_of_BBAT_Depot']*4
	bbat_array = raw[76:76 + bbat_array_length]
	for idx in range(0, len(bbat_array), 4):
		data['BBAT_array'].append(int.from_bytes(bbat_array[idx:idx + 4], "little"))
	return data

