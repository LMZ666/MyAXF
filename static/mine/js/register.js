$(function(){
    $('.register').width(innerWidth)
//    刷新图形验证码
    $.get("/imgcheck/",function(data){
        $("#imgcode").attr("src","/"+data)
    })
    $("#imgcode").click(function(){
        $.get("/imgcheck/",function(data){
        console.log(data)
        $("#imgcode").attr("src","/"+data)

    })
    })
//    检测输入是否符合要求
//    账号是否已经被注册过
    function success(this_){
        this_.parent().parent().addClass("has-success").removeClass("has-error")
            this_.next().removeClass("glyphicon-remove").addClass("glyphicon-ok").show()
    }
    function fail(this_){
        this_.parent().parent().removeClass("has-success").addClass("has-error")
            this_.next().removeClass("glyphicon-ok").addClass("glyphicon-remove").show()
        this_.val("")
    }

    $("#account").change(function(){
        data={"account":$(this).val()}
        var this_ = $(this)
        $.get("/account/",data,function(data){
            if(data.status == "1"){
                if(/^\d{6,12}$/.test(this_.val())){
                    success(this_)
                    $("#account").parent().next().hide()
                }
                else{
                    fail(this_)
                    $("#account").parent().next().html("账号格式不对")
                    $("#account").parent().next().show()
                }
            }
            else{
               fail(this_)
                $("#account").parent().next().html("账号已被注册")
                $("#account").parent().next().show()
            }
        })
    })
    // 两次密码的验证
    $("#passwd1").change(function(){
        if($(this).val().length>=6&&$(this).val().length<=12){
            success($(this))
        }
        else{
            fail($(this))
        }
    })
    $("#passwd2").change(function(){
        if($("#passwd1").val() === $("#passwd2").val()){
            success($(this))
        }
        else{
            fail($(this))
        }
    })
//    验证码
    $("#code").change(function(){
        if($.cookie("imgcode").toLowerCase() == $(this).val().toLowerCase()){
            success($(this))
        }
        else{
            $.get("/imgcheck/",function(data){
            console.log(data)
            $("#imgcode").attr("src","/"+data)
            })
            fail($(this))

        }
    })
//  昵称验证
    $("#name").change(function(){
        if($("#name").val().length>=2 && $("#name").val().length<=6){
            success($(this))
        }
        else{
            fail($(this))
        }
    })

})