def fileheader(raw):
	'''
	:path: /FileHeader
	:document: hwp v5.0 8page
	'''
	data = {
		'signature' : raw[0:32],
		'version' : {
			'MM' : raw[32],
			'nn' : raw[33],
			'PP' : raw[34],
			'rr' : raw[35]
		},
		'문서 속성' : {
			'압축 여부' : None,
			'암호 설정 여부' : None,
			'배포용 문서 여부' : None,
			'스크립트 저장 여부' : None,
			'DRM 보안 문서 여부' : None,
			'XMLTemplate 스토리지 존재 여부' : None,
			'문서 이력 관리 존재 여부' : None,
			'전자 서명 정보 존재 여부' : None,
			'공인 인증서 암호화 여부' : None,
			'전자 서명 예비 저장 여부' : None,
			'공인 인증서 DRM 보안 문서 여부' : None,
			'CCL 문서 여부' : None,
			'모바일 최적화 여부' : None,
			'개인정보 보안 문서 여부' : None,
			'변경 추적 문서 여부' : None,
			'공공누리(KOGL) 저작권 문서' : None,
			'비디오 컨트롤 포함 여부' : None,
			'차례 필드 컨트롤 포함 여부' : None,
			'예약' : None
		},
		'저작권 속성' : {
			'CCL' : None,
			'복제 제한 여부' : None,
			'동일 조건 하에 복제 허가 여부' : None,
			'예약' : None
		},
		'EncryptVersion' : None,
		'공공누리(KOGL) 라이선스 지원 국가' : None,
		'예약' : None
	}
	return data

def docinfo(raw):
	'''
	:path: /DocInfo
	:document: hwp v5.0 9page
	'''
	data = {
		'HWPTAG_DOCUMENT_PROPERTIES' : 30,
		'HWPTAG_ID_MAPPINGS' : 32,
		'HWPTAG_BIN_DATA' : None,
		'HWPTAG_FACE_NAME' : None,
		'HWPTAG_BORDER_FILL' : None,
		'HWPTAG_CHAR_SHAPE' : 72,
		'HWPTAG_TAB_DEF' : 14,
		'HWPTAG_NUMBERING' : None,
		'HWPTAG_BULLET' : 10,
		'HWPTAG_PARA_SHAPE' : 54,
		'HWPTAG_STYLE' : None,
		'HWPTAG_MEMO_SHAPE' : 22,
		'HWPTAG_TRACK_CHANGE_AUTHOR' : None,
		'HWPTAG_TRACK_CHANGE' : None,
		'HWPTAG_DOC_DATA' : None,
		'HWPTAG_FORBIDDEN_CHAR' : None,
		'HWPTAG_COMPATIBLE_DOCUMENT' : 4,
		'HWPTAG_LAYOUT_COMPATIBILITY' : 20,
		'HWPTAG_DISTRIBUTE_DOC_DATA' : 256,
		'HWPTAG_TRACKCHANGE' : 1032
	}
	return data

def bodytext_section(raw):
	'''
	:path: /BodyText/SectionN
	:document: hwp v5.0 9-10page
	'''
	data = {
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
	return data

def hwpsummaryinformation():
	'''
	:path: /\005HwpSummaryInformation
	:document: hwp v5.0 12page
	'''
	data = {
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
	return data

