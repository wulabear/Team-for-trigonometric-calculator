2024软件工程题目说明
一.任务：
  1.建立小组git代码库
  2.每个成员分配单独账号，指派某成员账号对trunk开发线负责
  3.生成三角函数计算器（sin，cos，arcsin，arctan）
  4.代码架构应考虑方便显示，测试和移植
二.代码功能
  代码功能是实现对四个三角函数sin，cos，arcsin，arctan的计算，使用时会让用户输入要使用的函数类型，接着再输入输入数据，之后会输出结果
三.三角函数模块计算
  本工程一共有三个输入数据以及一个输出数据
    in_type：输入函数类型；
    in_data：用户输入函数所需的输入数据；
    in_terms：用户输入函数泰勒展开阶数；
    result：输出数据；
    根据用户输入的in_type函数类型判断用户所要使用的函数类型，再计算出相应的函数结果并输出。
  三角函数
    正弦函数：taylor_sin(in_data, in_terms);
    余弦函数：taylor_cos(in_data, in_terms);
    反正弦函数：taylor_asin(in_data, in_terms);
    反正切函数：taylor_atan(in_data, in_terms);
