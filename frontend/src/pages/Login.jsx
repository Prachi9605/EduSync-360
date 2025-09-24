import { useAuth } from "../context/AuthContext"

function Login() {
  const { login } = useAuth()

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h2 className="text-3xl font-bold mb-6">Login</h2>

      <div className="flex flex-col gap-4">
        <button
          className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          onClick={() => login("Admin", "adminUser")}
        >
          Admin Login
        </button>

        <button
          className="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700"
          onClick={() => login("Teacher", "teacherUser")}
        >
          Teacher Login
        </button>

        <button
          className="px-6 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700"
          onClick={() => login("Student", "studentUser")}
        >
          Student Login
        </button>
      </div>
    </div>
  )
}

export default Login
