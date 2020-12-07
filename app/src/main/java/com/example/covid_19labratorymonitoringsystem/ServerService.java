package com.example.covid_19labratorymonitoringsystem;
/**
 * @author Ifiok Udoh
 *
 */

import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Binder;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.FilterOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public class ServerService extends Service {
    ServerSocket serverSocket;
    Thread listenThread = null;
    public static Thread refresh = new Thread(new Refresh());
//    public static Thread submit = new Thread(new Submit());
    public static String SERVER_IP = "";
    public static final int SERVER_PORT = 8080;
    public static String recvd = "";

    private String getLocalIpAddress() throws UnknownHostException{
        WifiManager wifiManager = (WifiManager) getApplicationContext().getSystemService(WIFI_SERVICE);
        assert wifiManager != null;
        WifiInfo wifiInfo = wifiManager.getConnectionInfo();
        int ipInt = wifiInfo.getIpAddress();
        return InetAddress.getByAddress(ByteBuffer.allocate(4).order(ByteOrder.LITTLE_ENDIAN).putInt(ipInt).array()).getHostAddress();
    }
    public static void Submit(String data){
        Submit t = new Submit();
        t.data = data;
        new Thread(t).start();
    }

    public static PrintWriter output;
    public static BufferedReader input;
    class listenThread implements Runnable {
        @Override
        public void run() {
            Socket socket;
            try {
                serverSocket = new ServerSocket(SERVER_PORT);
                try {
                    socket = serverSocket.accept();
                    output = new PrintWriter(socket.getOutputStream());
                    input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                } catch (IOException e) {
                    e.printStackTrace();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            while(true){
                try {
                    String read = input.readLine();
                    if (read != null) {
                        recvd = read;
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    static class Refresh implements Runnable{
//        private FilterOutputStream output = ;

        @Override
        public void run() {
            try {
                output.write("R\n");
                output.flush();
            }catch (NullPointerException e){
                e.printStackTrace();
            }

        }
    }

    static class Submit implements Runnable{
//        private FilterOutputStream output = ;
        public String data;
        @Override
        public void run() {
            try {
                output.write("S," +data);
                output.flush();
            }catch (NullPointerException e){
                e.printStackTrace();
            }

        }
    }


    /**
     * Class for clients to access.  Because we know this service always
     * runs in the same process as its clients, we don't need to deal with
     * IPC.
     */
    public class LocalBinder extends Binder {

        ServerService getService() {
            return ServerService.this;
        }
    }

    @Override
    public void onCreate() {
        // Display a notification about us starting.  We put an icon in the status bar.
//        showNotification();
        try {
            SERVER_IP = getLocalIpAddress();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
        listenThread = new Thread(new listenThread());
        listenThread.start();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        Log.i("LocalService", "Received start id " + startId + ": " + intent);
        return START_NOT_STICKY;
    }

    @Override
    public void onDestroy() {
    }

    @Override
    public IBinder onBind(Intent intent) {
        return mBinder;
    }

    // This is the object that receives interactions from clients.  See
    // RemoteService for a more complete example.
    private final IBinder mBinder = new LocalBinder();


}
