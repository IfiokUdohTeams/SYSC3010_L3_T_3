package com.example.covid_19labratorymonitoringsystem;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
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


public class Lab1 extends AppCompatActivity {
    Button button;
    TextView pressureL1;
    TextView tempL1;
    TextView pressurethreshL1;
    TextView tempthreshL1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lab1);

        button = findViewById(R.id.button);
        pressureL1 = findViewById(R.id.changepressure);
        tempL1 = findViewById(R.id.changetemp);
        pressurethreshL1 = findViewById(R.id.pressurethresh);
        tempthreshL1 = findViewById(R.id.tempthresh);
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                //add back end code
                ServerService.refresh.start();  //send op to refresh values
                while(ServerService.recvd.matches("")){

                }
                String recv = ServerService.recvd;
                String[] noComma = recv.split(",");
                tempL1.setText(noComma[0].split(":")[1]);
                pressureL1.setText(noComma[1].split(":")[1]);
                pressurethreshL1.setText(noComma[2].split(":")[1]);
                tempthreshL1.setText(noComma[3].split(":")[1]);
                ServerService.recvd = "";
            }
        });
    }
}