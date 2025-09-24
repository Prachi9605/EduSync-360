import { createContext, useContext, useState } from "react"
import { studentLogin } from "src/services/studentAPI.js"

const AuthContext = createContext()

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null)
  const [token, setToken] = useState(localStorage.getItem("token") || null)

  // Login
  const login = async (username, password) => {
    const data = await studentLogin(username, password)
    setUser({ username: data.username, name: data.name, id: data.user_id })
    setToken(data.token)
    localStorage.setItem("token", data.token)
    return data
  }

  // Logout
  const logout = () => {
    setUser(null)
    setToken(null)
    localStorage.removeItem("token")
  }

  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)
