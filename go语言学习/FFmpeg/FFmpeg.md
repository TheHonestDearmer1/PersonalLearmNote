# ffmpeg

## 常用命令

### 01.下载，配置

用的系统是Ubuntu18.04,所以直接apt-get就可以了

```shell
sudo apt-get install ffmpeg
```

### 02.简介，上手(FFmpeg FFprobe FFplay)

(1)查看ffmpeg的帮助说明，提供的指令

```shell
ffmpeg -h
```

(2)播放媒体的指令

```shell
ffplay video.mp4
ffplay music.mp3
```

(3)常用快捷键

按键"Q"或"Esc"：退出媒体播放
键盘方向键：媒体播放的前进后退
点击鼠标右键：拖动到该播放位置
按键"F"：全屏
按键"P"或空格键：暂停
按键"W":切换显示模式

(4)查看媒体参数信息

```shell
ffprobe video.mp4
```

### 03.转换格式(文件格式,封装格式)

(1)文件名可以是中英文，但不能有空格。

(2)转换格式

```shell
ffmpeg -i video.mp4 video_avi.avi
```

### 04.改变编码 上(编码,音频转码)

(1)查看编解码器

```shell
ffmpeg -codecs
```

(2)网站常用编码

MP4封装：H264视频编码+ACC音频编码

```
ffmpeg -i inputFile -c:v libx264 -c:a aac outputFile
```

WebM封装：VP8视频编码+Vorbis音频编码
OGG封装：Theora视频编码+Vorbis音频编码

(3)无损编码格式.flac转换编码

```shell
ffmpeg -i music_flac.flac -acodec libmp3lame -ar 44100 -ab 320k -ac 2 music_flac_mp3.mp3
```

**说明：**

* acodec:audio Coder Decoder 音频编码解码器
* libmp3lame:mp3解码器
* ar:audio rate：音频采样率
* 44100:设置音频的采样率44100。若不输入，默认用原音频的采样率
* ab:audio bit rate 音频比特率
* 320k：设置音频的比特率。若不输入，默认128K
* ac: aduio channels 音频声道
* 2:声道数。若不输入，默认采用源音频的声道数

概括：设置格式的基本套路-先是指名属性，然后跟着新的属性值

(4)查看结果属性

```shell
ffprobe music_flac_mp3.mp3
```

### 05.改变编码 中(视频压制)

(1)视频转码

```shell
ffmpeg -i video.mp4 -s 1920x1080 -pix_fmt yuv420p -vcodec libx264 -preset medium -profile:v high -level:v 4.1 -crf 23 -acodec aac -ar 44100 -ac 2 -b:a 128k video_avi.avi
```

**说明:**

* -s 1920x1080：缩放视频新尺寸(size)
* -pix_fmt yuv420p：pixel format,用来设置视频颜色空间。参数查询：ffmpeg -pix_fmts
* -vcodec libx264：video Coder Decoder，视频编码解码器
* -preset medium: 编码器预设。参数：ultrafast,superfast,veryfast,faster,fast,medium,slow,slower,veryslow,placebo
* -profile:v high :编码器配置，与压缩比有关。实时通讯-baseline,流媒体-main,超清视频-high
* -level:v 4.1 ：对编码器设置的具体规范和限制，权衡压缩比和画质。
* -crf 23 ：设置码率控制模式。constant rate factor-恒定速率因子模式。范围0~51,默认23。数值越小，画质越高。一般在8~28做出选择。
* -r 30 :设置视频帧率
* -acodec aac :audio Coder Decoder-音频编码解码器
* -b:a 128k :音频比特率.大多数网站限制音频比特率128k,129k
  其他参考上一个教程

### 06.改变编码 下(码率控制模式)

ffmpeg支持的码率控制模式：-qp -crf -b

(1)  -qp :constant quantizer,恒定量化器模式 

无损压缩的例子（快速编码）

```shell
ffmpeg -i input -vcodec libx264 -preset ultrafast -qp 0 output.mkv
```

无损压缩的例子（高压缩比）

```shell
ffmpeg -i input -vcodec libx264 -preset veryslow -qp 0 output.mkv
```

(2) -crf :constant rate factor,恒定速率因子模式

