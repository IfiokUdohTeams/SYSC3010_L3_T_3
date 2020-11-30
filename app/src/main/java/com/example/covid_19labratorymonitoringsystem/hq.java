package com.example.covid_19labratorymonitoringsystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class hq extends AppCompatActivity {
    Button submit;
    EditText HQ_pressure;
    EditText  HQ_temp;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hq);


        //When you click the button, the temeprature and pressure values should be dispalyed in the correct inputs of lab1 and lab2 classes
        //button id= submit
        //TextEdit for pressure id = HQ_P_Threshold
        //TextEdit for temperature id= HQ_T_Threshold

        submit = findViewById(R.id.submit);
        HQ_pressure = findViewById(R.id.HQ_P_Threshold);
        HQ_temp=findViewById(R.id.HQ_T_Threshold);

        submit.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                //add back end code
                String pressureVal = HQ_pressure.getText().toString();
                String tempVal = HQ_temp.getText().toString();
//                Log.v("press",pressureVal);
                if((pressureVal.matches("")  || tempVal.matches("")) == false){
                    ServerService.Submit("pressure:"+pressureVal+ "," + "temperature:"+tempVal+"\n");
                }
            }
        });
    }
}