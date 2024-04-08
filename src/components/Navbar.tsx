import React from 'react';
import logo from '../images/plane_icon512.png';

const Navbar: React.FC = () => {
    return (
        <div>
            <nav className='h-16 bg-gradient-to-b from-blue-600 to-blue-400 flex'>
                <img src={logo} alt="logo" className='w-10 h-10 mt-3 ml-8' />
                <div className='text-3xl text-blue-50 font-bold pl-6 pt-3'>Flight Tracker</div>
            </nav>

        </div>
    );     
};

export default Navbar;
