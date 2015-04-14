$(document).ready(function() {
    $('select').material_select();

    $('select').on('change', function(event) {
        event.preventDefault();

        var value = $(this).val();

        if ( value == 'Todos') {
            $('div.congresista').show(600);
        } else {
            a = $('div.congresista');


            console.log(value);
            console.log($(a).length);

            for (var i = 0; i < a.length; i++ ) {
                $(a[i]).data('region');

                if ( $(a[i]).data('region') == value ) {
                    $(a[i]).show(600);
                } else {
                    $(a[i]).hide(600);
                }
            }
        };
    });
});
