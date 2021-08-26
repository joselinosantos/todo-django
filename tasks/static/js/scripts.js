$(document).ready(function() {
    var deleteBtn = $('.delete-btn')
    var searchBtn = $('#search-btn')
    var searchForm = $('#search-form')

    //Confirm message before delete
    $(deleteBtn).on('click', function(e){
        e.preventDefault()

        var delLink = $(this).attr('href')
        var result = confirm('Quer deletar essa tarefa')

        if (result) {
            window.location.href = delLink
        }
    })

    //Search
    $(searchBtn).on('click', function(){
        searchForm.submit()
    })
})