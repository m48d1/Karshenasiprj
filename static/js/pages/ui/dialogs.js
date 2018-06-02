$(function () {
    $('.js-sweetalert').on('click', function () {
        var type = $(this).data('type');
        if (type === 'basic') {
            showBasicMessage();
        }
        else if (type === 'with-title') {
            showWithTitleMessage();
        }
        else if (type === 'success') {
            showSuccessMessage();
        }
        else if (type === 'confirm') {
            showConfirmMessage();
        }
        else if (type === 'cancel') {
            showCancelMessage();
        }
        else if (type === 'with-custom-icon') {
            showWithCustomIconMessage();
        }
        else if (type === 'html-message') {
            showHtmlMessage();
        }
        else if (type === 'autoclose-timer') {
            showAutoCloseTimerMessage();
        }
        else if (type === 'prompt') {
            showPromptMessage();
        }
        else if (type === 'ajax-loader') {
            showAjaxLoaderMessage();
        }
        else if (type === 'ajax-loader2') {
            showAjaxLoaderMessage2();
        }
        else if (type === 'deleteprf') {
            var id = $(this).data('id');
            deleteprofessor(id);
        }
        else if (type === 'deletestd') {
            var id = $(this).data('id');
            deletestudent(id);
        }
        else if (type === 'deleteprj') {
            deleteproject(10);
        }
        else if (type === 'accept') {
            var id = $(this).data('id');
            acceptproject(id);
        }
        else if (type === 'editprf') {
            var id = $(this).data('id');
            editprofessor(id);
        }
        else if (type === 'editstd') {
            var id = $(this).data('id');
            editstudent(id);
        }
        else if (type === 'deadline') {
            var id = $(this).data('id');
            deadline(id);
        }
        else if (type === 'score') {
            var id = $(this).data('id');
            score(id);
        }
        else if (type === 'final') {
            var id = $(this).data('id');
            final(id);
        }
        else if (type === 'editprofileprof') {
            editprofileprof();
        }
        else if (type === 'editprofilestudent') {
            editprofilestudent();
        }
    });
});

//These codes takes from http://t4t5.github.io/sweetalert/
function showBasicMessage() {
    swal("Here's a message!");
}

function showWithTitleMessage() {
    swal("Here's a message!", "It's pretty, isn't it?");
}

function showSuccessMessage() {
    swal("Good job!", "You clicked the button!", "success");
}

function showConfirmMessage() {
    swal({
        title: "آیا از حذف پروژه اطمینان دارید",
        text: " نکته مهم : شما دیگر قادر به بازگرداندن آن نخواهید بود",
        type: "warning",
        showCancelButton: true,
        cancelButtonText: "خیر ، بستن پنجره",
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "بله، حذف کن",
        closeOnConfirm: false,
        showLoaderOnConfirm: true
    }, function () {
        swal("با موفقیت حذف شد", "شما میتوانید از طریق گزینه ایجاد پروژه ، پروژه جدیدی را ایجاد کنید", "success");
    });
}

