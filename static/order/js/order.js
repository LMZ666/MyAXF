$(function(){
    // $(".btn").click(function(){
    //
    // })
    $("ul").each(function(){
        var money=0
        $(this).find("li").each(function(){
            console.log($(this).find(".price"))
            money += parseInt($(this).find(".price").attr("price"))*parseInt($(this).find(".num").attr("num"))
        })
    $(this).next().html('总价:￥'+money)
    })
})