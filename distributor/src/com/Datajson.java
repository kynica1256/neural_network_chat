package com;
import java.util.*;

class Datajson {
  private Map<String, String> zero;
  public Map<String, String> getZero() {
    return zero;
  }
  public void setZero(Map<String, String> zero) {
    this.zero = zero;
  }
  @Override
  public String toString() {
    String tab_ = "\t";
    String control_json = "{\n\t\"0\":{";
    byte counter = 0;
    for (String key : zero.keySet()) {
      counter++;
      control_json = control_json + String.format("\n\t\t\"%s\":\"%s\"", key, zero.get(key));
      if (counter != zero.keySet().size()) {
        control_json += ",";
      }
    }
    control_json = control_json + "\n\t}\n}";
    return control_json;
  }
}
