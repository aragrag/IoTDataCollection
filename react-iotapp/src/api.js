// api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/', // Remplacez par l'URL de votre API Django
});

export default api;
