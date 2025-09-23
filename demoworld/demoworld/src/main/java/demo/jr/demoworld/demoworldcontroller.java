package demo.jr.demoworld;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class demoworldcontroller {
    @GetMapping("/hello")
    String gethelloworld(){
        return "Hello World";

    }

}
