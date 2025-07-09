document.addEventListener("DOMContentLoaded", function () {
    var textarea = document.getElementById('id_body');
    if (textarea) {
        CKEDITOR.replace('id_body', {
            filebrowserUploadUrl: window.ckeditorUploadUrl,
            filebrowserBrowseUrl: window.ckeditorBrowseUrl,
            extraPlugins: 'uploadimage,image2',
            removePlugins: 'image',
            width: '100%',
            height: 300
        });
    }
});
