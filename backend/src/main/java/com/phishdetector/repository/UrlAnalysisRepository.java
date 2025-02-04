package com.phishdetector.repository;

import com.phishdetector.model.UrlAnalysis;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UrlAnalysisRepository extends JpaRepository<UrlAnalysis, Long> {

}

