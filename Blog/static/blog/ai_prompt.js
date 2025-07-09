ocument.getElementById('ask-ai-btn').addEventListener('click', async () => {
    const promptInput = document.querySelector('input[name="prompt"]');
    const titleInput = document.querySelector('input[name="title"]');
    const bodyTextarea = document.querySelector('textarea[name="body"]');
    const errorDiv = document.getElementById('ai-response-error');

    const prompt = promptInput.value.trim();

    if (!prompt) {
        errorDiv.textContent = "Введіть запит для генерації статті.";
        return;
    }
    errorDiv.textContent = "";

    try {
        const response = await fetch('/ask-ai/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({prompt}),
        });

        if (!response.ok) {
            const errorData = await response.json();
            errorDiv.textContent = errorData.error || "Помилка при генерації.";
            return;
        }

        const data = await response.json();

        // Заполняем title
        titleInput.value = data.title || "";

        // Заполняем body (textarea или CKEditor)
        if (typeof CKEDITOR !== 'undefined' && CKEDITOR.instances.body) {
            CKEDITOR.instances.body.setData(data.body || "");
        } else if (bodyTextarea) {
            bodyTextarea.value = data.body || "";
        }

    } catch (err) {
        errorDiv.textContent = "Помилка під час запиту до сервера.";
        console.error(err);
    }
});

// Функция для получения CSRF-токена из cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}