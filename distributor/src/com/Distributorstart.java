package com;

import com.Distributor.Distributormethods;

import java.io.*;
import java.util.*;
import java.util.Base64;

import java.io.BufferedReader;
import java.lang.reflect.Type;
import com.google.gson.reflect.TypeToken;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;


// processBuilder.command("bash", "-c", "dir");
public class Distributorstart {
  static String path_users_data = String.format("%1$sUsers_data%1$s" ,File.separator);
  static String path_java = String.format("%1$sdistributor%1$sout" ,File.separator);




  public static void workwithdata(int id, String text_start, String text_finish) {

    Gson gson = new Gson();

    String id_ = Integer.toString(id);
    String separator = File.separator;


    String work_path = System.getProperty("user.dir");
    String path_ = work_path.replace(path_java,"")+path_users_data+id_+"_data.json";

    try {
      File file_obj = new File(path_);
      BufferedReader br = new BufferedReader(new FileReader(file_obj));
      String all_text = "";
      String line;
      while ((line = br.readLine()) != null) {
        all_text += line;
      }
      all_text = all_text.replace("0", "zero");
      //Type type = new TypeToken<Map<String, String>>(){}.getType();
      //Map<String, String> myMap = gson.fromJson("{'k1':'apple','k2':'orange'}", type);
      //System.out.println(myMap);
      Datajson data_ = gson.fromJson(all_text, Datajson.class);
      //data_.toString();
      Map<String, String> zero = new HashMap<>();
      zero.putAll(data_.getZero());
      zero.put(text_start, text_finish);
      data_.setZero(zero);


      FileWriter writer = new FileWriter(file_obj, false);
      writer.write(data_.toString());
      writer.flush();

    } catch (IOException ioe) {
      ioe.printStackTrace();
    }

  }
  public static void main(String[] args) {
    int id_ = Integer.parseInt(args[0]);
    String text = args[1];
    String type_ = args[2];
    Distributormethods dm = new Distributormethods();
    //System.out.println(String.format("cd ../../nn_other && python kernel_nn.py %s \"%s\" %s", type_, text, id_));
    String out_sys = dm.func_process(String.format("cd ../../nn_other && python kernel_nn.py %s \"%s\" %s", type_, text, id_));
    if (type_ == "train") {
      System.exit(0);
    }
    String data_for_decode = out_sys.substring(out_sys.indexOf("{")+1, out_sys.indexOf("}"));
    Base64.Decoder decoder = Base64.getDecoder();
    String decoded = new String(decoder.decode(data_for_decode));

    System.out.println(decoded);
    workwithdata(id_, text, decoded);
  }
}
