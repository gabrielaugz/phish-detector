package com.phishdetector.dto;

import java.time.LocalDateTime;

public class UrlAnalysisResponse {

    private String url;
    private boolean phishing;
    private LocalDateTime analyzedAt;

    public UrlAnalysisResponse() {
    }

    public UrlAnalysisResponse(String url, boolean phishing, LocalDateTime analyzedAt) {
        this.url = url;
        this.phishing = phishing;
        this.analyzedAt = analyzedAt;
    }

    public String getUrl() {
        return url;
    }

    public boolean isPhishing() {
        return phishing;
    }

    public LocalDateTime getAnalyzedAt() {
        return analyzedAt;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public void setPhishing(boolean phishing) {
        this.phishing = phishing;
    }

    public void setAnalyzedAt(LocalDateTime analyzedAt) {
        this.analyzedAt = analyzedAt;
    }
}

