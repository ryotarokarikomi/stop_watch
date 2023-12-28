# mypkg

## talker.py
* ```
  from birthday_msgs.msg import Birthday
  ```  
  * メッセージは[birthday_msgs](https://github.com/ryotarokarikomi/birthday_msgs.git)より`Birthday`型として使用
<br><br>
* ```
  pub = node.create_publisher(Birthday, "birthday", 10)
  ```  
  * メッセージの型を`Birthday`、トピックを`birthday`としてパブリッシャを定義
<br><br>
* ```
  class birth:
    year = 2000
    month = 9
    day = 13
    hour = 0
    minute = 0
    second = 0
  ```
  * `birth`クラスに求めたい人の生年月日とその日の時刻を記述
<br><br>
* `cb`関数にて`birth`クラスから経過時間を求める
<br><br>
* ```
  node.create_timer(1, cb)
  ```  
  * 1秒ごとに`cb`関数を呼び出し、経過時間を送信
<br><br>
### 実行
* 以下のコマンドで実行
  ```
  $ ros2 run mypkg talker
  ```
* 結果
  ```
  (何も表示されない)
  ```
  何も表示されていませんが、メッセージを送信しています。

## listener.py
* ```
  from birthday_msgs.msg import Birthday
  ```  
  * `talker.py`と同様にメッセージは[birthday_msgs](https://github.com/ryotarokarikomi/birthday_msgs.git)より`Birthday`型として使用
<br><br>
* `cb`関数にてメッセージのログを表示
<br><br>
* `sub = node.create_subscription(Birthday, "birthday", cb, 10)`  
  * メッセージの型を`Birthday`、トピックを`birthday`としてサブスクライバを定義し、受け取った`Birthday`型のメッセージをcb関数に渡す
<br><br>
### 実行
* 以下のコマンドで実行
  ```
  $ ros2 run mypkg listener
  ```
* 結果
  ```
  (何も表示されない)
  ```
  こちらも何も表示されていませんが、メッセージ受信の待機状態になっています。