function showCancelMessage() {
    swal({
        title: "Are you sure?",
        text: "You will not be able to recover this imaginary file!",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, delete it!",
        cancelButtonText: "No, cancel plx!",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (isConfirm) {
        if (isConfirm) {
            swal("Deleted!", "Your imaginary file has been deleted.", "success");
        } else {
            swal("Cancelled", "Your imaginary file is safe :)", "error");
        }
    });
}

function showWithCustomIconMessage() {
    swal({
        title: "Sweet!",
        text: "Here's a custom image.",
        imageUrl: "../../images/thumbs-up.png"
    });
}

function showHtmlMessage() {
    swal({
        title: "HTML <small>Title</small>!",
        text: "A custom <span style=\"color: #CC0000\">html<span> message.",
        html: true
    });
}

function showAutoCloseTimerMessage() {
    swal({
        title: "Auto close alert!",
        text: "I will close in 2 seconds.",
        timer: 2000,
        showConfirmButton: false
    });
}

function showPromptMessage() {
    swal({
        title: "An input!",
        text: "Write something interesting:",
        type: "input",
        showCancelButton: true,
        closeOnConfirm: false,
        animation: "slide-from-top",
        inputPlaceholder: "Write something"
    }, function (inputValue) {
        if (inputValue === false) return false;
        if (inputValue === "") {
            swal.showInputError("You need to write something!"); return false
        }
        swal("Nice!", "You wrote: " + inputValue, "success");
    });
}

function showAjaxLoaderMessage() {
    swal({
        title: "از اطلاعات وارد شده اطمینان دارید؟",
        text: "پس از ثبت این پروژه اطلاعات قابل تغییر نیست و تنها راه حذف این پروژه و درخواست مجدد خواهد بود .",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، ایجاد پروژه",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var Title = $("#Title").val();
        var Professor = $("#Professor").val();
        var Detail = $("#Detail").val();
        var Requirements = $("#Requirements").val();
        var TagofProject = $("#TagofProject").val();
        var serializeData =  { 'Title' : Title,'Professor' : Professor,'Detail' : Detail , 'Requirements' : Requirements , 'TagofProject' : TagofProject};
        $.ajax({
            url: "/Dashboard/AddProject/Add",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("پروژه با موفقیت ایجاد شد", "", "success");
                }
                else if (response == "Error2") {
                    swal("امکان ثبت چندین پروژه وجود ندارد", "", "error");
                }
                else
                    swal("اشکال در ایجاد پروژه", "", "error");
            }
        });
    });
}


function showAjaxLoaderMessage2() {
    swal({
        title: "از اطلاعات وارد شده اطمینان دارید؟",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، افزودن استاد",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var FullName = $("#FullName").val();
        var Group = $("#Group").val();
        var Email = $("#Email").val();
        var MobilePhone = $("#MobilePhone").val();
        var serializeData =  { 'FullName' : FullName,'Group' : Group , 'Email' : Email , 'MobilePhone' : MobilePhone};
        $.ajax({
            url: "/Dashboard/AddProfessor/Add",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("استاد با موفقیت افزوده شد", "", "success");

                }
                else
                    swal("اشکال در افزودن استاد", "", "error");
            }
        });
    });
}




function editprofessor(id) {
    swal({
        title: "از اطلاعات وارد شده اطمینان دارید؟",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، ثبت تغییرات",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var FullName = $("#" + ("FullName" + id).toString()).val();
        var Group = $("#" + ("Group" + id).toString()).val();
        var Email = $("#" + ("Email" + id).toString()).val();
        var MobilePhone = $("#" + ("MobilePhone" + id).toString()).val();
        var Username =  $("#" + ("Username" + id).toString()).val();
        var Password = $("#" + ("Password" + id).toString()).val();
        var serializeData =  {'Id' : id , 'FullName' : FullName,'Group' : Group , 'Email' : Email , 'MobilePhone' : MobilePhone , 'Username' : Username , 'Password' : Password};
        $.ajax({
            url: "/Dashboard/EditProfessor",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("تغییرات با موفقیت اعمال شد", "", "success");
                }
                else
                    swal("اشکال در اعمال تغییرات", "", "error");
            }
        });
    });
}

function editprofileprof() {
    swal({
        title: "از اطلاعات وارد شده اطمینان دارید؟",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، ثبت تغییرات",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var FullName = $("#FullName").val();
        var Email = $("#Email").val();
        var MobilePhone = $("#MobilePhone").val();
        var Username =  $("#Username").val();
        var Password = $("#Password").val();
        var serializeData =  { 'FullName' : FullName, 'Email' : Email , 'MobilePhone' : MobilePhone , 'Username' : Username , 'Password' : Password};
        $.ajax({
            url: "/Dashboard/EditProfileProf",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("تغییرات با موفقیت اعمال شد", "", "success");
                    re
                }
                else
                    swal("اشکال در اعمال تغییرات", "", "error");
            }
        });
    });
}


