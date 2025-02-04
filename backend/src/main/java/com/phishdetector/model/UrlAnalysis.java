package com.phishdetector.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "url_analysis")
public class UrlAnalysis {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String url;

    private Boolean isPhishing;

    private LocalDateTime analyzedAt;

    public UrlAnalysis() {
    }

    public UrlAnalysis(String url, Boolean isPhishing, LocalDateTime analyzedAt) {
        this.url = url;
        this.isPhishing = isPhishing;
        this.analyzedAt = analyzedAt;
    }

    public Long getId() {
        return id;
    }

    public String getUrl() {
        return url;
    }

    public Boolean getIsPhishing() {
        return isPhishing;
    }

    public LocalDateTime getAnalyzedAt() {
        return analyzedAt;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public void setIsPhishing(Boolean phishing) {
        isPhishing = phishing;
    }

    public void setAnalyzedAt(LocalDateTime analyzedAt) {
        this.analyzedAt = analyzedAt;
    }
}

