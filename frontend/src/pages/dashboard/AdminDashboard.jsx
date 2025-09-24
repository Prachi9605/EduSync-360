import { useState } from "react"
import { useAuth } from "../../context/AuthContext"

function Admission() {
  const { registerStudent } = useAuth()
  const [name, setName] = useState("")
  const [credentials, setCredentials] = useState(null)

  const handleSubmit = (e) => {
    e.preventDefault()
    const creds = registerStudent(name)
    setCredentials(creds)
    setName("")
  }

  return (
    <div className="flex flex-col items-center p-6">
      <h2 className="text-3xl font-bold mb-6">Student Admission</h2>

      <form onSubmit={handleSubmit} className="flex flex-col gap-4 w-80">
        <input
          type="text"
          placeholder="Enter full name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          className="border p-2 rounded"
        />
        <button
          type="submit"
          className="bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
        >
          Register Student
        </button>
      </form>

      {credentials && (
        <div className="mt-6 bg-green-100 p-4 rounded shadow">
          <p className="font-semibold">🎉 Account Created!</p>
          <p>Username: <span className="font-mono">{credentials.username}</span></p>
          <p>Password: <span className="font-mono">{credentials.password}</span></p>
          <p className="text-sm text-gray-600">Please note these credentials for login.</p>
        </div>
      )}
    </div>
  )
}

export default Admission
