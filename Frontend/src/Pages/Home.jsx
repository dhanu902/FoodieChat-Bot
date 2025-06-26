import React from 'react';

const Home = () => {
    return(
        <main style={styles.main}>
            <h2>Welcome to FoodieBOT..!</h2>
            <p>Discover resturants near you using our intelligent Chatbot</p>
        </main>
    );
};

const styles = {
    main: {
      minHeight: '80vh',
      textAlign: 'center',
      padding: '0.75rem',
    },
};

export default Home;