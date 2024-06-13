import requests  
import json  
import datetime
def record_log():  
    # 获取当前时间
    current_time = datetime.datetime.now()

    # 格式化时间为字符串，格式为：年-月-日 时:分:秒
    time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')

    # 要写入的日志内容
    log_message = f"{time_str} test start "

    # 打开文件并追加内容
    with open('/root/test_api.log', 'a') as file:
        file.write(log_message)

def get_scan_results(id):  
    url = f"http://anqing.natapp1.cc/api/v1/scans/{id}/results/preview"  
    headers = {'Accept': 'application/json'}  # 根据需要添加额外的HTTP头  
  
    try:  
        response = requests.get(url, headers=headers)  
        response.raise_for_status()  # 如果请求不是2xx，则抛出HTTPError异常  
        data = response.json()  # 将响应内容转换为JSON对象  
        # 假设返回的是一个JSON对象，并且你需要将它转换为JSON数组（如果它不是数组的话）  
        # 但通常，如果接口设计合理，返回的就应该是一个JSON数组或对象  
        # 如果data已经是一个列表（即JSON数组），则不需要进行任何转换  
        # 这里我们假设需要手动处理，例如提取某个字段作为数组  
        # data_as_array = data.get('some_key_that_holds_array', [])  # 替换为实际的键名  
        # 为了示例，我们假设data已经是JSON数组或我们不需要额外转换  
  
        # 返回数据（如果需要，可以进行进一步处理）  
        return data  
    except requests.exceptions.RequestException as e:  
        print(f"Error occurred: {e}")  
        return None  
def detail_result(data):

    results=[]

    for obj in data:
        metadata=obj['Metadata']
        for result in obj['Results']:
            for node in result['Nodes']:
                item={}
                item['path'] = node['fileName']
                item['column']= node['column']
                item['line'] = node['line']
                item['msg'] = ''
                item['rule'] = metadata['queryName']
                refs=[]
                ref={}
                ref['line']=item['line']
                ref['msg'] = ''
                ref['tag'] = ''
                ref['path']=item['path']
                refs.append(ref)
                item['refs']=refs
                results.append(item)
    results_info= json.dumps(results)
    # 指定要写入的文件名
    file_name = 'result.json'

    # 将JSON数据写入到文件中，使用with语句确保文件正确关闭
    with open(file_name, 'w', encoding='utf-8') as file:
        # json.dump将Python对象编码成JSON格式，并写入到文件中
        json.dump(results, file, ensure_ascii=False, indent=4)

record_log()
# 使用示例  
scan_id = 'b47b5b71-3e64-4f97-9455-ec9bb1f72839'  # 替换为你的scan_id  
results = get_scan_results(scan_id)  
if results is not None:  
    detail_result(results)
else:  
    print("Failed to get results.")
