$(document).ready(function(){
    $('.tt').tooltip({delay: 50});
    $('.button-collapse').sideNav({
        menuWidth: 300, // Default is 300
        edge: 'left', // Choose the horizontal origin
        draggable: true
    });
    $('.toastmsg').each(function() {
        Materialize.toast($(this).text(), 5000);
        $(this).remove();
    });
    $('.modal').modal({
        dismissible: true, // Modal can be dismissed by clicking outside of the modal
        opacity: .8,
        endingTop: '2%'
    });
    setInterval(checkstatus, 30 * 1000);
});

function logout() {
    if (confirm('Are you sure you want to log out of the workshop application?\n\nCareful: If you do this, your progress will be deleted!')) {
        location.href = '/logout';
    }
}

function checkstatus() {
    if (location.pathname !== '/') {
        $.get('/check', function(data) {
            if (data.status === false) {
                location.href = '/';
            }
        })
    }
}