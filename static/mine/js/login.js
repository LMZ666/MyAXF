$(function(){
    // $("#subBtn").attr("disabled","disabled")
    $("#account").change(function(){
        {
        }

    })
    function fail(this_){
        this_.parent().parent().removeClass("has-success").addClass("has-error")
            this_.next().removeClass("glyphicon-ok").addClass("glyphicon-remove").show()
        this_.val("")
    }
    $("#subBtn").click(function(e){
        $("#account").parent().next().hide()
         $("#passwd").parent().next().hide()
        if($("#account").val().length>=6&&$("#account").length<=12&&$("#passwd").val().length>=6&&$("#account").length<=12){
            console.log("执行submit")
        }
        else{
            if(!($("#account").val().length>=6&&$("#account").length<=12)){
                fail($("#account"))
                $("#account").parent().next().html("账号6-12位数字")
                $("#account").parent().next().show()
            }
            if(!($("#passwd").val().length>=6&&$("#account").length<=12)){
                $("#passwd").parent().next().html("密码6-12位")
                $("#passwd").parent().next().show()
                fail($("#passwd"))
            }
            e.preventDefault()
        }
    })
})
