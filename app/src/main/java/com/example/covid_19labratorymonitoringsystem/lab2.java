package com.example.covid_19labratorymonitoringsystem;

/**
 * @author Ifiok Udoh
 * @author Zoya Mushtaq
 *
 */
import androidx.appcompat.app.AppCompatActivity;

import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.annotation.SuppressLint;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.IBinder;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public class lab2 extends AppCompatActivity {
    Button button;
    TextView pressureL2;
    TextView tempL2;
    TextView pressurethreshL2;
    TextView tempthreshL2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lab2);
//        doBindService();
        button = findViewById(R.id.buttonL2);
        pressureL2 = findViewById(R.id.changepressureL2);
        tempL2 = findViewById(R.id.changetempL2);
        pressurethreshL2 = findViewById(R.id.pressurethreshL2);
        tempthreshL2 = findViewById(R.id.tempthreshL2);


        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                ServerService.refresh.start();  //send op to refresh values
                while(ServerService.recvd.matches("")){

                }
                String recv = ServerService.recvd;
                String[] noComma = recv.split(",");
                tempL2.setText(noComma[0].split(":")[1]);
                pressureL2.setText(noComma[1].split(":")[1]);
                pressurethreshL2.setText(noComma[2].split(":")[1]);
                tempthreshL2.setText(noComma[3].split(":")[1]);
                ServerService.recvd = "";
            }
        });
    }
}

