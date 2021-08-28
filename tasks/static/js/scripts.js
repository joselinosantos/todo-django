$(document).ready(function() {
    let baseUrl = window.location.origin
    let deleteBtn = $('.delete-btn')
    let searchBtn = $('#search-btn')
    let searchForm = $('#search-form')
    var filter = $('#filter')

    //Confirm message before delete
    $(deleteBtn).on('click', function(e){
        e.preventDefault()

        let delLink = $(this).attr('href')
        let result = confirm('Quer realmente deletar essa tarefa?')

        if (result) {
            window.location.href = delLink
        }
    })

    //Search
    $(searchBtn).on('click', function(){
        searchForm.submit()
    })

    //Show Field select
    $('select').formSelect()

    //Change select
    $(filter).change(function() {
        var filter = $(this).val()
        window.location.href = baseUrl+'?filter='+filter
    })
})