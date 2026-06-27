import { useState, useRef, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { askQuestion } from '../api'
import './Chat.css'

const SUGGESTIONS = [
  'How many leaves do I have?',
  'What is my salary?',
  'Show my payslip',
  'What was my performance rating?',
  'What is the leave policy?',
  'Show my salary and leave balance',
]

export default function Chat() {
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      text: 'HEY THERE! I\'M YOUR HR ASSISTANT. ASK ME ANYTHING ABOUT YOUR LEAVES, SALARY, PAYSLIPS, PERFORMANCE, OR HR POLICIES.',
      sources: [],
    },
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const bottomRef = useRef(null)
  const navigate = useNavigate()
  const username = localStorage.getItem('username') || 'USER'

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const sendMessage = async (text) => {
    const question = text || input.trim()
    if (!question) return

    setMessages((prev) => [...prev, { role: 'user', text: question }])
    setInput('')
    setLoading(true)

    try {
      const res = await askQuestion(question)
      setMessages((prev) => [
        ...prev,
        { role: 'assistant', text: res.data.answer, sources: res.data.sources },
      ])
    } catch (err) {
      if (err.response?.status === 401) {
        localStorage.clear()
        navigate('/login')
      } else {
        setMessages((prev) => [
          ...prev,
          { role: 'assistant', text: 'ERROR: Could not process your request.', sources: [] },
        ])
      }
    } finally {
      setLoading(false)
    }
  }

  const handleLogout = () => {
    localStorage.clear()
    navigate('/login')
  }

  return (
    <div className="chat-page">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="sidebar-logo">
          <h2>HR<span>RAG</span></h2>
        </div>

        <div className="sidebar-user">
          <div className="user-badge">
            {username.charAt(0).toUpperCase()}
          </div>
          <div>
            <p className="user-name">{username.toUpperCase()}</p>
            <p className="user-role">EMPLOYEE</p>
          </div>
        </div>

        <div className="sidebar-section">
          <p className="section-label">QUICK QUESTIONS</p>
          {SUGGESTIONS.map((s, i) => (
            <button key={i} className="suggestion-btn" onClick={() => sendMessage(s)}>
              {s}
            </button>
          ))}
        </div>

        <button className="logout-btn" onClick={handleLogout}>
          LOGOUT →
        </button>
      </aside>

      {/* Main Chat */}
      <main className="chat-main">
        <div className="chat-topbar">
          <div className="topbar-title">
            <span className="dot yellow"></span>
            <span className="dot pink"></span>
            <span className="dot cyan"></span>
            <p>HR ASSISTANT CHAT</p>
          </div>
          <p className="topbar-status">● ONLINE</p>
        </div>

        <div className="messages-area">
          {messages.map((msg, i) => (
            <div key={i} className={`message ${msg.role}`}>
              <div className="message-label">
                {msg.role === 'user' ? username.toUpperCase() : 'HR BOT'}
              </div>
              <div className="message-bubble">
                {msg.text}
              </div>
              {msg.sources?.length > 0 && (
                <div className="sources">
                  {msg.sources.map((s, j) => (
                    <span key={j} className="source-tag">{s}</span>
                  ))}
                </div>
              )}
            </div>
          ))}

          {loading && (
            <div className="message assistant">
              <div className="message-label">HR BOT</div>
              <div className="message-bubble typing">
                <span></span><span></span><span></span>
              </div>
            </div>
          )}
          <div ref={bottomRef} />
        </div>

        <div className="chat-input-area">
          <input
            type="text"
            placeholder="ASK ANYTHING ABOUT YOUR HR DATA..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
            disabled={loading}
          />
          <button
            className="send-btn"
            onClick={() => sendMessage()}
            disabled={loading || !input.trim()}
          >
            SEND →
          </button>
        </div>
      </main>
    </div>
  )
}
