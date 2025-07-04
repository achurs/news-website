import './Home.css'
import { useState, useEffect } from 'react'
import { io } from 'socket.io-client'
export default function Home() {
  const [msg, setMsg] = useState({})

  useEffect(() => {
    const socket = io('localhost:5000')
    socket.on('connect', () => {
      console.log('Connected to the server')
    })
    socket.on('message', (message) => {
      console.log('Received message:', message.title)
      setMsg({
        title: message.title,
        link: message.link,
        published: message.published
      })
    })
    // Cleanup function to disconnect the socket when the component unmounts
    return () => {
      socket.disconnect()
    }
  }, []);

  useEffect(() => {
    const footer = document.querySelector('footer');
    footer.style.position = 'fixed';
    footer.style.bottom = '0';
    footer.style.width = '100%';
  }, []);
  return (
    <>
      <div className="news-div">
        {msg.title ? (
          <div key={msg.title} className="news-item">
            <a href={msg.link} target="_blank" rel="noopener noreferrer" className='news-link' >
              <h3>{msg.title}</h3>
            </a>
            <p>Published: {new Date(msg.published).toDateString()}</p>
            <br />
          </div>
        ) : (
          <p className='no-msg'>No messages received yet.</p>
        )}
      </div>
    </>
  )
}
