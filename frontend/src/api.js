import axios from 'axios';
axios.defaults.baseURL = import.meta.env.VITE_API_URL

// Create API instance
const api = axios.create({
    headers: {
        "Content-Type": "application/json",
    },
});

// Function to set Authorization token
export function setAuthToken(token) {
    if (token) {
        api.defaults.headers["Authorization"] = `Bearer ${token}`;
    } else {
        delete api.defaults.headers["Authorization"];
    }
}

export default api;
