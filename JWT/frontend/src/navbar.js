import { useEffect, useState } from "react";

const NavBar = () => {

    const [name, setName] = useState("Tim");

    useEffect(() => {
        console.log("Cahnge chc")
    });
    return ( 
        <div className="nav-bar">
            <button onClick={() => setName("Andr")}>Change Name</button>
            <p>{ name }</p>
        </div>
     );
}
 
export default NavBar;