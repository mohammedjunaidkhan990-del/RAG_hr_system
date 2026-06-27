import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8080',
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

export const login = (username, password) =>
  api.post('/auth/login', { username, password })

export const register = (username, password, department) =>
  api.post('/auth/register', { username, password, department })

export const askQuestion = (message) =>
  api.post('/api/ask', { message })

export default api
