import React, { useState } from 'react';
import { TextField, Button, Card, CardContent, Typography } from '@mui/material';

function UrlAnalyzer() {
  const [inputUrl, setInputUrl] = useState('');
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  const analyzeUrl = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8080/api/v1/url/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: inputUrl })
      });
      const data = await response.json();

      setHistory((prev) => [...prev, data]);
    } catch (error) {
      console.error('Erro ao analisar:', error);
    } finally {
      setLoading(false);
      setInputUrl('');
    }
  };

  return (
    <div style={{ margin: '20px' }}>
      <Typography variant="h4" gutterBottom>
        PhishDetector
      </Typography>
      <TextField
        label="URL"
        variant="outlined"
        value={inputUrl}
        onChange={(e) => setInputUrl(e.target.value)}
        style={{ marginRight: '10px', width: '400px' }}
      />
      <Button variant="contained" color="primary" onClick={analyzeUrl} disabled={loading}>
        {loading ? 'Analisando...' : 'Analisar'}
      </Button>

      <div style={{ marginTop: '20px' }}>
        <Typography variant="h5">Histórico</Typography>
        {history.length === 0 && <Typography>Nenhuma análise ainda.</Typography>}
        {history.map((item, i) => (
          <Card key={i} style={{ margin: '10px 0' }}>
            <CardContent>
              <Typography>URL: {item.url}</Typography>
              <Typography>Phishing: {item.phishing ? 'SIM' : 'NÃO'}</Typography>
              <Typography>Data/Hora: {item.analyzedAt}</Typography>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}

export default UrlAnalyzer;

