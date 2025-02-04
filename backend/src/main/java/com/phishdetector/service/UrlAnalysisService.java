package com.phishdetector.service;

import com.phishdetector.model.UrlAnalysis;
import com.phishdetector.repository.UrlAnalysisRepository;
import com.phishdetector.dto.UrlAnalysisResponse;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.*;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

@Service
public class UrlAnalysisService {

    @Autowired
    private UrlAnalysisRepository urlAnalysisRepository;

    private final RestTemplate restTemplate = new RestTemplate();
    private final String PYTHON_ML_URL = "http://localhost:5000/predict"; 

    public UrlAnalysisResponse analyze(String url) {
        // Chama o serviço python
        boolean isPhishing = analyzeUrl(url);

        // Salva no BD
        UrlAnalysis entity = new UrlAnalysis(url, isPhishing, LocalDateTime.now());
        urlAnalysisRepository.save(entity);

        // Monta response
        return new UrlAnalysisResponse(
            entity.getUrl(),
            entity.getIsPhishing(),
            entity.getAnalyzedAt()
        );
    }

    private boolean analyzeUrl(String url) {
        Map<String, String> requestBody = new HashMap<>();
        requestBody.put("url", url);

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<Map<String, String>> request = new HttpEntity<>(requestBody, headers);

        ResponseEntity<Map> response = restTemplate.postForEntity(
            PYTHON_ML_URL,
            request,
            Map.class
        );

        if (response.getBody() != null && response.getBody().get("phishing") != null) {
            return (boolean) response.getBody().get("phishing");
        }
        return false;
    }
}

