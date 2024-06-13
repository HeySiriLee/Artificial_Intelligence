package com.example.webtoon_practice.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WebtoonApiController {
    @GetMapping("/api/ver")
    public String main() {
        return "{'API version': '1.2'}";
    }
}
