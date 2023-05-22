import axiosInstance from './index'

const axios = axiosInstance

export const getview = () => { return axios.get('http://localhost:8000/index') }
export const getscrapy = () => { return axios.get('http://localhost:8000/index/scrapy') }