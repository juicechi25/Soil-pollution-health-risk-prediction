function sendData() {
  const region = document.getElementById('regionInput').value;
  const pollutant = document.getElementById('pollutantType').value;
  const industry = document.getElementById('industry').value;

  if (!region || !pollutant || !industry) {
    document.getElementById('result').textContent = "⚠️ Please fill in all fields.";
    return;
  }

  fetch('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      region: region,
      pollutant_type: pollutant,
      nearby_industry: industry
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.prediction && data.confidence !== undefined) {
      document.getElementById('result').innerHTML =
        `✅ Prediction: <b>${data.prediction}</b><br>` +
        `📊 Confidence: <b>${data.confidence}%</b><br><br>` +
        `🧪 Full Risk Distribution:<pre>${JSON.stringify(data.distribution, null, 2)}</pre>`;
    } else if (data.error) {
      document.getElementById('result').textContent = `❌ Error: ${data.error}`;
    } else {
      document.getElementById('result').textContent = "❌ Unexpected response format.";
    }
  })
  .catch(err => {
    document.getElementById('result').textContent = "❌ Error fetching prediction.";
    console.error(err);
  });
}

