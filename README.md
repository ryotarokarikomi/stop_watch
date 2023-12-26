# robosys2023_ros2
***ロボットシステム学(課題2)***  
ROS 2のサンプルコードです。  
`birthday/mypkg/talker.py`に記述されている誕生時刻から、現在の誕生時刻を求めます。

## 使用方法
### インストール
```
$ mkdir -p ~/ros2_ws/src
$ cd ~/ros2_ws/src
$ git clone https://github.com/ryotarokarikomi/robosys2023_ros2.git
```

### ビルド
```
$ cd ~/ros2_ws
$ colcon build
$ source ~/ros2_ws/install/setup.bash
```

### 実行
```
$ ros2 launch mypkg talk_listen.launch.py
```

## ビルドテスト [![build-test](https://github.com/ryotarokarikomi/robosys2023_ros2/actions/workflows/test.yaml/badge.svg)](https://github.com/ryotarokarikomi/robosys2023_ros2/actions/workflows/test.yaml)
### テスト環境
* Ubuntu(22.04.3 LTS)

### 著作権
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* このパッケージのplusコマンドの一部のコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
 * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022) 
* © 2023 Ryotaro Karikomi
