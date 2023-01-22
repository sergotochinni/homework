package Programmer.familiarityWithJava.homeWork2;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.util.logging.*;
import java.net.URL;
import java.util.Scanner;

public class task1 {

    // Напишите программу, которая
    // 1) по указанной строке URL скачивает файл и возвращает строковое содержимое файла
    // 2) изменяет строковое содержимое файла подставляя по маске "%s" ваше имя
    // 3) сохраняет файл локально
    // 4) читает сохраненный файл и выводит содержимое в логгер
    // 5) удаляет сохраненный файл
    public static void main(String[] args) throws IOException {
        Logger lg = Logger.getLogger(task1.class.getName());
        FileHandler fh = new FileHandler("log.txt");
        lg.addHandler(fh);
        SimpleFormatter sf = new SimpleFormatter();
        fh.setFormatter(sf);
        String fileUrl = "https://raw.githubusercontent.com/aksodar/JSeminar_2/master/src/main/resources/example.txt";
        File file = new File(fileUrl);
        String fileName = file.getName();
        // 1
        String fileBody = download(fileUrl);
        // 2
        fileBody = change("Sergey", fileBody);
        // 3
        saveOnLocal(fileName, fileBody);
        // 4
        fileBody = read(fileName);
        lg.info(fileBody);
        // 5
        removeFromLocale(fileName);
        
        
    }

    public static String download(String url) throws IOException {
        URL urlForDownload = new URL(url);
        InputStream is = urlForDownload.openStream();
        ByteArrayOutputStream bo = new ByteArrayOutputStream();
        byte[] buf = new byte[10];
        while(true){
            int nReaded = is.read(buf);
            if (nReaded == -1){
                break;
            }
            bo.write(buf, 0, nReaded);
        }
        return bo.toString();
    }
    
    public static String change(String name, String fileContent) {
        return String.format(fileContent, name);
    }
    
public static String read(String localFilename){
    String data = "";
    try {
        File myObj = new File(localFilename);
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
        data += myReader.nextLine();
        }
        myReader.close();
    } catch (FileNotFoundException e) {
        System.out.println("An error occurred.");
        e.printStackTrace();
    }
    return data;
}
    
    public static void saveOnLocal(String fileName, String fileContent) {
        File file = new File(fileName);
        FileWriter fr = null;
        try {
            fr = new FileWriter(file);
            fr.write(fileContent);
        } catch (IOException e) {
            e.printStackTrace();
        }finally{
            //close resources
            try {
                fr.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    
    public static boolean removeFromLocale(String fileName) {
        File file = new File(fileName);
        return file.delete();
    }
}
