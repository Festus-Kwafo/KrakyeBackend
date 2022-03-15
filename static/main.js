console.log("Hello Word")

$.ajax({
    type: 'GET',
    url: '/data-json',
    success: function(response){
        console.log(response)
    },
    error: function(error){
        console.log(error)
    } 
})



