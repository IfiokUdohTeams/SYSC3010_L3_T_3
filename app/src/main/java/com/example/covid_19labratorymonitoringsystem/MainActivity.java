package com.example.covid_19labratorymonitoringsystem;
/**
 * @author Zoya Mushtaq
 *
 */

import androidx.appcompat.app.AppCompatActivity;

import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    void startService(){
        startService(new Intent(this, ServerService.class));
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        startService();
    }

    /** Called when the user taps the Send button */
    public void goto_Lab1(View view) {
        Intent intent = new Intent(this, Lab1.class);
        startActivity(intent);
    }

    public void goto_Lab2(View view) {
        Intent intent = new Intent(this, lab2.class);
        startActivity(intent);
    }

    public void goto_hq(View view) {
        Intent intent = new Intent(this, hq.class);
        startActivity(intent);
    }
}
