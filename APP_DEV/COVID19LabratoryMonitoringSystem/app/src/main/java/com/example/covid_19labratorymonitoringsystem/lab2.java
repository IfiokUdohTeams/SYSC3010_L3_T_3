package com.example.covid_19labratorymonitoringsystem;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.annotation.SuppressLint;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
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
    ServerSocket serverSocket;
    Thread Thread1 = null;
//    Thread Thread2 = null;
    TextView myIP, myPort;
    TextView recvMessage;
    EditText messageToSend;
    Button btnSend;
    public static String SERVER_IP = "";
    public static final int SERVER_PORT = 8080;
    String message;
    String message1 = "1, 12, 45";

    private String getLocalIpAddress() throws UnknownHostException {
        WifiManager wifiManager = (WifiManager) getApplicationContext().getSystemService(WIFI_SERVICE);
        assert wifiManager != null;
        WifiInfo wifiInfo = wifiManager.getConnectionInfo();
        int ipInt = wifiInfo.getIpAddress();
        return InetAddress.getByAddress(ByteBuffer.allocate(4).order(ByteOrder.LITTLE_ENDIAN).putInt(ipInt).array()).getHostAddress();
    }
    private PrintWriter output;
    private BufferedReader input;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lab2);
        myIP = findViewById(R.id.myIP);
        myPort = findViewById(R.id.myPort);
        recvMessage = findViewById(R.id.recvMessage);
        messageToSend = findViewById(R.id.messageToSend);
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
                new Thread(new Thread3()).start();
            }
        });
    }


//  Thread1 class to start server and start Thread2 to read from server socket
    class Thread1 implements Runnable {
        @Override
        public void run() {
            Socket socket;
            try {
                serverSocket = new ServerSocket(SERVER_PORT);
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        recvMessage.setText("Not connected");
                        myIP.setText("IP: " + SERVER_IP);
                        myPort.setText("Port: " + String.valueOf(SERVER_PORT));
                    }
                });
                try {
                    socket = serverSocket.accept();
                    output = new PrintWriter(socket.getOutputStream()); //output is used to send output from socket
                    input = new BufferedReader(new InputStreamReader(socket.getInputStream())); //Input is used to get input from socket
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            recvMessage.setText("Connected\n");
                        }
                    });
//                    new Thread(new Thread2()).start();

                } catch (IOException e) {
                    e.printStackTrace();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

//    //Thread2 to read from server socket
//    private class Thread2 implements Runnable {
//        @Override
//        public void run() {
//            while (true) {
//                try {
//                    final String message = input.readLine(); //read input from socket and assign to message
//                    if (message != null) {
//                        runOnUiThread(new Runnable() {
//                            @Override
//                            public void run() {
//                                tvMessages.append("client:" + message + "\n");
//                            }
//                        });
//                    }
//                    else {
//                        Thread1 = new Thread(new Thread1());
//                        Thread1.start();
//                        return;
//                    }
//                } catch (IOException e) {
//                    e.printStackTrace();
//                }
//            }
//        }
//    }
//
    //This sends message gotten from app to socket
    class Thread3 implements Runnable {
//        private String message;
//        Thread3(String message) {
//            this.message = message;
//        }
        @Override
        public void run() {
//            output.write(message);
//            output.flush();
            output.write(message1);
            output.flush();
//            output.write("done");
//            output.flush();

//            runOnUiThread(new Runnable() {
//                @Override
//                public void run() {
//                    tvMessages.append("server: " + message + "\n");
//                    etMessage.setText("");
//                }
//            });
        }
    }
}