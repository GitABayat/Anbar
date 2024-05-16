$(document).ready(function () {
	$('#fancy-file-upload').FancyFileUpload({
        params: {
            action: 'fileuploader'
        },
        maxfilesize: 1000000
    });

    $('#image-uploadify').imageuploadify();

    $('.single-select').select2({
        theme: 'bootstrap4',
        width: $(this).data('width') ? $(this).data('width') : $(this).hasClass('w-100') ? '100%' : 'style',
        placeholder: $(this).data('placeholder'),
        allowClear: Boolean($(this).data('allow-clear')),
    });
    $('.multiple-select').select2({
        theme: 'bootstrap4',
        width: $(this).data('width') ? $(this).data('width') : $(this).hasClass('w-100') ? '100%' : 'style',
        placeholder: $(this).data('placeholder'),
        allowClear: Boolean($(this).data('allow-clear')),
    });


    $(".mobile-toggle-menu").on("click", function () {
        $(".wrapper").addClass("toggled");
        $('#MasterTable').DataTable().ajax.reload();
    });
    // toggle menu button
    $(".toggle-icon").click(function () {
        $('#MasterTable').DataTable().ajax.reload();
        if ($(".wrapper").hasClass("toggled")) {
            // unpin sidebar when hovered
            $(".wrapper").removeClass("toggled");
            $(".sidebar-wrapper").unbind("hover");
        } else {
            $(".wrapper").addClass("toggled");
            $(".sidebar-wrapper").hover(function () {
                $(".wrapper").addClass("sidebar-hovered");
            }, function () {
                $(".wrapper").removeClass("sidebar-hovered");
            })
        }
    });

    /* Back To Top */
    $(document).ready(function () {
        $(window).on("scroll", function () {
            if ($(this).scrollTop() > 300) {
                $('.back-to-top').fadeIn();
            } else {
                $('.back-to-top').fadeOut();
            }
        });
        $('.back-to-top').on("click", function () {
            $("html, body").animate({
                scrollTop: 0
            }, 600);
            return false;
        });
    });
    // === sidebar menu activation js
    $(function () {
        for (var i = window.location, o = $(".metismenu li a").filter(function () {
            return this.href == i;
        }).addClass("").parent().addClass("mm-active"); ;) {
            if (!o.is("li")) break;
            o = o.parent("").addClass("mm-show").parent("").addClass("mm-active");
        }
    });

    $(function () {
        $('#menu').metisMenu();
    });

    // sidebar colors 


	$('#sidebarcolor1').click(theme1);
	$('#sidebarcolor2').click(theme2);
	$('#sidebarcolor3').click(theme3);
	$('#sidebarcolor4').click(theme4);
	$('#sidebarcolor5').click(theme5);
	$('#sidebarcolor6').click(theme6);
	$('#sidebarcolor7').click(theme7);
	$('#sidebarcolor8').click(theme8);

	function theme1() {
		$('html').attr('class', 'color-sidebar sidebarcolor1');
	}

	function theme2() {
		$('html').attr('class', 'color-sidebar sidebarcolor2');
	}

	function theme3() {
		$('html').attr('class', 'color-sidebar sidebarcolor3');
	}

	function theme4() {
		$('html').attr('class', 'color-sidebar sidebarcolor4');
	}

	function theme5() {
		$('html').attr('class', 'color-sidebar sidebarcolor5');
	}

	function theme6() {
		$('html').attr('class', 'color-sidebar sidebarcolor6');
	}

	function theme7() {
		$('html').attr('class', 'color-sidebar sidebarcolor7');
	}

	function theme8() {
		$('html').attr('class', 'color-sidebar sidebarcolor8');
	}
});