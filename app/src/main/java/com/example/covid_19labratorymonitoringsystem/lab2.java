package com.example.covid_19labratorymonitoringsystem;
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

    // get threshold values from the database and do the math caluclation based on the current temperature/ pressure and the threshold.
    // the threshold is dipalyed using the edit text box.




//public class lab2 extends AppCompatActivity {
//    ServerSocket serverSocket;
//    Thread listenThread = null;
//    public static String SERVER_IP = "";
//    public static final int SERVER_PORT = 8080;
//    Button button;
//    TextView pressureL2;
//    TextView tempL2;
//    TextView pressurethreshL2;
//    TextView tempthreshL2;
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_lab2);
//        button = findViewById(R.id.buttonL2);
//        pressureL2 = findViewById(R.id.changepressureL2);
//        tempL2 = findViewById(R.id.changetempL2);
//        pressurethreshL2 = findViewById(R.id.pressurethreshL2);
//        tempthreshL2 = findViewById(R.id.tempthreshL2);
//
//        //When you click the button, the temeprature and pressure values should dispaly +/- X degrees
//        //button id= buttonL2
//        //TextEdit for pressure id = changepressureL2
//        //TextEdit for temperature id= changetempL2
//
//        try {
//            SERVER_IP = getLocalIpAddress();
//        } catch (UnknownHostException e) {
//            e.printStackTrace();
//        }
//        listenThread = new Thread(new listenThread());
//        listenThread.start();
//
//        button.setOnClickListener(new View.OnClickListener() {
//            public void onClick(View v) {
//                //add back end code
//                new Thread(new Refresh()).start();
////                pressureL2.setText("L2 degrees ");
////                tempL2.setText("L2 degrees ");
//            }
//        });
//    }
//
//        private String getLocalIpAddress() throws UnknownHostException{
//            WifiManager wifiManager = (WifiManager) getApplicationContext().getSystemService(WIFI_SERVICE);
//            assert wifiManager != null;
//            WifiInfo wifiInfo = wifiManager.getConnectionInfo();
//            int ipInt = wifiInfo.getIpAddress();
//            return InetAddress.getByAddress(ByteBuffer.allocate(4).order(ByteOrder.LITTLE_ENDIAN).putInt(ipInt).array()).getHostAddress();
//        }
//
//        private PrintWriter output;
//        private BufferedReader input;
//        class listenThread implements Runnable {
//            @Override
//            public void run() {
//                Socket socket;
//                try {
//                    serverSocket = new ServerSocket(SERVER_PORT);
//                    try {
//                        socket = serverSocket.accept();
//                        output = new PrintWriter(socket.getOutputStream());
//                        input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
//                    } catch (IOException e) {
//                        e.printStackTrace();
//                    }
//                } catch (IOException e) {
//                    e.printStackTrace();
//                }
//                while(true){
//                    try {
//                        String read = input.readLine();
//                        if (read != null) {
//                            process(read);
//                        }
//                    } catch (IOException e) {
//                    e.printStackTrace();
//                    }
//                }
//            }
//        }
//        // get threshold values from the database and do the math caluclation based on the current temperature/ pressure and the threshold.
//        // the threshold is dipalyed using the edit text box.
//
//
//    private void process(String read) {
//        String[] arrOfStr = read.split(":");
//        String op = arrOfStr[0];
//        String data = arrOfStr[1];
//
//        switch (op){
//            case "chngTempBy":
//                tempL2.setText(data);
//                break;
//            case "chngPressBy":
//                pressureL2.setText(data);
//                break;
//            case "PressThresh":
//                pressurethreshL2.setText(data);
//                break;
//            case "TempThresh":
//                tempthreshL2.setText(data);
//                break;
//
//        }
//
//    }
//
//    class Refresh implements Runnable{
//        @Override
//        public void run() {
//            output.write("R\n");
//            output.flush();
//        }
//    }
//
//}



/*
public class lab2 extends AppCompatActivity {
    ServerSocket serverSocket;
    Thread Thread1 = null;
    Thread Thread2 = null;
    TextView tvIP, tvPort;
    TextView tvMessages;
    EditText etMessage;
    Button btnSend;
    public static String SERVER_IP = "";
    public static final int SERVER_PORT = 8080;
    String message;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lab2);
        tvIP = findViewById(R.id.tvIP);
        tvPort = findViewById(R.id.tvPort);
        tvMessages = findViewById(R.id.tvMessages);
        etMessage = findViewById(R.id.etMessage);
        btnSend = findViewById(R.id.btnSend);
        try {
            SERVER_IP = getLocalIpAddress();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
        Thread1 = new Thread(new Thread1());
        Thread1.start();

        btnSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                message = etMessage.getText().toString().trim();
                if (!message.isEmpty()) {
                    new Thread(new Thread3(message)).start();
                }
            }
        });
    }
    private String getLocalIpAddress() throws UnknownHostException {
        WifiManager wifiManager = (WifiManager) getApplicationContext().getSystemService(WIFI_SERVICE);
        assert wifiManager != null;
        WifiInfo wifiInfo = wifiManager.getConnectionInfo();
        int ipInt = wifiInfo.getIpAddress();
        return InetAddress.getByAddress(ByteBuffer.allocate(4).order(ByteOrder.LITTLE_ENDIAN).putInt(ipInt).array()).getHostAddress();
    }
    private PrintWriter output;
    private BufferedReader input;
    class Thread1 implements Runnable {
        @Override
        public void run() {
            Socket socket;
            try {
                serverSocket = new ServerSocket(SERVER_PORT);
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        tvMessages.setText("Not connected");
                        tvIP.setText("IP: " + SERVER_IP);
                        tvPort.setText("Port: " + String.valueOf(SERVER_PORT));
                    }
                });
                try {
                    socket = serverSocket.accept();
                    output = new PrintWriter(socket.getOutputStream());
                    input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            tvMessages.setText("Connected\n");
                        }
                    });
                    new Thread(new Thread2()).start();

                } catch (IOException e) {
                    e.printStackTrace();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    private class Thread2 implements Runnable {
        @Override
        public void run() {
            while (true) {
                try {
                    final String message = input.readLine();
                    if (message != null) {
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                tvMessages.append("client:" + message + "\n");
                            }
                        });
                    }
                    else {
                        Thread1 = new Thread(new Thread1());
                        Thread1.start();
                        return;
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    class Thread3 implements Runnable {
        private String message;
        Thread3(String message) {
            this.message = message;
        }
        @Override
        public void run() {
            output.write(message);
            output.flush();
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    tvMessages.append("server: " + message + "\n");
                    etMessage.setText("");
                }
            });
        }
    }
}*/
