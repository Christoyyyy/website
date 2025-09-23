package demo.jr.demoworld;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class todoservice {
    @Autowired
    private todorepositary todorepositary;



//    public todoservice(){
//        todorepositary = new todorepositary();
//    }
    public void printtodo(){
        System.out.printf( todorepositary.getallthetodo());
    }

}