function editprofilestudent() {
    swal({
        title: "از اطلاعات وارد شده اطمینان دارید؟",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، ثبت تغییرات",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var FullName = $("#FullName").val();
        var StudentNumber = $("#StudentNumber").val();
        var Email = $("#Email").val();
        var MobilePhone = $("#MobilePhone").val();
        var Username =  $("#Username").val();
        var Password = $("#Password").val();
        var serializeData =  {'FullName' : FullName,'StudentNumber' : StudentNumber , 'Email' : Email , 'MobilePhone' : MobilePhone , 'Username' : Username , 'Password' : Password};
        $.ajax({
            url: "/Dashboard/EditProfileStudent",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("تغییرات با موفقیت اعمال شد", "", "success");
                }
                else
                    swal("اشکال در اعمال تغییرات", "", "error");
            }
        });
    });
}



function deleteprofessor(id) {

        swal({
        title: "آیا از حذف استاد اطمینان دارید ؟",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، حذف استاد",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var serializeData =  { 'Id' : id};
        $.ajax({
            url: "/Dashboard/DelProfessor",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("استاد با موفقیت حذف شد", "", "success");
                }
                else
                    swal("اشکال در حذف استاد", "", "error");
            }
        });
    });



}

function editstudent(id) {
    swal({
        title: "از اطلاعات وارد شده اطمینان دارید؟",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، ثبت تغییرات",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var FullName = $("#" + ("FullName" + id).toString()).val();
        var Field = $("#" + ("Field" + id).toString()).val();
        var Email = $("#" + ("Email" + id).toString()).val();
        var MobilePhone = $("#" + ("MobilePhone" + id).toString()).val();
        var Username =  $("#" + ("Username" + id).toString()).val();
        var Password = $("#" + ("Password" + id).toString()).val();
        var serializeData =  {'Id' : id , 'FullName' : FullName,'Group' : Group , 'Email' : Email , 'MobilePhone' : MobilePhone , 'Username' : Username , 'Password' : Password};
        $.ajax({
            url: "/Dashboard/EditStudent",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("تغییرات با موفقیت اعمال شد", "", "success");
                }
                else
                    swal("اشکال در اعمال تغییرات", "", "error");
            }
        });
    });
}

function deletestudent(id) {

        swal({
        title: "آیا از حذف استاد اطمینان دارید ؟",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، حذف استاد",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var serializeData =  { 'Id' : id};
        $.ajax({
            url: "/Dashboard/DelStudent",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("دانشجو با موفقیت حذف شد", "", "success");
                }
                else
                    swal("اشکال در حذف استاد", "", "error");
            }
        });
    });



}




function deleteproject(id) {

        swal({
        title: "آیا از حذف پروژه اطمینان دارید",
        text: " نکته مهم : شما دیگر قادر به بازگرداندن آن نخواهید بود",
        type: "warning",
        showCancelButton: true,
        cancelButtonText: "خیر ، بستن پنجره",
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "بله، حذف کن",
        closeOnConfirm: false,
        showLoaderOnConfirm: true
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var serializeData =  { 'Id' : id};
        $.ajax({
            url: "/Dashboard/DelProject",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("با موفقیت حذف شد", "شما میتوانید از طریق گزینه ایجاد پروژه ، پروژه جدیدی را ایجاد کنید", "success");
                }
                else
                    swal("اشکال در حذف پروژه", "", "error");
            }
        });
    });



}




function acceptproject(id) {
        swal({
        title: "آیا از تایید پروژه اطمینان دارید ؟",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، تایید پروژه",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var serializeData =  { 'Id' : id};
        $.ajax({
            url: "/Dashboard/AcceptProject",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("پروژه با موفقیت تایید شد", "", "success");
                }
                else
                    swal("اشکال در تایید پروژه", "", "error");
            }
        });
    });



}

