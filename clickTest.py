import click 

# THIS IS A TEST SCRIPT TO TEST OUT CLICK

print("Greetings sire. You are at the command center of the King Taipan botnet.")

@click.command()
@click.option('--host', prompt="Please enter host: ", help="Host on which king taipan will run")
@click.option("--port", prompt="Please enter port: ", help="Port at which king taipan's services will be exposed at")


def clickTest(host, port):
    
    
    print("Host is %s" % host)
    print("Port is %s" % port)




if __name__ == "__main__":
    clickTest()