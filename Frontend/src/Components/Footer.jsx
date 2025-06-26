import React from "react";                          /*<------ import react library*/

const Footer = () => {
    return(
        <footer style={styles.footer}>
            <p>©️ 2025 FoodieBot. All rights reserved.</p>
        </footer>  
    );
};

const styles = {
    footer: {
      backgroundColor: '#4B0082',
      color: 'white',
      textAlign: 'center',
      padding: '0.75rem',
      position: 'fixed',
      width: '100%',
      bottom: 0,
    },
};  


export default Footer;