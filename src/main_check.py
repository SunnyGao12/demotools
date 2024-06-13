import argparse  
import json  
  
def main(action):  
    if action == 'check':  
        result = {"usable": True}  # 注意Python中的True是大写的  
        with open('check_result.json', 'w') as f:  
            json.dump(result, f)  
        print("check_result.json has been updated.")  
    else:  
        print("Invalid action. Only 'check' is supported.")  
  
if __name__ == "__main__":  
    parser = argparse.ArgumentParser(description='Check usability and write to JSON.')  
    parser.add_argument('action', type=str, help='The action to perform (check).')  
    args = parser.parse_args()  
    main(args.action)