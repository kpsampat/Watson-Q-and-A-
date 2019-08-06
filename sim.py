from ast import literal_eval
import paralleldots
import json
def main():
    with open('C:\\Users\\kishan.sampat\\Desktop\\user_input.txt', 'r') as file1:

        with open('C:\\Users\\kishan.sampat\\Desktop\\fact.txt', 'r') as file2:
            total_sim = []
            sim_val = []
            
            for target in file1:
                #print(target)
                pass
            
                for compare in file2:
                    #print(compare)
                  
                    final_data = similarity(target,compare)
                    new_final = final_data*100
                    sim_val.append(new_final)
                    #print(sim_val)
                    value = sum(sim_val)/len(sim_val)
                    total_sim = value
                    break
                
            return total_sim

def similarity(target,compare):
    api_key   = "djTeOg4gRQRnwl25dgswQoj1joPGmlila2puvacHu9w"
    paralleldots.set_api_key(api_key)
    sim = paralleldots.similarity(target, compare ) 
    json_sim = json.dumps(sim)
    #print(json_sim)
    d = literal_eval(json_sim)
    #print(d)
    data = d["actual_score"]
    #print(data)
    return data

main()