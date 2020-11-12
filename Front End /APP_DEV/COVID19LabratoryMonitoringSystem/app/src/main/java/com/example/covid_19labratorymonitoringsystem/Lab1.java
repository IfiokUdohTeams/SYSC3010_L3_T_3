package com.example.covid_19labratorymonitoringsystem;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;


public class Lab1 extends AppCompatActivity {



   /* @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lab1);
    }
*/


  /*  public void get_pressure(View view) {
        EditText myText = (EditText)findViewById(R.id.changepressure);
        String text = "here put the text that you want";
        myText.setText(text); //variable from point 2
    }*/



    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_lab1);


        //When you click the button, the temeprature and pressure values should say +/- X degrees
        //button id= button
        //TextEdit for pressure id = changepressure
        //TextEdit for temperature id= changetemp
        final Button button = findViewById(R.id.button);
        final TextView pressureL1 = findViewById(R.id.changepressure);
        final TextView tempL1=findViewById(R.id.changetemp);
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                //add back end code

                pressureL1.setText("degrees " );
                tempL1.setText("degrees " );
            }
        });
    }
}