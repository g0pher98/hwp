
def test():
	import olefile, pprint
	import hwp.parser.v5 as v5
	fh_data = olefile.OleFileIO("test.hwp").openstream('FileHeader').read()
	pprint.pprint(v5.fileheader(fh_data))
	pprint.pprint(v5.docinfo(fh_data[256:]))

	
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
	return {'FileHeader':structure, 'size':256}

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
	structure['HWPTAG_BIN_DATA'] = HWPTAG_BIN_DATA()
	structure['HWPTAG_FACE_NAME'] = HWPTAG_FACE_NAME()
	structure['HWPTAG_BORDER_FILL'] = HWPTAG_BORDER_FILL()
	structure['HWPTAG_CHAR_SHAPE'] = reader.pop(72)
	structure['HWPTAG_TAB_DEF'] = reader.pop(14)
	structure['HWPTAG_NUMBERING'] = HWPTAG_NUMBERING()
	structure['HWPTAG_BULLET'] = reader.pop(10)
	structure['HWPTAG_PARA_SHAPE'] = reader.pop(54)
	structure['HWPTAG_STYLE'] = HWPTAG_STYLE()
	structure['HWPTAG_MEMO_SHAPE'] = reader.pop(22)
	structure['HWPTAG_TRACK_CHANGE_AUTHOR'] = HWPTAG_TRACK_CHANGE_AUTHOR()
	structure['HWPTAG_TRACK_CHANGE'] = HWPTAG_TRACK_CHANGE()
	structure['HWPTAG_DOC_DATA'] = HWPTAG_DOC_DATA()
	structure['HWPTAG_FORBIDDEN_CHAR'] = HWPTAG_FORBIDDEN_CHAR()
	structure['HWPTAG_COMPATIBLE_DOCUMENT'] = reader.pop(4)
	structure['HWPTAG_LAYOUT_COMPATIBILITY'] = reader.pop(20)
	structure['HWPTAG_DISTRIBUTE_DOC_DATA'] = reader.pop(256)
	structure['HWPTAG_TRACKCHANGE'] = reader.pop(1032)
	
	def HWPTAG_BIN_DATA():
		'''
		:reference: [hwp v5.0] Page 19, Cell 18
		'''
		structure = {
			'PROPERTY' : None, # 속성
			'LINK1_SIZE' : None,
			# Type이 "LINK"일 때, 연결 파일의 절대 경로 길이 (len1)
			'LINK1' : None,
			# Type이 "LINK"일 때, 연결 파일의 절대 경로
			'LINK2_SIZE' : None,
			# Type이 "LINK"일 때, 연결 파일의 상대 경로 길이 (len2)
			'LINK2' : None,
			# Type이 "LINK"일 때, 연결 파일의 상대 경로
			'BINDATASTORAGE_ID' : None,
			# Type이 "EMBEDDING"이나 "STORAGE"일 때, BINDATASTORAGE 데이터의 아이디
			'EMBEDDING_SIZE' : None,
			# Type이 "EMBEDDING"일 때, 바이너리 데이터의 형식 이름의 길이 (len3)
			'EMBEDDING' : None
			# Type이 "EMBEDDING"일 때 extension("." 제외)
		}
		properties = reader.pop(2)
		structure['PROPERTY'] = properties
		'''
		[TODO]
		properties를 비트로 변환하고, 딕셔너리로 만들어서 넣을 예정.
		19 page의 표18(바이너리 데이터 속성) 참고.
		'''
		size = reader.intpop(2)
		data = reader.pop(2*data)
		structure['LINK1_SIZE'] = size
		structure['LINK1'] = data
		
		size = reader.intpop(2)
		data = reader.pop(2*data)
		structure['LINK2_SIZE'] = size
		structure['LINK2'] = data
		structure['BINDATASTORAGE_ID'] = reader.intpop(2)
		
		size = reader.intpop(2)
		data = reader.pop(2*data)
		structure['EMBEDDING_SIZE'] = size
		structure['EMBEDDING'] = data
		return structure
	
	def HWPTAG_FACE_NAME():
		structure = {
			'PROPERTY' : None,
			'FONTNAME_LEN' : None,
			'FONTNAME' : None,
			'REPLACED_FONTTYPE' : None,
			'REPLACED_FONTNAME_LEN' : None,
			'REPLACED_FONTNAME' : None,
			'FONTTYPE_INFO' : None,
			
		}
		properties = reader.intpop(1)
		structure['property'] = properties
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_BORDER_FILL():
		'''
		[TODO]
		미완.
		'''
		return

	def HWPTAG_NUMBERING():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_STYLE():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_TRACK_CHANGE_AUTHOR():
		'''
		[TODO]
		미완.
		'''
		return

	def HWPTAG_TRACK_CHANGE():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_DOC_DATA():
		'''
		[TODO]
		미완.
		'''
		return
	
	
	def HWPTAG_FORBIDDEN_CHAR():
		'''
		[TODO]
		미완.
		'''
		return

	
	return structure

