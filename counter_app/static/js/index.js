const baseUrl = "http://localhost:8000"

const page = {
    init: function () {
        const submitButton = document.getElementById('submit-button');
        submitButton.addEventListener('click', this.submitForm);
    },

    submitForm: function (event) {
        event.preventDefault();

        const words = document.getElementById('words').value;

        const url = baseUrl + '/counter'
        $.ajax({
            type: 'POST',
            url: url,
            data: { words: words },
            success: function (response) {
                alert(response.word_count)
            },
            error: function (error) {
                alert('Error: ' + error.responseJSON.error_message);
            }
        });
    }
};
