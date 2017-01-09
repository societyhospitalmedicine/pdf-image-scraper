/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.example.extractimagesfrompdfpages;

import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
// import net.java.dev.JaiImageIo;
import org.apache.pdfbox.cos.COSName;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.pdmodel.PDPageTree;
import org.apache.pdfbox.pdmodel.PDResources;
import org.apache.pdfbox.pdmodel.graphics.PDXObject;

/**
 *
 * @author fedevela
 */
public class ExtractImagesFromPDFPagesMain {

    public static void main(String[] args) {
        try {
            File thePDFFile = new File(args[0]);
            PDDocument document = PDDocument.load(thePDFFile);
            PDPageTree list = document.getPages();
            int i = 1;
            for (PDPage page : list) {
                Boolean alreadyCreatedFolderForThisPage = false;
                File thePDFFileDirectory = thePDFFile.getParentFile();
                File thePDFPageFolder = new File(thePDFFileDirectory.getAbsolutePath()+"/temp_images"+"/"+i);
                PDResources pdResources = page.getResources();
                int j = 1;
                for (COSName c : pdResources.getXObjectNames()) {
                    PDXObject o = pdResources.getXObject(c);
                    if (o instanceof org.apache.pdfbox.pdmodel.graphics.image.PDImageXObject) {
                        if (alreadyCreatedFolderForThisPage == false){
                            thePDFPageFolder.mkdirs();
                            alreadyCreatedFolderForThisPage = true;
                        }
                       
                        File file = new File(thePDFPageFolder.getAbsolutePath()+"/" + j + ".png");
                        ImageIO.write(((org.apache.pdfbox.pdmodel.graphics.image.PDImageXObject) o).getImage(), "png", file);
                        System.out.println(thePDFPageFolder.getAbsolutePath()+"/" + j + ".png");
                            
                        
                        j++;
                    }
                    
                }
                i++;
            }
        } catch (IOException ex) {
            Logger.getLogger(ExtractImagesFromPDFPagesMain.class.getName()).log(Level.SEVERE, null, ex);
            throw new RuntimeException(ex);
        }

    }
}