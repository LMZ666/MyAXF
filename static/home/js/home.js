$(function () {
    // 隐藏滚动条后，导致页面过大的一个处理
    $('.home').width(innerWidth)
    new Swiper('#topSwiper', {
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        spaceBetween: 5,
      centeredSlides: true,
      autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
        loop: true,
    });


     new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        spaceBetween: 10,
         loop: true
    });
})