import {redirect} from "react-router-dom";

const Api = {
    fetch(url, params = {}) {
        try {
            if (!url === '/api/token') {
                const token = localStorage.getItem('token');
                params = {...params, headers: {...params.headers, 'Authorization': `Bearer ${token}`}};
            }
        } catch (e) {
            return redirect('/login');
        }
        return fetch(`http://localhost:8000${url}`, params)
    }
}

export default Api;