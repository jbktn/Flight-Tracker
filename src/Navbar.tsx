import React from 'react';

const Navbar: React.FC = () => {
    return (
        <nav className='h-16 bg-gradient-to-b from-blue-500 to-blue-300'>
            <div className='text-3xl text-blue-50 font-bold'>Flight Tracker</div>
        </nav>
    );
};

export default Navbar;
