import React, { useContext } from 'react';
import AuthContext from '../context/AuthContext';

const Signup = () => {
    const { SignupUser } = useContext(AuthContext);

    return (
        <form onSubmit={SignupUser} encType="multipart/form-data">
            <input type="text" name="first_name" placeholder="First Name" required />
            <input type="text" name="last_name" placeholder="Last Name" required />
            <input type="email" name="email" placeholder="Email" required />
            <input type="text" name="username" placeholder="Username" required />
            <input type="password" name="password" placeholder="Password" required />
            <input type="date" name="dateofbirth" placeholder="Date of Birth" />
            <input type="file" name="profilepic" accept="image/*" />
            <input type="file" name="coverpic" accept="image/*" />
            <button type="submit">Sign Up</button>
        </form>
    );
};

export default Signup;