def bodytext_section(raw):
	'''
	:path: /BodyText/SectionN
	:document: [hwp v5.0] 9-10page
	'''
	structure = {
		'HWPTAG_PARA_HEADER' : None, #22
		'HWPTAG_PARA_TEXT' : None,
		'HWPTAG_PARA_CHAR_SHAPE' : None,
		'HWPTAG_PARA_LINE_SEG' : None,
		'HWPTAG_PARA_RANGE_TAG' : None,
		'HWPTAG_CTRL_HEADER' : None, #4
		'HWPTAG_LIST_HEADER' : None, #6
		'HWPTAG_PAGE_DEF' : None, #40
		'HWPTAG_FOOTNOTE_SHAPE' : None, #30
		'HWPTAG_PAGE_BORDER_FILL' : None, #14
		'HWPTAG_SHAPE_COMPONENT' : None, #4
		'HWPTAG_TABLE' : None,
		'HWPTAG_SHAPE_COMPONENT_LINE' : None, #20
		'HWPTAG_SHAPE_COMPONENT_RECTANGLE' : None, #9 
		'HWPTAG_SHAPE_COMPONENT_ELLIPSE' : None, #60
		'HWPTAG_SHAPE_COMPONENT_ARC' : None, #25
		'HWPTAG_SHAPE_COMPONENT_POLYGON' : None,
		'HWPTAG_SHAPE_COMPONENT_CURVE' : None,
		'HWPTAG_SHAPE_COMPONENT_OLE' : None, #26
		'HWPTAG_SHAPE_COMPONENT_PICTURE' : None,
		'HWPTAG_CTRL_DATA' : None,
		'HWPTAG_EQEDIT' : None,
		'HWPTAG_SHAPE_COMPONENT_TEXTART' : None,
		'HWPTAG_FORM_OBJECT' : None,
		'HWPTAG_MEMO_SHAPE' : None, #22
		'HWPTAG_MEMO_LIST' : None, #4
		'HWPTAG_CHART_DATA' : None, #2
		'HWPTAG_VIDEO_DATA' : None,
		'HWPTAG_SHAPE_COMPONENT_UNKNOWN' : None #36
	}
	reader = Reader(raw)
	structure['HWPTAG_PARA_HEADER'] = reader.pop(22),
	structure['HWPTAG_PARA_TEXT'] = HWPTAG_PARA_TEXT(),
	structure['HWPTAG_PARA_CHAR_SHAPE'] = HWPTAG_PARA_CHAR_SHAPE(),
	structure['HWPTAG_PARA_LINE_SEG'] = HWPTAG_PARA_LINE_SEG(),
	structure['HWPTAG_PARA_RANGE_TAG'] = HWPTAG_PARA_RANGE_TAG(),
	structure['HWPTAG_CTRL_HEADER'] = reader.pop(4),
	structure['HWPTAG_LIST_HEADER'] = reader.pop(6),
	structure['HWPTAG_PAGE_DEF'] = reader.pop(40),
	structure['HWPTAG_FOOTNOTE_SHAPE'] = reader.pop(30),
	structure['HWPTAG_PAGE_BORDER_FILL'] = reader.pop(14),
	structure['HWPTAG_SHAPE_COMPONENT'] = reader.pop(4),
	structure['HWPTAG_TABLE'] = HWPTAG_TABLE(),
	structure['HWPTAG_SHAPE_COMPONENT_LINE'] = reader.pop(20),
	structure['HWPTAG_SHAPE_COMPONENT_RECTANGLE'] = reader.pop(9),
	structure['HWPTAG_SHAPE_COMPONENT_ELLIPSE'] = reader.pop(60),
	structure['HWPTAG_SHAPE_COMPONENT_ARC'] = reader.pop(25),
	structure['HWPTAG_SHAPE_COMPONENT_POLYGON'] = HWPTAG_SHAPE_COMPONENT_POLYGON(),
	structure['HWPTAG_SHAPE_COMPONENT_CURVE'] = HWPTAG_SHAPE_COMPONENT_CURVE(),
	structure['HWPTAG_SHAPE_COMPONENT_OLE'] = reader.pop(26),
	structure['HWPTAG_SHAPE_COMPONENT_PICTURE'] = HWPTAG_SHAPE_COMPONENT_PICTURE(),
	structure['HWPTAG_CTRL_DATA'] = HWPTAG_CTRL_DATA(),
	structure['HWPTAG_EQEDIT'] = HWPTAG_EQEDIT(),
	structure['HWPTAG_SHAPE_COMPONENT_TEXTART'] = HWPTAG_SHAPE_COMPONENT_TEXTART(),
	structure['HWPTAG_FORM_OBJECT'] = HWPTAG_FORM_OBJECT(),
	structure['HWPTAG_MEMO_SHAPE'] = reader.pop(22),
	structure['HWPTAG_MEMO_LIST'] = reader.pop(4),
	structure['HWPTAG_CHART_DATA'] = reader.pop(2),
	structure['HWPTAG_VIDEO_DATA'] = HWPTAG_VIDEO_DATA(),
	structure['HWPTAG_SHAPE_COMPONENT_UNKNOWN'] = reader.pop(36)
	
	def HWPTAG_PARA_TEXT():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_PARA_CHAR_SHAPE():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_PARA_LINE_SEG():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_PARA_RANGE_TAG():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_TABLE():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_SHAPE_COMPONENT_POLYGON():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_SHAPE_COMPONENT_CURVE():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_SHAPE_COMPONENT_PICTURE():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_CTRL_DATA():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_EQEDIT():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_SHAPE_COMPONENT_TEXTART():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_FORM_OBJECT():
		'''
		[TODO]
		미완.
		'''
		return
	
	def HWPTAG_VIDEO_DATA():
		'''
		[TODO]
		미완.
		'''
		return
	
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
	'''
	[TODO]
	Summary Information에 대한 자세한 설명은 MSDN을 참고라고 써있음. (12page)
	'''
	return structure

