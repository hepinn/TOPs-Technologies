import './App.css'
import Lifecycle from './lifecycle'
import Menu from './Menu'
import LifecycleFunc from './LifecycleFunc'
import { BrowserRouter,Route,Routes} from 'react-router-dom'
import StyleComponent from './StyleComponent'
function App() {
  return (
    <>
      <div>
        
        
      <BrowserRouter>
        <Menu />
        <Routes>
            <Route path='/lifecycle' element={<Lifecycle />}></Route> 
            <Route path='/lifecyclefunc' element={<LifecycleFunc />}></Route> 
            <Route path='/StyleComponent' element={<StyleComponent />}></Route> 
        </Routes>

        </BrowserRouter>

        

      </div>
      
    </>
  )
}

export default App