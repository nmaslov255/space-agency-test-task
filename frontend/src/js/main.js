import '../css/styles.scss'
import * as bootstrap from 'bootstrap'

import $ from 'jquery'

window.$ = $
window.jQuery = $

import 'slick-carousel'
import 'slick-carousel/slick/slick.css'
import 'slick-carousel/slick/slick-theme.css'


$(document).ready(function() {
  $('.slider-main').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    infinite: true,
    asNavFor: '.slider-nav',
    adaptiveHeight: true,
  })

  $('.slider-nav').slick({
    slidesToShow: 5,
    arrows: true,
    prevArrow: '<button class="slick-prev">&#8592;</button>',
    nextArrow: '<button class="slick-next">&#8594;</button>',
    slidesToScroll: 1,
    asNavFor: '.slider-main',
    focusOnSelect: true,
    infinite: true,
    centerMode: true,
    centerPadding: '0px',

    responsive: [
      {
        breakpoint: 992,
        settings: {
          arrows: false,
          centerPadding: null,
        }
      },
    ]
  })


  $('.slider-main img').on('click', function() {
    const src = $(this).attr('src')
    $('#modalPhoto').attr('src', src)
    new bootstrap.Modal('#photoModal').show()
  })
})