def scripts_jscriptversion():
	'''
	:path: Scripts/JScriptVersion
	:document: [hwp v5.0] 13page
	'''
	structure = {
		'HIGH' : None, #4
		'LOW' : None #4
	}
	'''
	[TODO]
	미완.
	'''
	return structure

def scripts_defaultjscript():
	'''
	:path: Scripts/DefalutJScript
	:document: [hwp v5.0] 13page
	'''
	structure = {
		'HEADER_LENGTH' : None, #4
		'HEADER' : None,
		'SOURCE_LENGTH' : None, #4
		'SOURCE' : None,
		'PRE_SOURCE_LENGTH' : None, #4
		'PRE_SOURCE' : None,
		'POST_SOURCE_LENGTH' : None, #4
		'POST_SOURCE' : None,
		'END_FLAG' : None #4
	}
	'''
	[TODO]
	미완.
	'''
	return structure


def xmltemplate_schemaname():
	'''
	:path: XMLTemplate/_SchemaName
	:document: [hwp v5.0] 14page
	'''
	structure = {
		'LENGTH' : None, #4
		'VALUE' : None # LENGTH * 2
	}
	'''
	[TODO]
	미완.
	'''
	return structure



def xmltemplate_schema():
	'''
	:path: XMLTemplate/Schema
	:document: [hwp v5.0] 14page
	'''
	structure = {
		'LENGTH' : None, #4
		'VALUE' : None # LENGTH * 2
	}
	'''
	[TODO]
	미완.
	'''
	return structure
	
def xmltemplate_instance():
	'''
	:path: XMLTemplate/Instance
	:document: [hwp v5.0] 14page
	'''
	structure = {
		'LENGTH' : None, #4
		'VALUE' : None # LENGTH * 2
	}
	'''
	[TODO]
	미완.
	'''
	return structure
	

def dochistory():
	return

def bibliography():
	return
	
	
	
	
	
	