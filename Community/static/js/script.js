document.addEventListener('DOMContentLoaded', ()=> {
  function likePost(postId) {
    fetch(`/like/${postId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
        }
    }).then(response => response.json()).then(data => {
        document.querySelector(`#post-${postId} .like-count`).innerText = data.likes_count;
    });
};
});
