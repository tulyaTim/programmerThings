import { useState, useEffect } from "react";
import Blogs from "./blogList";

const Home = () => {

    const [blogs, setBlogs] = useState(null)

    const handleDelete = (id) => {
        const newBlogs =  blogs.filter(blog => blog.id !== id);
        setBlogs(newBlogs);
    }

    useEffect(() => {
        fetch('http://localhost:8000/blogs')
            .then(res => {
                return res.json();
            })
            .then(data => {
                setBlogs(data);
            }, []);
    })

    return ( 
        <div className="home">
           { blogs && < Blogs blogs={ blogs } title="Blogs" handleDelete={handleDelete}/>}
        </div>
        
     );
}
 
export default Home;