import axios from "axios"

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api"

// Register a new student
export const registerStudent = async (name) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/register_student/`, {
      name: name,
    })
    return response.data
  } catch (error) {
    console.error("Register student error:", error)
    throw error.response?.data || { error: "Something went wrong" }
  }
}

// Student login API
export const studentLogin = async (username, password) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/student_login/`, {
      username,
      password,
    })
    return response.data
  } catch (error) {
    console.error("Student login error:", error)
    throw error.response?.data || { error: "Something went wrong" }
  }
}
