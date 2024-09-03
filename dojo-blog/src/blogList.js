const Blogs = ( props ) => {

    const blogs = props.blogs;
    const title = props.title;
    const handleDelete = props.handleDelete;

    return ( 
        <div className="blog-list">
            <h1>{ title }</h1>
            {blogs.map((blog) => (
            <div className="blog-preview" key={blog.id}>
                <h2>{ blog.title }</h2>
                <h3>{ blog.body }</h3>
                <p>Written by: { blog.author }</p>
                <button onClick={() => handleDelete(blog.id) }>Delete blog</button>
            </div>
       ))}    
        </div>
     );
}
 
export default Blogs;