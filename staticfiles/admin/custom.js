(function ($) {
    $(document).ready(function () {
        console.log('erad')
        var techniqueSelect = $('.technique-select');
        var subTechniqueSelect = $('.sub-technique-select');

        techniqueSelect.on('change', function () {
            console.log('technique change')
            var selectedTechnique = $(this).val();
            subTechniqueSelect.empty();

            $.ajax({
                url: '/admin/get_subtechniques/',
                data: {
                    technique_id: selectedTechnique
                },
                success: function (data) {
                    var subTechniques = data.sub_techniques;
                    $.each(subTechniques, function (key, value) {
                        subTechniqueSelect.append('<option value="' + value.id + '">' + value.name + '</option>');
                    });
                }
            });
        });
        // Trigger change event on page load
        // techniqueSelect.trigger('change');
    });
})(django.jQuery);
