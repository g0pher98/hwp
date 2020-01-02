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


def get_block(raw, number):
	'''
	@author : Lee Jae Seung
	
	특정 번호에 해당하는 블록 데이터를 리턴하는 함수.
	'''
	idx = (number+1) * 512
	return raw[idx:idx + 512]


# ======= 여기부터는 문서만 보고 우선적으로 개발한 부분 ====

def fileheader(raw):
	'''
	@author : Lee Jae Seung
	
	FileHeader(256Bytes) 스트림 파싱함수.
	hwp 구조 5.0 문서 8page 참고하여 개발.
	'''
	data = {
		'signature' : raw[0:32],
		'version' : {
			'MM' : raw[32],
			'nn' : raw[33],
			'PP' : raw[34],
			'rr' : raw[35]
		},
		'property' : {
			'compressed' : ,
			'password' : ,
			'distribution' : ,
			'script' : ,
			'DRM' : ,
			'XML_template_stroage' : ,
			'document_history' : ,
			'electronic_signature' : ,
			'authorized_certificate' : ,
			'electronic_signature_tmp' : ,
			'authorized_certificate_DRM' : ,
			'CCL' : ,
			'mobile' : ,
			'privacy' : ,
			'modify_trace' : ,
			'KOGL' : ,
			'video_control' : ,
			'index_fild_control' : ,
			'reservation' : 	
		},
		'licence' : {
			'CCL' : ,
			'not_copy' : ,
			'same_copy' : ,
			'reservation' : 
		},
		'EncryptVersion' : ,
		'KOGL' : ,
		'reservation' :
	}
	return data

def docinfo(raw):
	'''
	@author : Lee Jae Seung
	'''
	data = {
		'HWPTAG_DOCUMENT_PROPERTIES' : 30,
		'HWPTAG_ID_MAPPINGS' : 32,
		'HWPTAG_BIN_DATA' : 가변,
		'HWPTAG_FACE_NAME' : 가변,
		'HWPTAG_BORDER_FILL' : 가변,
		'HWPTAG_CHAR_SHAPE' : 72,
		'HWPTAG_TAB_DEF' : 14,
		'HWPTAG_NUMBERING' : 가변,
		'HWPTAG_BULLET' : 10,
		'HWPTAG_PARA_SHAPE' : 54,
		'HWPTAG_STYLE' : 가변,
		'HWPTAG_MEMO_SHAPE' : 22,
		'HWPTAG_TRACK_CHANGE_AUTHOR' : 가변,
		'HWPTAG_TRACK_CHANGE' : 가변,
		'HWPTAG_DOC_DATA' : 가변,
		'HWPTAG_FORBIDDEN_CHAR' : 가변,
		'HWPTAG_COMPATIBLE_DOCUMENT' : 4,
		'HWPTAG_LAYOUT_COMPATIBILITY' : 20,
		'HWPTAG_DISTRIBUTE_DOC_DATA' : 256,
		'HWPTAG_TRACKCHANGE' : 1032
	}
	return data

def bodytext_section(raw):
	'''
	@author : Lee Jae Seung
	'''
	data = {
		'HWPTAG_PARA_HEADER' : 22,
		'HWPTAG_PARA_TEXT' : 가변,
		'HWPTAG_PARA_CHAR_SHAPE' : 가변,
		'HWPTAG_PARA_LINE_SEG' : 가변,
		'HWPTAG_PARA_RANGE_TAG' : 가변,
		'HWPTAG_CTRL_HEADER' : 4 ,
		'HWPTAG_LIST_HEADER' : 6 ,
		'HWPTAG_PAGE_DEF' : 40,
		'HWPTAG_FOOTNOTE_SHAPE' : 30,
		'HWPTAG_PAGE_BORDER_FILL' : 14,
		'HWPTAG_SHAPE_COMPONENT' : 4 ,
		'HWPTAG_TABLE' : 가변,
		'HWPTAG_SHAPE_COMPONENT_LINE' : 20,
		'HWPTAG_SHAPE_COMPONENT_RECTANGLE' : 9 ,
		'HWPTAG_SHAPE_COMPONENT_ELLIPSE' : 60,
		'HWPTAG_SHAPE_COMPONENT_ARC' : 25,
		'HWPTAG_SHAPE_COMPONENT_POLYGON' : 가변,
		'HWPTAG_SHAPE_COMPONENT_CURVE' : 가변,
		'HWPTAG_SHAPE_COMPONENT_OLE' : 26,
		'HWPTAG_SHAPE_COMPONENT_PICTURE' : 가변,
		'HWPTAG_CTRL_DATA' : 가변,
		'HWPTAG_EQEDIT' : 가변,
		'HWPTAG_SHAPE_COMPONENT_TEXTART' : 가변,
		'HWPTAG_FORM_OBJECT' : 가변,
		'HWPTAG_MEMO_SHAPE' : 22,
		'HWPTAG_MEMO_LIST' : 4 ,
		'HWPTAG_CHART_DATA' : 2 ,
		'HWPTAG_VIDEO_DATA' : 가변,
		'HWPTAG_SHAPE_COMPONENT_UNKNOWN' : 36
	}
	return data


