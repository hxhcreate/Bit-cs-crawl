# Bit-cs-crawl
crawl all the teachers' info at the CS school of BIT

`teacher_info.json` updated in 2023 Spring
json template structure as follows
```json
{
"<层次>":[
       {
        "姓名": "",
        "所在学科": "",
        "职称": " ",
        "联系电话": "",
        "E-mail": "",
        "通信地址": "",
        "detail_info": {
                "个人信息": "",
                "科研方向": "",
                "代表性学术成果": "",
                "承担科研情况": "",
                "所获奖励": "",
                "社会兼职": "",
                "备注": ""
        },
       ]
}

```

```bash
python bit_cs_tearch_crawl.py
```
