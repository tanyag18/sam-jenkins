import json
import calc

#console.log('Loading the calculator function');

def lambda_handler(event, context):
    # TODO implement
    
    a = event['a']
    b = event['b']
    o = event['o']
    
    if (o == "a") :
        c = calc.add(int(a),int(b))
    if (o == "s") :
        c = calc.sub(int(a),int(b))
    if (o == "m") :
        c = calc.mul(int(a),int(b))
    if (o == "d") :
        c = calc.div(int(a),int(b))
    
    d = str(c)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Answer = '+d)
    }
