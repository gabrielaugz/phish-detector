package com.phishdetector.dto;

public class AnalyzeUrlRequest {

    private String url;

    public AnalyzeUrlRequest() {
    }

    public AnalyzeUrlRequest(String url) {
        this.url = url;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
}

