$(document).ready(function(){

    function getNumberFromCache(){
        $.ajax({
            url: document.location.origin + '/learn-celery-tutorial/get_counter_number_from_cache',
            dataType: 'json',
            success: function(data){
                if(data.result == null){
                    $('#result').text('Task failed or unknown status from CACHE...See Console.log for Reason');
                    console.log("celery BEAT application is NOT RUNNING or Cannot connected to Redis Server");
//                    setTimeout(function() {
//                        getNumberFromCache();
//                    }, 3000);
                }
                else{
                    console.log("New Number = ", data.result);
                    $('#result').text(data.result);
                    setTimeout(function() {
                        getNumberFromCache();
                    }, 3000);
                }
            },

            error:function(){
                $('#result').text('Error occurred while fetching from CACHE');
            }

        });
    }

    setTimeout(function() {
        console.log('First Call to `get_counter_number_from_cache` API ');
        getNumberFromCache();
    }, 3000);
});