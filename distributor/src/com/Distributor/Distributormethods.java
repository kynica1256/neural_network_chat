package com.Distributor;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;



// processBuilder.command("bash", "-c", "dir");
public class Distributormethods {

    public String func_process(String command) {

        ProcessBuilder processBuilder = new ProcessBuilder();

        // Run this on Windows, cmd, /c = terminate after this run
        processBuilder.command("cmd.exe", "/c", command);
        String data_ = "";
        try {
            Process process = processBuilder.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                data_ = data_ + line;
            }
            //int exitCode = process.waitFor();
            //System.out.println("\nExited with error code : " + exitCode);

        } catch (IOException e) {
            e.printStackTrace();
        }
        return data_;
    }
}
