import api, { setAuthToken } from "./api";

// Register function
export async function register(username, email, password, password2) {
    try {
        const response = await api.post("/auth/register/", {
            username,
            email,
            password,
            password2,
        });

        return response.data;
    } catch (error) {
        console.error("Registration failed:", error.response.data);
        throw error.response.data;
    }
}

// Login function
export async function login(username, password) {
    try {
        const response = await api.post("/auth/login/", {
            username,
            password,
        });

        const tokens = response.data; // {access, refresh}
        console.log("Tokens object:", tokens); // Log tokens
        console.log("Access token:", tokens.access);
        localStorage.setItem("access", tokens.access); // Save tokens
        localStorage.setItem("refresh", tokens.refresh);

        console.log(localStorage.getItem("access"));
        console.log(localStorage.getItem("refresh"));

        setAuthToken(tokens.access); // Set token for future requests
        return tokens;
    } catch (error) {
        console.error("Login failed:", error.response.data);
        throw error.response.data;
    }
}

// Logout function
export async function logout() {
  try {
    const response = await api.post("/auth/logout/", {});

    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    setAuthToken(null);
    return response.data;
  } catch (error) {
    console.error("Logout failed:", error.response.data);
    throw error.response.data;
  }
}
