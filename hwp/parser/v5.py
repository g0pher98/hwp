
def test():
	import olefile, pprint
	import hwp.parser.v5 as v5
	fh_data = olefile.OleFileIO("test.hwp").openstream('FileHeader').read()
	pprint.pprint(v5.fileheader(fh_data))

	
class Reader:
	def __init__(self, raw, start_index=0):
		self.focus = start_index
		self.data = raw
		return
	def pop(self, size, ):
		poped_data = data[focus:focus+size]
		focus += size
		return poped_data
	def intpop(size, endian="little")
		poped_data = int.from_bytes(data[focus:focus+size], endian)
		focus += size
		return poped_data
	
def fileheader(raw):
	'''
	:path: /FileHeader
	:document: [hwp v5.0] Page 8
	'''
	reader = Reader(raw)
	_property = '{0:032b}'.format(int.from_bytes(raw[36:40], "big"))
	_copyright = '{0:032b}'.format(int.from_bytes(raw[40:44], "big"))
	_encversion = {
		0 : None,
		1 : "한글 2.5 버전 이하",
		2 : "한글 3.0 버전 Enhanced",
		3 : "한글 3.0 버전 Old",
		4 : "한글 7.0 버전 이후"
	}
	_KOGLsupport = {
		0 : None, # 0번은 문서에 기록되어있지 않음.
		6 : 'KOR',
		15 : 'US'
	}
	structure = {
		'signature' : raw[0:32],
		'version' : '.'.join([str(i) for i in list(raw[32:36])[::-1]]),
		'문서 속성' : {
			'압축 여부' : bool(_property[0]),
			'암호 설정 여부' : bool(_property[1]),
			'배포용 문서 여부' : bool(_property[2]),
			'스크립트 저장 여부' : bool(_property[3]),
			'DRM 보안 문서 여부' : bool(_property[4]),
			'XMLTemplate 스토리지 존재 여부' : bool(_property[5]),
			'문서 이력 관리 존재 여부' : bool(_property[6]),
			'전자 서명 정보 존재 여부' : bool(_property[7]),
			'공인 인증서 암호화 여부' : bool(_property[8]),
			'전자 서명 예비 저장 여부' : bool(_property[9]),
			'공인 인증서 DRM 보안 문서 여부' : bool(_property[10]),
			'CCL 문서 여부' : bool(_property[11]),
			'모바일 최적화 여부' : bool(_property[12]),
			'개인정보 보안 문서 여부' : bool(_property[13]),
			'변경 추적 문서 여부' : bool(_property[14]),
			'공공누리(KOGL) 저작권 문서' : bool(_property[15]),
			'비디오 컨트롤 포함 여부' : bool(_property[16]),
			'차례 필드 컨트롤 포함 여부' : bool(_property[17]),
			'예약' : _property[18:]
		},
		'저작권 속성' : {
			'CCL' : _copyright[0],
			'복제 제한 여부' : _copyright[1],
			'동일 조건 하에 복제 허가 여부' : _copyright[2],
			'예약' : _copyright[3:]
		},
		'EncryptVersion' : _encversion[int.from_bytes(raw[44:48], "little")],
		'공공누리(KOGL) 라이선스 지원 국가' : _KOGLsupport[raw[48]],
		'예약' : raw[49:]
	}
	return structure

