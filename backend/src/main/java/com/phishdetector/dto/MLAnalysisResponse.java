package com.phishdetector.dto;

import java.util.List;

public class MLAnalysisResponse {
    private String url;
    private boolean phishing;
    private int score;
    private List<String> reasons;
    private boolean gsb;
    private boolean ml_pred;

    public MLAnalysisResponse() {

    }

    public MLAnalysisResponse(String url, boolean phishing, int score, List<String> reasons, boolean gsb, boolean ml_pred){
        this.url = url;
        this.phishing = phishing;
        this.score = score;
        this.reasons = reasons;
        this.gsb = gsb;
        this.ml_pred = ml_pred;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public boolean isPhishing() {
        return phishing;
    }

    public void setPhishing(boolean phishing) {
        this.phishing = phishing;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public List<String> getReasons() {
        return reasons;
    }

    public void setReasons(List<String> reasons) {
        this.reasons = reasons;
    }

    public boolean isGsb() {
        return gsb;
    }

    public void setGsb(boolean gsb) {
        this.gsb = gsb;
    }

    public boolean isMl_pred() {
        return ml_pred;
    }

    public void setMl_pred(boolean ml_pred) {
        this.ml_pred = ml_pred;
    }
}
