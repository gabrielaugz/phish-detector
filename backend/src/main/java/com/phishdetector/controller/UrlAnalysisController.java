package com.phishdetector.controller;

import com.phishdetector.dto.AnalyzeUrlRequest;
import com.phishdetector.dto.UrlAnalysisResponse;
import com.phishdetector.service.UrlAnalysisService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@CrossOrigin(origins = "http://localhost:3000")
@RestController
@RequestMapping("/api/v1/url")
public class UrlAnalysisController {

    @Autowired
    private UrlAnalysisService urlAnalysisService;

    @PostMapping("/analyze")
    public ResponseEntity<UrlAnalysisResponse> analyzeUrl(@RequestBody AnalyzeUrlRequest request) {
        UrlAnalysisResponse result = urlAnalysisService.analyze(request.getUrl());
        return ResponseEntity.ok(result);
    }
}