def docinfo(raw):
	'''
	:path: /DocInfo
	:document: [hwp v5.0] Page 9, 18, 19
	'''
	structure = {
		'HWPTAG_DOCUMENT_PROPERTIES' : None, #30
		'HWPTAG_ID_MAPPINGS' : None, #32
		'HWPTAG_BIN_DATA' : None,
		'HWPTAG_FACE_NAME' : None,
		'HWPTAG_BORDER_FILL' : None,
		'HWPTAG_CHAR_SHAPE' : None, #72
		'HWPTAG_TAB_DEF' : None, #14
		'HWPTAG_NUMBERING' : None,
		'HWPTAG_BULLET' : None, #10
		'HWPTAG_PARA_SHAPE' : None, #54
		'HWPTAG_STYLE' : None,
		'HWPTAG_MEMO_SHAPE' : None, #22
		'HWPTAG_TRACK_CHANGE_AUTHOR' : None,
		'HWPTAG_TRACK_CHANGE' : None,
		'HWPTAG_DOC_DATA' : None,
		'HWPTAG_FORBIDDEN_CHAR' : None,
		'HWPTAG_COMPATIBLE_DOCUMENT' : None, #4
		'HWPTAG_LAYOUT_COMPATIBILITY' : None, #20
		'HWPTAG_DISTRIBUTE_DOC_DATA' : None, #256
		'HWPTAG_TRACKCHANGE' : None #1032
	}
	reader = Reader(raw)
	structure['HWPTAG_DOCUMENT_PROPERTIES'] = reader.pop(30)
	structure['HWPTAG_ID_MAPPINGS'] = reader.pop(32)
	
	def HWPTAG_BIN_DATA():
		'''
		:reference: [hwp v5.0] Page 19, Cell 18
		'''
		structure = {}
		structure['property'] = reader.pop(2)
		size = reader.intpop(2)
		data = reader.pop(2*data)
		structure['LINK1_SIZE'] = size
		structure['LINK1'] = data
		size = reader.intpop(2)
		data = reader.pop(2*data)
		structure['LINK2_SIZE'] = size
		structure['LINK2'] = data
		structure['BINDATASTORAGE ID'] = reader.intpop(2)
		size = reader.intpop(2)
		data = reader.pop(2*data)
		structure['EMBEDDING_SIZE'] = size
		structure['EMBEDDING'] = data
		return structure
	

	

	# HWPTAG_FACE_NAME
	
	return structure

def bodytext_section(raw):
	'''
	:path: /BodyText/SectionN
	:document: [hwp v5.0] 9-10page
	'''
	structure = {
		'HWPTAG_PARA_HEADER' : 22,
		'HWPTAG_PARA_TEXT' : None,
		'HWPTAG_PARA_CHAR_SHAPE' : None,
		'HWPTAG_PARA_LINE_SEG' : None,
		'HWPTAG_PARA_RANGE_TAG' : None,
		'HWPTAG_CTRL_HEADER' : 4 ,
		'HWPTAG_LIST_HEADER' : 6 ,
		'HWPTAG_PAGE_DEF' : 40,
		'HWPTAG_FOOTNOTE_SHAPE' : 30,
		'HWPTAG_PAGE_BORDER_FILL' : 14,
		'HWPTAG_SHAPE_COMPONENT' : 4 ,
		'HWPTAG_TABLE' : None,
		'HWPTAG_SHAPE_COMPONENT_LINE' : 20,
		'HWPTAG_SHAPE_COMPONENT_RECTANGLE' : 9 ,
		'HWPTAG_SHAPE_COMPONENT_ELLIPSE' : 60,
		'HWPTAG_SHAPE_COMPONENT_ARC' : 25,
		'HWPTAG_SHAPE_COMPONENT_POLYGON' : None,
		'HWPTAG_SHAPE_COMPONENT_CURVE' : None,
		'HWPTAG_SHAPE_COMPONENT_OLE' : 26,
		'HWPTAG_SHAPE_COMPONENT_PICTURE' : None,
		'HWPTAG_CTRL_DATA' : None,
		'HWPTAG_EQEDIT' : None,
		'HWPTAG_SHAPE_COMPONENT_TEXTART' : None,
		'HWPTAG_FORM_OBJECT' : None,
		'HWPTAG_MEMO_SHAPE' : 22,
		'HWPTAG_MEMO_LIST' : 4 ,
		'HWPTAG_CHART_DATA' : 2 ,
		'HWPTAG_VIDEO_DATA' : None,
		'HWPTAG_SHAPE_COMPONENT_UNKNOWN' : 36
	}
	return structure

def hwpsummaryinformation():
	'''
	:path: /\005HwpSummaryInformation
	:document: [hwp v5.0] 12page
	'''
	structure = {
		'PIDSI_TITLE' : None,
		'PIDSI_SUBJECT' : None,
		'PIDSI_AUTHOR' : None,
		'PIDSI_KEYWORDS' : None,
		'PIDSI_COMMENTS' : None,
		'PIDSI_LASTAUTHOR' : None,
		'PIDSI_REVNUMBER' : None,
		'PIDSI_LASTPRINTED' : None,
		'PIDSI_CREATE_DTM' : None,
		'PIDSI_LASTSAVE_DTM' : None,
		'PIDSI_PAGECOUNT' : None,
		'HWPPIDSI_DATE_STR' : None,
		'HWPPIDSI_PARACOUNT' : None
	}
	return structure


