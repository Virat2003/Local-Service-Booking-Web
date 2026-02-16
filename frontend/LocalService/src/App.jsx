import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Services from "./pages/Services";
import MyBookings from "./pages/MyBooking";
import CreateBooking from "./pages/CreateBooking";
import ProviderDashBoard from "./pages/ProviderDashBoard";
import PrivateRoute from "./components/PrivateRoute";
import Navbar from "./components/Navbar";
import Register from "./pages/Register";
import Profile from "./pages/Profile";
import HomePage from "./pages/HomePage";
import ProviderServices from "./pages/ProviderServices";

const App = () => {
  return (
    <>
      <BrowserRouter>
      <Navbar />
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/profile" element={ <PrivateRoute> <Profile /> </PrivateRoute> } />
          <Route path="/register" element={<Register />} />

          <Route path="/" element={<PrivateRoute> <HomePage /> </PrivateRoute> } />
          <Route path="/services" element={ <PrivateRoute> <Services /> </PrivateRoute> } />
          <Route path="/mybookings" element={ <PrivateRoute> < MyBookings />  </PrivateRoute>} />
          <Route path="/book/:serviceId" element={ <PrivateRoute> <CreateBooking /> </PrivateRoute> } />
          <Route path="/provider-dashboard" element={ <PrivateRoute>   <ProviderDashBoard /> </PrivateRoute> } />
          <Route path="/provider/services" element={ <PrivateRoute>   <ProviderServices /> </PrivateRoute> } />
          <Route path="/provider/services" element={ <PrivateRoute>   <ProviderServices /> </PrivateRoute> } />

        </Routes>
      </BrowserRouter>
      
      
    </>
  );
};

export default App;
