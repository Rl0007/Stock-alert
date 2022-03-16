import logo from './logo.svg';
import './App.css';
import { Routes, Route, Link } from "react-router-dom";
import { Stockup } from './pages/stockup';
import { Navbar } from './components/navbar';
import { Stockdown } from './pages/stockdown';
import { Notify } from './pages/notify';


function App() {
  return (<>
  <Navbar/>

  <div className="container">
  <Routes>

  <Route path="/" element={<Stockup />}/>
  <Route path="/stockdown" element={<Stockdown />}/>  
  <Route path="/Notify" element={<Notify />}/>   

   
   </Routes>
   </div>
  </>);
}

export default App;
