const https = require('https');

const MANIFEST_URL = 'https://raw.githubusercontent.com/anoochit/uikits/refs/heads/master/lib/pages/templates_manifest.json';
const BASE_URL = 'https://raw.githubusercontent.com/anoochit/uikits/refs/heads/master';

const templateId = process.argv[2];

if (!templateId) {
  console.error('Please provide a template ID.');
  process.exit(1);
}

https.get(MANIFEST_URL, (res) => {
  let data = '';
  res.on('data', (chunk) => { data += chunk; });
  res.on('end', () => {
    try {
      const templates = JSON.parse(data);
      const template = templates.find(t => t.id === templateId);
      if (!template) {
        console.error(`Template with ID "${templateId}" not found.`);
        process.exit(1);
      }

      const sourceUrl = BASE_URL + template.path;
      https.get(sourceUrl, (res) => {
        let sourceData = '';
        res.on('data', (chunk) => { sourceData += chunk; });
        res.on('end', () => {
          console.log(`Source for template "${template.title}":`);
          console.log('---');
          console.log(sourceData);
        });
      }).on('error', (err) => {
        console.error('Error fetching template source:', err.message);
      });

    } catch (e) {
      console.error('Error parsing manifest:', e.message);
    }
  });
}).on('error', (err) => {
  console.error('Error fetching manifest:', err.message);
});
