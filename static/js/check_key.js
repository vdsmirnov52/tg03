
function	intkey(event) {	// фильтр на ввод - только цифры 0-9
	var	chCode = ('charCode' in event) ? event.charCode : event.keyCode;
	return (chCode < 32 || chCode >= 48 && chCode <= 57);   /* '0' - '9' */
	}
function	ip_key(event) {	// IP addres & Domen name
	var	chCode = ('charCode' in event) ? event.charCode : event.keyCode;
	return (chCode < 32 || chCode == 46 || chCode >= 48 && chCode <= 57 || chCode > 64 && chCode < 123)
	}

