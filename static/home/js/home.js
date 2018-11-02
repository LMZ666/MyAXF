$(function () {
    // 隐藏滚动条后，导致页面过大的一个处理
    $('.home').width(innerWidth)
    new Swiper('#topSwiper', {
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        paginationClickable: true,
        spaceBetween: 5,
        centeredSlides: true,
        autoplayDisableOnInteraction: false,
        loop: true,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
    });


     new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        spaceBetween: 10,
         loop: true
    });
})