import { Link } from "react-router-dom"
import { useAuth } from "../context/AuthContext"

function Navbar() {
  const { user, logout } = useAuth()

  return (
    <nav className="bg-blue-600 text-white flex justify-between items-center px-6 py-4">
      <Link to="/" className="text-xl font-bold">EduSync360</Link>

      <div className="flex items-center gap-6">
        {!user ? (
          // Public links before login
          <>
            <Link to="/about" className="hover:underline">About Us</Link>
            <Link to="/courses" className="hover:underline">Courses</Link>
            <Link to="/results" className="hover:underline">Our Results</Link>
            <Link to="/admission" className="hover:underline">Registration</Link>
            <Link to="/contact" className="hover:underline">Contact Us</Link>
            <Link
              to="/login"
              className="bg-white text-blue-600 px-3 py-1 rounded hover:bg-gray-100"
            >
              Login
            </Link>
          </>
        ) : (
          // After login (show role + logout)
          <>
            <Link
              to={`/dashboard/${user.role}`}
              className="hover:underline capitalize"
            >
              {user.role} Dashboard
            </Link>
            <button
              onClick={logout}
              className="bg-red-500 px-3 py-1 rounded hover:bg-red-600"
            >
              Logout
            </button>
          </>
        )}
      </div>
    </nav>
  )
}

export default Navbar
