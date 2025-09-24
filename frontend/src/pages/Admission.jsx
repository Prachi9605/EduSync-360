// src/pages/Admission.jsx
import { useState } from "react"
import { registerStudent } from "src/services/studentAPI.js"

function Admission() {
  const [name, setName] = useState("")
  const [newStudent, setNewStudent] = useState(null)
  const [error, setError] = useState("")

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const student = await registerStudent(name)
      setNewStudent(student)
      setError("")
      setName("")
    } catch (err) {
      setError(err.error || "Failed to register student")
    }
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h2 className="text-3xl font-bold mb-6">Student Admission</h2>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4 w-80">
        <input
          type="text"
          placeholder="Enter Student Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          className="border p-2 rounded"
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Register Student
        </button>
      </form>

      {error && (
        <p className="mt-4 text-red-600">{error}</p>
      )}

      {newStudent && (
        <div className="mt-6 p-4 bg-green-100 border border-green-400 rounded">
          <h3 className="font-semibold text-lg">🎉 Admission Successful!</h3>
          <p>Username: <span className="font-mono">{newStudent.username}</span></p>
          <p>Password: <span className="font-mono">{newStudent.password}</span></p>
          <p className="text-sm text-gray-500 mt-2">⚠️ Save these credentials to login later.</p>
        </div>
      )}
    </div>
  )
}

export default Admission
