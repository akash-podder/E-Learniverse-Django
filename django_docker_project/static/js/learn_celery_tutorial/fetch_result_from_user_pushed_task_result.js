$(document).ready(function() {
    var taskId =  result ;  // Get the task ID from the rendered context

    function checkTaskStatus(taskId) {
//     console.log(document.location.origin + '/learn-celery-tutorial/get_user_pushed_task_result')
        $.ajax({
            url: document.location.origin + '/learn-celery-tutorial/get_user_pushed_task_result',
            data: {'task_id': taskId},
            dataType: 'json',
            success: function(data) {
                $('#result').text(data.result);
            },
            error: function() {
                $('#result').text('Error occurred while checking task status');
            }
        });
    }

    checkTaskStatus(taskId);
});