function deadline(id) {
        swal({
        title: "آیا از اطلاعات وارد شده اطمینان دارید ؟",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، تعیین مشخصات تحویل",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var DeadlineDate = $("#" + ("DeadlineDate" + id).toString()).val();
        var DeadlineTime = $("#" + ("DeadlineTime" + id).toString()).val();
        var referee1 = $("#" + ("referee1" + id).toString()).val();
        var referee2 = $("#" + ("referee2" + id).toString()).val();
        var serializeData =  { 'Id' : id , 'DeadlineDate' : DeadlineDate ,'DeadlineTime' : DeadlineTime ,'referee1' : referee1 ,'referee2' : referee2};
        $.ajax({
            url: "/Dashboard/DeadLine",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("مشخصات تحویل پروژه با موفقیت ثبت شد", "", "success");
                }
                else
                    swal("اشکال در ثبت مشخصات تحویل پروژه", "", "error");
            }
        });
    });



}

function score(id) {
            swal({
        title: "آیا از اطلاعات وارد شده اطمینان دارید ؟",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، ثبت نمره",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var Score = $("#" + ("Score" + id).toString()).val();
        var serializeData =  { 'Id' : id , 'Score' : Score };
        $.ajax({
            url: "/Dashboard/Score",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("نمره با موفقیت ثبت شد", "", "success");
                }
                else
                    swal("اشکال در ثبت نمره پروژه", "", "error");
            }
        });
    });
}


function final(id) {
            swal({
        title: "آیا از اطلاعات وارد شده اطمینان دارید ؟",
        type: "info",
        showCancelButton: true,
        confirmButtonText: "بله ، نهایی سازی نمرات",
        cancelButtonText: "خیر ، بستن پنجره",
        closeOnConfirm: false,
        showLoaderOnConfirm: true,
    }, function () {
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
    }
});
        var serializeData =  { 'Id' : id };
        $.ajax({
            url: "/Dashboard/Final",
            type: "POST",
            data: serializeData,
            success: function(response) {
                if (response == "Success") {
                    swal("پروژه با موفقیت نهایی سازی شد", "", "success");
                }
                else
                    swal("اشکال در نهایی سازی پروژه", "", "error");
            }
        });
    });
}



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var _validFileExtensionsPresent = [".pdf"];
function ValidatePresentation(oForm) {
    var arrInputs = oForm.getElementsByTagName("input");
    for (var i = 0; i < arrInputs.length; i++) {
        var oInput = arrInputs[i];
        if (oInput.type == "file") {
            var sFileName = oInput.value;
            if (sFileName.length > 0) {
                var blnValid = false;
                for (var j = 0; j < _validFileExtensionsPresent.length; j++) {
                    var sCurExtension = _validFileExtensionsPresent[j];
                    if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                        blnValid = true;
                        break;
                    }
                }

                if (!blnValid) {
                    swal("اشکال در فرمت فایل ، فرمت فایل تنها می تواند PDF باشد", "", "error");
                    return false;
                }
            }
            else {
                    swal("فایلی برای آپلود انتخاب نشده است", "", "error");
                    return false;
            }
        }
    }

    return true;
}

var _validFileExtensionsProject = [".zip"];
function ValidateProject(oForm) {
    var arrInputs = oForm.getElementsByTagName("input");
    for (var i = 0; i < arrInputs.length; i++) {
        var oInput = arrInputs[i];
        if (oInput.type == "file") {
            var sFileName = oInput.value;
            if (sFileName.length > 0) {
                var blnValid = false;
                for (var j = 0; j < _validFileExtensionsProject.length; j++) {
                    var sCurExtension = _validFileExtensionsProject[j];
                    if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                        blnValid = true;
                        break;
                    }
                }

                if (!blnValid) {
                    swal("اشکال در فرمت فایل ، فرمت فایل تنها می تواند Zip باشد", "", "error");
                    return false;
                }
            }
            else {
                    swal("فایلی برای آپلود انتخاب نشده است", "", "error");
                    return false;
            }
        }
    }

    return true;
}

$(document).ready(function() {
    $(".DeadlineDate").pDatepicker({
        observer: true,
    format: 'YYYY/MM/DD',
    altField: '.observer-example-alt',
        initialValue: false
    });
  });