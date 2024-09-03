document.addEventListener('DOMContentLoaded', () => {

  const nameInput = document.querySelector('input[name=Name]');
  const slugInput = document.querySelector('input[name=slug]');

  const slugify = (val) => {
    return val.toLowerCase().trim().toString()
    .replace(/&/g,'-and-')
    .replace(/[\s\W-]+/g,'-')
  };

  nameInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(nameInput.value));
  })

});
