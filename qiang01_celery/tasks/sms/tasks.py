from celery import Celery


# 创建celry对象
app = Celery('qiang01_celery', broker='redis://127.0.0.1:6379/5')


# 定义任务
@app.task
def send_template_sms():
    ccp = CCP()
    ret = ccp.sendTemplateSMS(to, datas, temp_id)
    return ret

# 在我们后端程序中，在需要发送短信的地方使用以下语句：
# tasks.send_template_sms.delay(mobile,[sms_code, str(constants.SMS_CODE_REDIS_EXPIRES / 60)],1)
