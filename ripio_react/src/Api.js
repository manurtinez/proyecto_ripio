const Api = {
    async fetch(url, params = {}) {
        try {
            if (url !== '/api/token') {
                const token = localStorage.getItem('token');
                params = {...params, headers: {...params.headers, 'Authorization': `Bearer ${token}`}};
            }
            const response = await fetch(`http://localhost:8000${url}`, params)
            if (!response.ok) {
                if (response.status === 401) {
                    alert('Por favor inicie sesion de nuevo')
                    window.location.href = '/login'
                    return false;
                }
                console.error(response)
                const data = await response.json()
                alert(Object.entries(data).map(([key, value]) => `${key}: ${value}`))
            } else {
                return response
            }
        } catch (e) {
            console.log(e)
        }
    }
}

export default Api;