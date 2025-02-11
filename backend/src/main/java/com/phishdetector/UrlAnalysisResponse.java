package com.phishdetector.dto;

import java.time.LocalDateTime;
import java.util.List;

public class UrlAnalysisResponse {
    private String url;
    private boolean phishing;
    private LocalDateTime analyzedAt;

    // Novos campos
    private Integer score;
    private List<String> reasons;

    public UrlAnalysisResponse() {}

    public UrlAnalysisResponse(String url, boolean phishing, LocalDateTime analyzedAt) {
        this.url = url;
        this.phishing = phishing;
        this.analyzedAt = analyzedAt;
    }

    // getters/setters
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

    // getters e setters para score e reasons
    public Integer getScore() {
        return score;
    }

    public void setScore(Integer score) {
        this.score = score;
    }

    public List<String> getReasons() {
        return reasons;
    }

    public void setReasons(List<String> reasons) {
        this.reasons = reasons;
    }
}
