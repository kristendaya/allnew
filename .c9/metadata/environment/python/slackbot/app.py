{"filter":false,"title":"app.py","tooltip":"/python/slackbot/app.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":49,"column":0},"end":{"row":57,"column":15},"action":"remove","lines":["@app.post(path='/sendhook')","async def sendHook(text:str):","    webhookToken = get_secret(\"slack_WebHookToken\")","    cmd =  \"curl -X POST -H\"","    cmd += \"'Content-type : application/json' --data \"","    cmd += \"'{\"+ '\"text\"'+ \":\" + '\"' + text + '\"' +\"}'\"","    cmd += webhookToken","    os.system(cmd)","    return cmd "],"id":1093},{"start":{"row":49,"column":0},"end":{"row":58,"column":0},"action":"insert","lines":["@app.post(path='/sendhook')","async def sendHook(text:str):","    webhookToken = get_secret(\"slack_WebHookToken\")","    cmd = \"curl -X POST -H \" ","    cmd += \"'Content-type: application/json' --data \"","    cmd += \"'{\" + '\"text\"' + \":\" + '\"' + text + '\"' + \"}' \"","    cmd += webhookToken    ","    os.system(cmd)","    return cmd ",""]}],[{"start":{"row":35,"column":45},"end":{"row":35,"column":46},"action":"insert","lines":[" "],"id":1094,"ignore":true},{"start":{"row":35,"column":47},"end":{"row":35,"column":48},"action":"insert","lines":[" "]}],[{"start":{"row":35,"column":44},"end":{"row":35,"column":45},"action":"insert","lines":[" "],"id":1095,"ignore":true}],[{"start":{"row":44,"column":29},"end":{"row":44,"column":30},"action":"remove","lines":[")"],"id":1096,"ignore":true}],[{"start":{"row":44,"column":29},"end":{"row":44,"column":30},"action":"insert","lines":[")"],"id":1097,"ignore":true}],[{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"remove","lines":["    "],"id":1098}],[{"start":{"row":23,"column":23},"end":{"row":23,"column":42},"action":"remove","lines":["slack_BotOAuthToken"],"id":1099},{"start":{"row":23,"column":23},"end":{"row":23,"column":42},"action":"insert","lines":["slack_BotOAuthToken"]}],[{"start":{"row":23,"column":23},"end":{"row":23,"column":42},"action":"remove","lines":["slack_BotOAuthToken"],"id":1100},{"start":{"row":23,"column":23},"end":{"row":23,"column":42},"action":"insert","lines":["slack_BotOAuthToken"]}],[{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":["x"],"id":1101}]]},"ace":{"folds":[],"scrolltop":180,"scrollleft":0,"selection":{"start":{"row":17,"column":31},"end":{"row":17,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"timestamp":1686641733126,"hash":"f73c0f05f272fae3caf0ea8cf4bbbda41a548fef"}