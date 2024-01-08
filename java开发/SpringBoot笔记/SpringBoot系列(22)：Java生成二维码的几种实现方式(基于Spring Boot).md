 

原文链接：[http://www.fightjava.com/web/index/blog/article/82](http://www.fightjava.com/web/index/blog/article/82)

在一些企业级应用系统中，有时候需要为产品或者商品生成特定的专属二维码，以供一些硬件设备或者用户在手机端扫码查看；其中，该二维码主要承载了该产品的相关核心信息，比如名称、简介、价格、单位、型号以及使用说明等等，本文将基于Spring Boot介绍两种生成二维码的实现方式，一种是基于Google开发工具包，另一种是基于Hutool来实现；

 话不多说，咱们直接进入正题~~~

 说起这个二维码，想必诸位小伙伴都比较熟悉，它是信息的一种载体，也是信息的一种表示形式，可以很好的承载、保护想要重点维护的产品相关的核心信息；而在软件开发领域，这种形式愈加常见，因此，还是有必要撸一撸相应的代码的！

![](https://img-blog.csdnimg.cn/img_convert/4267bf28e6d755da47d34fe11f7b02b7.png)

 为了方便理解二维码的实际应用场景，debug给诸位举一些例子吧！

（1）进销存系统 想必大家都听说过，其系统中的商品二维码承载了许多重要、核心的关键信息，比如商品编码、商品名称、规格、型号、单位、作用/使用说明等信息；操作者可以借助硬件设备，如“扫码枪”，通过扫描该二维码后将该商品录入到商品库中；

（2）再比如溯源系统中的产品，用户可以通过微信等APP中的扫一扫，扫描贴在产品上的二维码，不出片刻即可得到该产品的相关信息，比如产品名称、生源地、简介、价格、生产环境、经手人等信息；

 下面我们将基于Spring Boot，并采用两种方式实现二维码的生成，对于每一种方式还提供两种类型的二维码返回形式，即：物理文件 和 图片响应流

![](https://img-blog.csdnimg.cn/img_convert/6319e9cc05c3c22ed63cd0c2da52ca67.png)

**一、基于Google开发工具包ZXing生成二维码**

（1）首先，需要在pom.xml依赖配置文件中加入该工具包的依赖Jar，如下所示：   

`   1.  <!-- zxing生成二维码 -->      2.  <dependency>      3.      <groupId>com.google.zxing</groupId>      4.      <artifactId>core</artifactId>      5.      <version>3.3.3</version>      6.  </dependency>       8.  <dependency>      9.      <groupId>com.google.zxing</groupId>      10.      <artifactId>javase</artifactId>      11.      <version>3.3.3</version>      12.  </dependency>        `

（2）然后，建立一二维码处理工具类QRCodeUtil，其核心代码如下所示：

`   1.  /**      2.   * 二维码工具      3.   * @Author:debug (SteadyJack)      4.   * @Link: weixin-> debug0868  qq-> 1948831260      5.   * @Date: 2020/11/16 22:38      6.   **/      7.  public class QRCodeUtil {      8.      private static final Logger log= LoggerFactory.getLogger(QRCodeUtil.class);       10.      //CODE_WIDTH：二维码宽度，单位像素      11.      private static final int CODE_WIDTH = 400;      12.      //CODE_HEIGHT：二维码高度，单位像素      13.      private static final int CODE_HEIGHT = 400;      14.      //FRONT_COLOR：二维码前景色，0x000000 表示黑色      15.      private static final int FRONT_COLOR = 0x000000;      16.      //BACKGROUND_COLOR：二维码背景色，0xFFFFFF 表示白色      17.      //演示用 16 进制表示，和前端页面 CSS 的取色是一样的，注意前后景颜色应该对比明显，如常见的黑白      18.      private static final int BACKGROUND_COLOR = 0xFFFFFF;       20.      public static void createCodeToFile(String content, File codeImgFileSaveDir, String fileName) {      21.          try {      22.              if (StringUtils.isBlank(content) || StringUtils.isBlank(fileName)) {      23.                  return;      24.              }      25.              content = content.trim();      26.              if (codeImgFileSaveDir==null || codeImgFileSaveDir.isFile()) {      27.                  //二维码图片存在目录为空，默认放在桌面...      28.                  codeImgFileSaveDir = FileSystemView.getFileSystemView().getHomeDirectory();      29.              }      30.              if (!codeImgFileSaveDir.exists()) {      31.                  //二维码图片存在目录不存在，开始创建...      32.                  codeImgFileSaveDir.mkdirs();      33.              }       35.              //核心代码-生成二维码      36.              BufferedImage bufferedImage = getBufferedImage(content);       38.              File codeImgFile = new File(codeImgFileSaveDir, fileName);      39.              ImageIO.write(bufferedImage, "png", codeImgFile);       41.              log.info("二维码图片生成成功：" + codeImgFile.getPath());      42.          } catch (Exception e) {      43.              e.printStackTrace();      44.          }      45.      }       47.      /**      48.       * 生成二维码并输出到输出流, 通常用于输出到网页上进行显示，输出到网页与输出到磁盘上的文件中，区别在于最后一句 ImageIO.write      49.       * write(RenderedImage im,String formatName,File output)：写到文件中      50.       * write(RenderedImage im,String formatName,OutputStream output)：输出到输出流中      51.       * @param content  ：二维码内容      52.       * @param outputStream ：输出流，比如 HttpServletResponse 的 getOutputStream      53.       */      54.      public static void createCodeToOutputStream(String content, OutputStream outputStream) {      55.          try {      56.              if (StringUtils.isBlank(content)) {      57.                  return;      58.              }      59.              content = content.trim();      60.              //核心代码-生成二维码      61.              BufferedImage bufferedImage = getBufferedImage(content);       63.              //区别就是这一句，输出到输出流中，如果第三个参数是 File，则输出到文件中      64.              ImageIO.write(bufferedImage, "png", outputStream);       66.              log.info("二维码图片生成到输出流成功...");      67.          } catch (Exception e) {      68.              e.printStackTrace();      69.          }      70.      }       72.      //核心代码-生成二维码      73.      private static BufferedImage getBufferedImage(String content) throws WriterException {       75.          //com.google.zxing.EncodeHintType：编码提示类型,枚举类型      76.          Map<EncodeHintType, Object> hints = new HashMap();       78.          //EncodeHintType.CHARACTER_SET：设置字符编码类型      79.          hints.put(EncodeHintType.CHARACTER_SET, "UTF-8");       81.          //EncodeHintType.ERROR_CORRECTION：设置误差校正      82.          //ErrorCorrectionLevel：误差校正等级，L = ~7% correction、M = ~15% correction、Q = ~25% correction、H = ~30% correction      83.          //不设置时，默认为 L 等级，等级不一样，生成的图案不同，但扫描的结果是一样的      84.          hints.put(EncodeHintType.ERROR_CORRECTION, ErrorCorrectionLevel.M);       86.          //EncodeHintType.MARGIN：设置二维码边距，单位像素，值越小，二维码距离四周越近      87.          hints.put(EncodeHintType.MARGIN, 1);       89.          MultiFormatWriter multiFormatWriter = new MultiFormatWriter();      90.          BitMatrix bitMatrix = multiFormatWriter.encode(content, BarcodeFormat.QR_CODE, CODE_WIDTH, CODE_HEIGHT, hints);      91.          BufferedImage bufferedImage = new BufferedImage(CODE_WIDTH, CODE_HEIGHT, BufferedImage.TYPE_INT_BGR);      92.          for (int x = 0; x < CODE_WIDTH; x++) {      93.              for (int y = 0; y < CODE_HEIGHT; y++) {      94.                  bufferedImage.setRGB(x, y, bitMatrix.get(x, y) ? FRONT_COLOR : BACKGROUND_COLOR);      95.              }      96.          }      97.          return bufferedImage;      98.      }      99.  }        `

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png)

 上述代码有点多，诸位可以在文末提供的下载地址将其下载下来，并用IDEA等开发工具将其打开，几乎每行代码debug都做了必要的注释，在这里就不赘述了！

 总的来说，上面代码主要包含了两个部分，一部分是将实现如何将信息塞入二维码并将其生成图片存储至物理文件目录下；另一部分是实现如何直接将信息塞入二维码并生成图片最终以图片流的形式将其返回给前端调用端；

（3）最后，我们需要新建一个QrCodeController控制器类，并在其中创建两个请求方法，用于测试Google ZXing工具包这种方式生成两种类型的二维码是否可行，其代码如下所示：

`   1.  @RequestMapping("qr/code")      2.  public class QrCodeController extends BaseController{       4.      private static final String RootPath="E:\\shFiles\\QRCode";      5.      private static final String FileFormat=".png";       7.      private static final ThreadLocal<SimpleDateFormat> LOCALDATEFORMAT=ThreadLocal.withInitial(() -> new SimpleDateFormat("yyyyMMddHHmmss"));       9.      //生成二维码并将其存放于本地目录      10.      @PostMapping("generate/v1")      11.      public BaseResponse generateV1(String content){      12.          BaseResponse response=new BaseResponse(StatusCode.Success);      13.          try {      14.              final String fileName=LOCALDATEFORMAT.get().format(new Date());      15.              QRCodeUtil.createCodeToFile(content,new File(RootPath),fileName+FileFormat);      16.          }catch (Exception e){      17.              response=new BaseResponse(StatusCode.Fail.getCode(),e.getMessage());      18.          }      19.          return response;      20.      }       22.      //生成二维码并将其返回给前端调用者      23.      @PostMapping("generate/v2")      24.      public BaseResponse generateV2(String content,HttpServletResponse servletResponse){      25.          BaseResponse response=new BaseResponse(StatusCode.Success);      26.          try {      27.              QRCodeUtil.createCodeToOutputStream(content,servletResponse.getOutputStream());       29.          }catch (Exception e){      30.              response=new BaseResponse(StatusCode.Fail.getCode(),e.getMessage());      31.          }      32.          return response;      33.  }      34.  }        `

 最后是将该项目运行起来并采用Postman对该接口进行测试，首先是控制器第一个方法接口的测试，其测试结果如下图所示（生成的二维码图片是存放在 E:\\\\shFiles\\\\QRCode 中的）：

![](https://img-blog.csdnimg.cn/img_convert/79064ca686b2c288fce8ac03a3871f2c.png)

 最后是控制器第二个方法接口的测试，其测试结果如下图所示：

![](https://img-blog.csdnimg.cn/img_convert/1152d1312f60fe39b3d11fa55e2b9e75.png)

**PS****：**如果不想存储二维码图片到实际的文件目录，则可以采用“图片流”的形式将其返回即可；反之，则可以将生成的二维码图片存储起来并返回该图片的访问链接给到前端（这个就稍微有点麻烦了，既要存储、又要赋予图片的访问域名和链接）；具体取舍可以根据实际业务情况来做抉择吧！

**二、基于开源的Hutool工具生成二维码**

 下面，debug换一种实现方式，采用目前比较知名、流行的开源工具Hutool加以实现，同样的道理需要在pom.xml中加入相应的Jar依赖，如下所示：   

`   1.  <!--开发工具集-->      2.  <dependency>      3.      <groupId>cn.hutool</groupId>      4.      <artifactId>hutool-all</artifactId>      5.      <version>4.6.10</version>      6.  </dependency>        `

 然后，需要自定义一Java Config配置文件，以Bean的形式显示配置并注入QrConfig，如下代码所示：

`   1.  @Configuration      2.  public class QRConfig {       4.      //采用JavaConfig的方式显示注入hutool中 生成二维码      5.      @Bean      6.      public QrConfig qrConfig(){      7.          //初始宽度和高度      8.          QrConfig qrConfig=new QrConfig(300,300);       10.          //设置边距，即二维码和边框的距离      11.          qrConfig.setMargin(2);      12.          //设置前景色      13.          qrConfig.setForeColor(Color.BLACK.getRGB());      14.          //设置背景色      15.          qrConfig.setBackColor(Color.WHITE.getRGB());       17.          return qrConfig;      18.      }      19.  }        `

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png)

 紧接着我们建立一QrCodeService，用于处理真正的生成二维码的业务逻辑，其核心代码如下所示：

`   1.  @Service      2.  @Slf4j      3.  public class QrCodeService {      4.      @Autowired      5.      private QrConfig config;       7.      //生成到文件      8.      public void createCodeToFile(String content, String filePath) {      9.          try {      10.              QrCodeUtil.generate(content,config,FileUtil.file(filePath));      11.          } catch (QrCodeException e) {      12.              e.printStackTrace();      13.          }      14.      }      15.      //生成到流      16.      public void createCodeToStream(String content, HttpServletResponse response) {      17.          try {      18.              QrCodeUtil.generate(content,config, "png", response.getOutputStream());      19.          } catch (QrCodeException | IOException e) {      20.              e.printStackTrace();      21.          }      22.      }      23.  }        `

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png)

 最终，是在QrCodeController控制器类中进行调用，如下代码所示：

`   1.  @Autowired      2.  private QrCodeService codeService;       4.  //生成二维码并将其返回给前端调用者_hutool      5.  @PostMapping("generate/v3")      6.  public BaseResponse generateV3(String content,HttpServletResponse servletResponse){      7.      BaseResponse response=new BaseResponse(StatusCode.Success);      8.      try {      9.          //将生成的二维码文件存放于文件目录中      10.          //final String fileName=LOCALDATEFORMAT.get().format(new Date());      11.          //codeService.createCodeToFile(content,RootPath+File.separator+fileName+".png");       13.          //将生成的二维码文件直接返回给前端响应流      14.          codeService.createCodeToStream(content,servletResponse);      15.      }catch (Exception e){      16.          response=new BaseResponse(StatusCode.Fail.getCode(),e.getMessage());      17.      }      18.      return response;      19.  }        `

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png)

 在上述该代码中，debug也测试了两种形式的二维码的生成，下面采用Postman测试“以图片流的形式返回二维码图片”的方法接口，其测试结果如下图所示：

![](https://img-blog.csdnimg.cn/img_convert/4c401cb6bcd7f38c72e072fb45d87d0f.png)

**总结：**

（1）代码下载：关注“程序员实战基地”微信公众号，回复“**二维码**”，即可获取代码下载链接

（2）至此，我们已经介绍完了两种“生成二维码”的实现方式的代码实战；相对而言，显然是第二种用起来比较舒服，即基于Hutool工具包的组件来生成二维码，可以说是既方便又快捷啦，当然啦，其底层仍然是基于Google ZXing工具实现的，即Hutool的工具包的部分组件其实是对第三方工具/组件的高度封装！不信的话，诸位小伙伴可以去撸一撸！

![](https://img-blog.csdnimg.cn/img_convert/bd5af5224f99304f45a329b9b25ab8bc.png)

我是debug，一个相信技术改变生活、技术成就梦想 的攻城狮；如果本文对你有帮助，请关注公众号，并动动手指收藏、点赞、以及转发哦！！！   

 关注一下Debug的技术微信公众号，最新的技术文章、课程以及技术专栏将会第一时间在公众号发布哦！

![](https://img-blog.csdnimg.cn/img_convert/c14125a31a360dd70c5ddc13264c757d.png)

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Java技能树](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)136489 人正在系统学习中

本文转自 <https://blog.csdn.net/u013871100/article/details/110287809>，如有侵权，请联系删除。