$(document).ready(function() {
    var taskId =  result ;  // Get the task ID from the rendered context

    function checkTaskStatus(taskId) {
//     console.log(document.location.origin + '/learn-celery-tutorial/check_task_status')
     console.log("TaskId = ",taskId)

        $.ajax({
            url: document.location.origin + '/learn-celery-tutorial/check_task_status',
//            url: "check_task_status/",
            data: {'task_id': taskId},
            dataType: 'json',
            success: function(data) {
                if (data.status === 'SUCCESS') {
                    $('#result').text(data.result);
                } else if (data.status === 'PENDING' || data.status === 'STARTED') {
                    setTimeout(function() {
                        checkTaskStatus(taskId);
                    }, 1000);
                } else {
                    $('#result').text('Task failed or unknown status');
                }
            },
            error: function() {
                $('#result').text('Error occurred while checking task status');
            }
        });
    }

    checkTaskStatus(taskId);
});