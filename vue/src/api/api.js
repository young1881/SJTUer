import axiosInstance from './index'

const axios = axiosInstance

export const getBooks = () => { return axios.get(`http://localhost:8000`) }
