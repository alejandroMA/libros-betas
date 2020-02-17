let deleteBtns = document.querySelectorAll('.delete-btn')

deleteBtns.forEach(deleteBtn => {
    deleteBtn.addEventListener('click', deleteBook)
})

async function deleteBook() {
    let id = this.dataset.id
    let permition = confirm(`¿Deseas eliminar el libro ${id}?`)

    if (!permition) return

    let headers = new Headers({ 'X-CSRFToken': getCookie('csrftoken') })
    let formData = new FormData()
    formData.append('id', id)
    let resquest = await fetch('/libro/delete/', {
        method: 'POST',
        headers: headers,
        body: formData
    })
    await resquest.json()

    window.location = '/'
}

function getCookie(name) {
    let cookieValue = null
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';')
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim()
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + '=') {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                )
                break
            }
        }
    }
    return cookieValue
}
