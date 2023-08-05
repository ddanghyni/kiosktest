// src/utils/api.js
async function get(url) {
    const response = await fetch(url);
    return response.json();
  }
  
  async function post(url, data) {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    return response.json();
  }
  
  export { get, post };
  