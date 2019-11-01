
function get_len() {
	$.ajax({ type: "POST", url: "/ajax_html", data: $('form').serialize(), type: 'POST',
		success: function(response) {
			var json = jQuery.parseJSON(response)
			$('#len').html(json.len)
			console.log(response);
			},
		error: function(error) {
			console.log(error);
			}
	});
}
