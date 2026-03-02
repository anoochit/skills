const https = require('https');

const MANIFEST_URL = 'https://raw.githubusercontent.com/anoochit/uikits/refs/heads/master/lib/pages/templates_manifest.json';

https.get(MANIFEST_URL, (res) => {
  let data = '';
  res.on('data', (chunk) => { data += chunk; });
  res.on('end', () => {
    try {
      const templates = JSON.parse(data);
      console.log('Available Flutter UI Templates:');
      console.log('-------------------------------');
      templates.forEach(t => {
        console.log(`ID: ${t.id}`);
        console.log(`Title: ${t.title}`);
        console.log(`Description: ${t.description}`);
        console.log('---');
      });
    } catch (e) {
      console.error('Error parsing manifest:', e.message);
    }
  });
}).on('error', (err) => {
  console.error('Error fetching manifest:', err.message);
});
