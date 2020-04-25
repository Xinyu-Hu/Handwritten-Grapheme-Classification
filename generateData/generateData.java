import java.awt.AlphaComposite;
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.Transparency;
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;

import javax.imageio.ImageIO;


public class generateData {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String csvFile = "./src/testbangla.csv";
        String line = "";
        String cvsSplitBy = ",";
        int imgindex = 1;
        int imgsize = (int) (Math.random()*(224-180)+180); 
        Font font = null;
        
     
        // load bangla font
        try {
            font=Font.createFont( Font.TRUETYPE_FONT,
                new FileInputStream(new File("./src/kalpurush.ttf")) );
//            font=new Font("Arial Unicode MS", Font.PLAIN,30);
        } catch(Exception e) {
            System.out.println(e);
        }
        font=font.deriveFont(Font.PLAIN, 30);
        
        
        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            while ((line = br.readLine()) != null&&imgindex<=10) {
                // use comma as separator
                String[] map = line.split(cvsSplitBy);
//                if (map[0].indexOf('ং')!=0&&map[0].indexOf('্')!=2){
                if(true){
                    BufferedImage bufferedImage = new BufferedImage(imgsize, imgsize, BufferedImage.TYPE_INT_RGB); // Constructs a BufferedImage of one of the predefined image types.
                    Graphics2D g2d = bufferedImage.createGraphics();// Create a graphics which can be used to draw into the buffered image
                    g2d.setFont(font);
                    g2d.setColor(Color.white);// fill all the image with white
                    g2d.fillRect(0, 0, imgsize, imgsize);
                    g2d.setColor(Color.black);// create a string with black
                    g2d.drawString(map[0], (imgsize-10*map[0].length())/2, imgsize/2-10);
                    g2d.dispose();
                    File file = new File("./traceImg/"+imgindex+".png");
                    ImageIO.write(bufferedImage, "png", file);
                    System.out.println("[grapheme= " + map[0] +
                    		", index of ্: "+ map[0].indexOf('্') + //good feat. !=2
                    		", index of ং: "+map[0].indexOf('ং')+ //good feat. !=0
                    		", index of া: "+map[0].indexOf('া')+ //useless feat.
                    		", length: "+map[0].length()+ "]");
                    imgindex++;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        
	}

}
