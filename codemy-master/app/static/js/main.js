function send(){
    q = $('textarea')[0].value
    $.post("/" , {"data":q} , success = success)
}

function success(response){
    url = document.location.href
    index = url.indexOf("/")
    url = url.slice(0 , index) + response
    document.location.href = url
}

$(".save").bind('click',send)