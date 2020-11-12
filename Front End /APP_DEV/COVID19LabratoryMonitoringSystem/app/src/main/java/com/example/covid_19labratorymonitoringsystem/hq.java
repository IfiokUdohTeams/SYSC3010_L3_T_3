package com.example.covid_19labratorymonitoringsystem;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class hq extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hq);


        //When you click the button, the temeprature and pressure values should be dispalyed in the correct inputs of lab1 and lab2 classes
        //button id= submit
        //TextEdit for pressure id = HQ_P_Threshold
        //TextEdit for temperature id= HQ_T_Threshold

        final Button submit = findViewById(R.id.submit);
        final EditText HQ_pressure = findViewById(R.id.HQ_P_Threshold);
        final EditText  HQ_temp=findViewById(R.id.HQ_T_Threshold);
        submit.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                //add back end code
                String pressureVal = HQ_pressure.getText().toString();
                String tempVal = HQ_temp.getText().toString();



            }
        });
    }
}