$(function(){
	$('#search').keyup(function(){
		$.ajax({
			type: "POST",
			url: "/teams/search/",
			data: {
				'search_text' : $('#search').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType:'html'
		});

	});

});

function searchSuccess(data, textStatus, jqXHR)
{
	$('#search-result').html(data);
}
