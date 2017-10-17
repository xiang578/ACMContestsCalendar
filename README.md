# ACM Contests Calendar
- ACM 比赛日历订阅，让你不错过任何一场比赛


## 设计思路
1. `getjson`：获取比赛信息的 json 数据
2. `getics`：使用上一步得到的 json 数据构造符合 ics 要求的数据
3. `saveics`：保存上一步得到的数据到文件中
4. 在服务器上设置一个定时服务，每天更新ics文件
5. 使用 iCal、Google Calendar 等软件导入日历

## todo
* [ ] 部署到服务器，并提供订阅链接
* [ ] 编写获取比赛信息的脚本

## 参考资料
1. [比赛信息数据来源](http://acmicpc.info/archives/224)
2. [ACM近期比赛Google日历版](https://yangzhe1991.org/blog/2012/04/acm-contest-google-calendar/)
3. [cqut_student_schedule_py](https://github.com/acbetter/cqut_student_schedule_py)

