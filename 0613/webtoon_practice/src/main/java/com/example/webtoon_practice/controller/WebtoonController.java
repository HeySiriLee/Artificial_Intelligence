package com.example.webtoon_practice.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class WebtoonController {
//    @GetMapping("/")
//    @ResponseBody

    @GetMapping("/main")
    public String Main() {
        return "main.html";
    }

    @GetMapping("/detail")
    public String Detail() {
        return "detail.html";
    }

    @GetMapping("/mypage")
    public String Mypage() {
        return "mypage.html";
    }

    @GetMapping("/login")
    public String Login() {
        return "login.html";
    }

    @GetMapping("/signup")
    public String Signup() {
        return "signup.html";
    }
}
