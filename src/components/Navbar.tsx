import React from 'react';
//import icon from './images/plane_icon128.png';

const Navbar: React.FC = () => {
    return (
        <div>
            <nav className='h-16 bg-gradient-to-b from-blue-600 to-blue-400'>
                <div className='text-3xl text-blue-50 font-bold pl-12 pt-3'>Flight Tracker</div>
            </nav>

        </div>
    );     
};

export default Navbar;
