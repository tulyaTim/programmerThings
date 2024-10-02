import { createContext, useEffect, useState } from 'react';
import { jwtDecode } from 'jwt-decode';
import { useNavigate } from 'react-router-dom'

const AuthContext = createContext();


export default AuthContext;

export const AuthProvider = ({ children }) => {
 
    let [authTokens, setAuthTokens] = useState(() => localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null);
    let [user, setUser] = useState(() => localStorage.getItem('authTokens') ? jwtDecode(localStorage.getItem('authTokens')) : null);
    let [loading, setLoading] = useState(true)

    const navigate = useNavigate()

    let SignupUser = async (e) => {
        e.preventDefault(); // Prevent form refresh
    
        let formData = new FormData();
        formData.append('first_name', e.target.first_name.value);
        formData.append('last_name', e.target.last_name.value);
        formData.append('email', e.target.email.value);
        formData.append('username', e.target.username.value);
        formData.append('password', e.target.password.value);
        formData.append('dateofbirth', e.target.dateofbirth.value);
        formData.append('profilepic', e.target.profilepic.files[0]); 
        formData.append('coverpic', e.target.coverpic.files[0]);    
    
        let response = await fetch('http://127.0.0.1:8000/api/signup/', {
            method: 'POST',
            body: formData, // Pass formData for multipart form request
        });
    
        if (response.ok) {
            console.log("User signed up successfully");
            navigate('/login'); // Redirect to login 
        } else {
            alert('Signup failed');
            console.log("error", response.errors)
        }
        const result = await response.json();
    

    };


    let loginUser = async (e) => {
        e.preventDefault(); // Prevents form from refreshing the page

        let response = await fetch('http://127.0.0.1:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'username': e.target.username.value,
                'password': e.target.password.value,
            }),
        });

        if (response.ok) { // Check if the response is okay (status in the range 200-299)
            let data = await response.json();

            setAuthTokens(data);
            setUser(jwtDecode(data.access));
            localStorage.setItem('authTokens', JSON.stringify(data))
            navigate('/')
        } else {
            alert('Login failed');
        }
    };

    let logoutUser = () => {
        setAuthTokens(null);
        setUser(null);
        localStorage.removeItem('authTokens')
        navigate('/login')
    }

    let updateToken = async ()=> {
        let response = await fetch('http://127.0.0.1:8000/api/token/refresh/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({'refresh':authTokens.refresh}),
        });

        if (response.ok) { // Check if the response is okay (status in the range 200-299)
            let data = await response.json();

            setAuthTokens(data);
            setUser(jwtDecode(data.access));
            localStorage.setItem('authTokens', JSON.stringify(data))
        } else {
            logoutUser()
        }
    }

    const [name, setName] = useState('');
    const [proficiency, setProficiency] = useState(1);

    const AddSkills = async (e) => {
        e.preventDefault();
    
        const token = localStorage.getItem('access_token');  // Get the access token
        if (!token) {
            alert('User not authenticated');
            return;
        }
    
        try {
            let response = await fetch('http://127.0.0.1:8000/api/skills/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`  // Add token to headers
                },
                body: JSON.stringify({
                    'name': e.target.name.value,        // Use correct field names from your API
                    'proficiency_level': e.target.proficiency_level.value,  // Adjust proficiency field name as well
                }),
            });
    
            if (response.ok) {  // Check for successful response
                let data = await response.json();
                console.log('Skill added successfully', data);
    
                // Reset form after success
                setName('');
                setProficiency(1);
            } else {
                // Handle failure
                let errorData = await response.json();
                console.error('Failed to add skill:', errorData);
                alert('Skill Adding failed: ' + errorData.message);
            }
        } catch (error) {
            console.error('An error occurred:', error);
            alert('An error occurred while adding skill');
        }
    };
    

    let contextData = {
        user: user,
        authTokens: authTokens,
        SignupUser: SignupUser,
        loginUser: loginUser,
        logoutUser: logoutUser,
        AddSkills: AddSkills,
    };

    useEffect(()=>{

        let fourMinutes = 1000 * 60 * 4;
        let interval = setInterval(()=> {
            if(authTokens){
                updateToken()
            }
        }, fourMinutes)
        return ()=> clearInterval(interval)
        
    }, [authTokens, loading])

    return (
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    );
};
