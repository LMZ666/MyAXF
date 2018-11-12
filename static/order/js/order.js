$(function(){
    // $(".btn").click(function(){
    //
    // })
    $(".orderinfo").width(innerWidth)
    $("#pay").click(function(){
        console.log("支付")
        $.get("/pay/",{"identify":$(this).attr("identify")},function(data){
            window.open(data['alipay_url'],target="_self")
        })
    })
    $("ul").each(function(){
        var money=0
        $(this).find("li").each(function(){
            console.log($(this).find(".price"))
            money += parseInt($(this).find(".price").attr("price"))*parseInt($(this).find(".num").attr("num"))
        })
    $(this).next().html('总价:￥'+money)
    })
})