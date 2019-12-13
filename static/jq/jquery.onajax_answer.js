/**	\file	jq/jquery.onajax_answer.js
 *	\brief	Обработка результатов запроса $.ajax ({data: 'shstat=status&p_1=$p_1[&...]'});
 */
function	onAjaxSuccess (data)	/// Здесь мы получаем данные, отправленные сервером 'id_dom| Текст html [~id_dom_2| ...] ...'
{
	if  (data == 'submit') {
		document.mainForm.submit  ();
	} else {
		try {
			var arr = data.split  ('~');
			for  (var j in arr) {
				var vall = arr [j].split  ('|');
				if ('eval' == vall [0]) {
					eval (vall [1]);
				} else if ((vall [0] != '') && (document.getElementById(vall [0]))) {
					document.getElementById(vall [0]).innerHTML = vall [1];
				}
			}
		} catch (e) {
		//	console.log ('Ошибка ' + e.name + ":" + e.message + "\n" + e.stack);
			console.log ('Ошибка onAjaxSuccess ' + e.name + ': "' + e.message +'"');
		}
	}
}

function	onAjaxError (e, request, settings) {	/// Обработка ошибок
//	alert ("Error: " +e +", " +request +", " +settings +".");
	console.log ("Error: " +e +", " +request +", " +settings +".");
}

