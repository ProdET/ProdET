 const { createProxyMiddleware } = require('http-proxy-middleware');

 const context = [
     "/products",
 ];

 module.exports = function (app) {
     const appProxy = createProxyMiddleware(context, {
         target: 'https://localhost:7122',
         secure: false
     });

     app.use(appProxy);
 };
