import React from "react";                          /*<------ import react library*/

const Header = () => {
    return(
        <header style={styles.header}>
            <h1>FoodieBot 🍔</h1>
        </header>
    );
};

const styles = {
    header: {
        backgroundColor: '#4B0082',
        color: 'white',
        padding: '1rem',
        textAlign: 'center',    
    },
};

export default Header;