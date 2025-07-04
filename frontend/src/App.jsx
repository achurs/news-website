import './App.css'
import Home from './Home.jsx'
import Header from './Header.jsx'
import Footer from './Footer.jsx'
import AllNews from './AllNews.jsx'
import { Route, Routes } from 'react-router-dom'
function App() {
  return (
    <>
    <Header />
    <div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/all" element={<AllNews />} />
        <Route path="*" element={<div>404 Not Found</div>} />
      </Routes>
    </div>
    <Footer />
    </>
  )
}

export default App
