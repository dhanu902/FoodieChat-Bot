import React from 'react';
import Header from './Components/Header';
import Footer from './Components/Footer';
import Home from './Pages/Home';

const App = () => {
  return (
    <div style={styles.container}>
      <Header />
      <main style={styles.main}>
        <Home />
      </main>
      <Footer />
    </div>
  );
};

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100vh',
    backgroundColor: '#1e1e1e'
  },

  main: {
    flex: 1,
  },
};

export default App;