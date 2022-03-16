import React from 'react'

export const Alertgreen = ({message}) => {
 
     const [show, setShow] = useState(true);

  if (show) {
    return (
      <Alert variant="success" onClose={() => setShow(false)} dismissible>
        <Alert.Heading>Alert</Alert.Heading>
        <p>
       {message}
        </p>
      </Alert>
    );
  }
  return <Button onClick={() => setShow(true)}>Show Alert</Button>;
}
  

