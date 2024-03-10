import { useState } from 'react'
import './App.css'
import TinyMce from '../Components/TinyMce'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <TinyMce/>
    </>
  )
}

export default App