(3) -b ：bitrate,固定目标码率模式。一般不建议使用

3种模式默认单遍编码

VBR(Variable Bit Rate/动态比特率) 例子

```shell
ffmpeg -i input -vcodec libx264 -preset veryslow output
```

ABR(Average Bit Rate/平均比特率) 例子

```shell
ffmpeg -i input -vcodec libx264 -preset veryslow -b:v 3000k output
```

CBR(Constant Bit Rate/恒定比特率) 例子

```shell
... -b:v 4000k -minrate 4000k -maxrate 4000k -bufsize 1835k ...
```



### 07.合并,提取音视频

(1)单独提取视频（不含音频流）

```shell
ffmpeg -i video.mp4 -vcodec copy -an video_silent.mp4
```

(2)单独提取音频（不含视频流）

```shell
ffmpeg -i video.mp4 -vn -acodec copy video_novideo.m4a
```

具备多个音频流的，如

Stream #0:2[0x81]:Audio:ac3,48000Hz,5.1,s16,384kb/s
Stream #0:3[0x82]:Audio:ac3,48000Hz,5.1,s16,384kb/s
Stream #0:4[0x80]:Audio:ac3,48000Hz,5.1,s16,448kb/s

针对性的单一的提取，例如提取第2条，用指令： -map 0:3

(3)合并音视频

```shell
ffmpeg -i video_novideo.m4a -i video_silent.mp4 -c copy video_merge.mp4
```

### 08.截取，连接音视频

(1)截取

```shell
ffmpeg -i music.mp3 -ss 00:00:30 -to 00:02:00 -acodec copy music_cutout.mp3
```

截取60秒

```shell
ffmpeg -i music.mp3 -ss 00:00:30 -t 60 -acodec copy music_cutout60s.mp3
```

-sseof : 从媒体末尾开始截取

```shell
ffmpeg -i in.mp4 -ss 00:01:00 -to 00:01:10 -c copy out.mp4
ffmpeg -ss 00:01:00 -i in.mp4 -to 00:01:10 -c copy out.mp4
ffmpeg -ss 00:01:00 -i in.mp4 -to 00:01:10 -c copy -copyts out.mp4
```

把-ss放到-i之前，启用了关键帧技术，加速操作。但截取的时间段不一定准确。可用最后一条指令，保留时间戳，保证时间准确。

(2)连接音视频

```shell
ffmpeg -i "concat:01.mp4|02.mp4|03.mp4" -c copy out.mp4
```

不同格式的音视频可以连接在一起，但不推荐不同格式连接在一起。
建议使用Avidemux软件连接

### 09.截图,水印,动图

(1)截图.

截取第7秒第1帧的画面

```shell
ffmpeg -i video.mp4 -ss 7 -vframes 1 video_image.jpg
```

(2)水印

```shell
ffmpeg -i video.mp4 -i qt.png -filter_complex "overlay=20:80" video_watermark.mp4
```

(3)截取动图

```shell
ffmpeg -i video.mp4 -ss 7.5 -to 8.5 -s 640x320 -r 15 video_gif.gif
```

10.录屏,直播

(1)录屏

windows: 

```shell
ffmpeg -f gdigrab -i desktop rec.mp4
```

ubuntu: 

```shell
sudo ffmpeg -f fbdev -framerate 10 -i /dev/fb0 rec.mp4
```

gdigrab ：ffmpeg中的一个组件。

只捕获视频.若要录屏，录音，获取摄像头，麦克风，换组件，用OBS Studio软件

(2)直播

```shell
ffmpeg -re i rec.mp4 按照网站要求编码 -f flv "你的rtmp地址/你的直播码"
```

在go中使用FFmpeg

```go
	// FFmpeg命令转换视频
	cmd := exec.Command("ffmpeg", "-i", "input.mp4", "-vcodec", "libx264", "-acodec", "aac", "-strict", "-2", "output.mp4")

	err = cmd.Run()
	if err != nil {
		fmt.Println(err)
	}
```

**相对目录以main.go文件所在的目录为准**

## 参考资料

笔记来源: https://www.bilibili.com/video/av40146374

官方教程: http://ffmpeg.org/ffmpeg-all.html