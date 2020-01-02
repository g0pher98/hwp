

def load():
	f = open("test.hwp",'rb')
	return f.read()





# ======= 여기부터는 문서만 보고 우선적으로 개발한 부분 ====

def fileheader(raw):
	'''
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


