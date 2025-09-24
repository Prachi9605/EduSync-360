import { Navigate } from "react-router-dom"
import { useAuth } from "../context/AuthContext"

/**
 * ProtectedRoute with optional role-based access
 * @param {ReactNode} children - Component(s) to render if allowed
 * @param {string|string[]} roles - Allowed role(s) (optional)
 */
function ProtectedRoute({ children, roles }) {
  const { token, user } = useAuth()

  // Not logged in → redirect to login
  if (!token) return <Navigate to="/login" replace />

  // If roles are defined, check user role
  if (roles) {
    const allowedRoles = Array.isArray(roles) ? roles : [roles]
    if (!allowedRoles.includes(user?.role)) {
      return <Navigate to="/" replace /> // redirect to home or error page
    }
  }

  return children
}

export default ProtectedRoute
