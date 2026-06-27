import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { register } from '../api'
import './Auth.css'

export default function Register() {
  const [form, setForm] = useState({ username: '', password: '', department: '' })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    try {
      const res = await register(form.username, form.password, form.department)
      localStorage.setItem('token', res.data.token)
      localStorage.setItem('username', res.data.username)
      localStorage.setItem('user_id', res.data.user_id)
      navigate('/chat')
    } catch (err) {
      setError(err.response?.data?.detail || 'Registration failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-header cyan">
          <h1>HR<span>RAG</span></h1>
          <p>CREATE YOUR ACCOUNT</p>
        </div>

        <form onSubmit={handleSubmit} className="auth-form">
          <div className="field">
            <label>USERNAME</label>
            <input
              type="text"
              placeholder="john_doe"
              value={form.username}
              onChange={(e) => setForm({ ...form, username: e.target.value })}
              required
            />
          </div>

          <div className="field">
            <label>PASSWORD</label>
            <input
              type="password"
              placeholder="••••••••"
              value={form.password}
              onChange={(e) => setForm({ ...form, password: e.target.value })}
              required
            />
          </div>

          <div className="field">
            <label>DEPARTMENT</label>
            <input
              type="text"
              placeholder="Engineering"
              value={form.department}
              onChange={(e) => setForm({ ...form, department: e.target.value })}
            />
          </div>

          {error && <div className="error-box">{error}</div>}

          <button type="submit" className="btn-cyan" disabled={loading}>
            {loading ? 'CREATING...' : 'REGISTER →'}
          </button>
        </form>

        <div className="auth-footer">
          <p>HAVE AN ACCOUNT? <Link to="/login">LOGIN HERE</Link></p>
        </div>
      </div>
    </div>
  )
}
