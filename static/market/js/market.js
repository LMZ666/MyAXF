$(function(){
    var type = $(".type-slider li")
    var index = $.cookie("index")
    // console.log(index)
    if($.cookie("index")){
        $(".type-slider li").eq(index).addClass('active')
    }
    else{
        $(".type-slider li").eq(0).addClass("active")
    }
    // 由于这是一个a标签，每次点击都会重新刷新页面，所以我们要记录下点击的位置，这就用到了jquery-cookie，这样的好处是在我们数据库中有大量的商品数据时，我们每次都只读取一少部分，大大缩短了响应时间
    type.click(function(){
        // print(type.index())

        //此处一定要设置过期时间和路径,3代表3天，path是存储路径，不设置会导致存不进去？？？？黑人问号刚开始我没有加上时间，然后点击同一个分类需要点击两次才能跳转我。。。。
        $.cookie("index",$(this).index(),{expires:3, path:'/'})
    })
    var catepory = $("nav ul li").first()
    cateporybtn = false
    orderbtn = false
    catepory.click(function(){
        cateporybtn=!cateporybtn
        orderbtn=false
        if (cateporybtn){
            catepory.find("i").removeClass("glyphicon-menu-up").addClass("glyphicon-menu-down")
            $("#typeview").show()
        }
        else{
            catepory.find("i").removeClass("glyphicon-menu-down").addClass("glyphicon-menu-up")
            $('#typeview').hide()
        }
    })

    var sortview = $("nav ul li").last()
    sortview.click(function(){
        cateporybtn = false
        orderbtn = !orderbtn
        if (orderbtn){
            sortview.find("i").removeClass("glyphicon-menu-up").addClass("glyphicon-menu-down")
            $("#sortview").show()
        }
        else{
            catepory.find("i").removeClass("glyphicon-menu-down").addClass("glyphicon-menu-up")
            $("#sortview").show()
        }

    })

    // 遍历一下.bt-wrapper .num里面如果有数据就会显示减号
    $(".bt-wrapper .num").each(function(){
        //parseInt可以截取字符串的数字部分
        // console.log($(this).html())
        if(parseInt($(this).html())){
            console.log($(this))
            $(this).prev().show()
        }
    })

    $(".plus").click(function(){
        var goodid = $(this).attr("goodid")
        $(this).prev().prev().show()
        $(this).prev().show()
        var this_=$(this)
        var data ={"goodid":goodid}
        $.get("/addcart/",data,function(data){
            if(data.login=="0"){
                window.open("/login/",target="_self")
            }
            this_.prev().html(data["cartnum"])
            console.log(this_.prev())
            console.log(data["cartnum"])
        })
    })
    $(".minus").click(function(){
        var this_ = $(this)
        var goodid = $(this).attr("goodid")
        var data = {"goodid":goodid}
        if(parseInt($(this).next().html())==1){
            this_.hide()
            this_.next().hide()
        }
        $.get("/minuscart/",data,function (data) {
            console.log(data)
            this_.next().html(data["cartnum"])
        })
    })


})