package demo.jr.demoworld;

import com.fasterxml.jackson.databind.annotation.JsonAppend;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/todo")

public class todocontroller {
    @Autowired
    private todoservice todoservice;
    @GetMapping("/get")
    String gettodo() {
        todoservice.printtodo();
        return "gettodo";
    }

    @GetMapping("/{id}")
    String gettodo2(@PathVariable long id) {
        return "get with id " + id;
    }
    @GetMapping("")
    String gettodo2param(@RequestParam long id) {
        return "get with id " + id;
    }
    @PostMapping("/create")
    String createtodo(@RequestBody String body){
        return body;
    }
}