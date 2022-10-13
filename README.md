# PASS
#####  Pass data through webhook
  
  Currently only support for discord webhooks
  
  
  Install
      
      python3 -m venv env
      source env/bin/activate
      pip install -r requirements.txt

  Run
    
      1.  cat <data-file> | python3 pass.py --pipe --id <id-from-config>
      2.  python3 pass.py -data <data-file> --id <id-from-config>

 #### Config Discord Template
 
  id - used for distinguishing between channels , can give any id but it must be unique

  app_name - discord

  channel_name - channel name given in the discord

  webhookurl - webhook url for communicating to the channel 
 
      [
        {
          "id": "",
          "app_name": "discord",
          "channel_name": "",
          "webhookurl": ""
        }
      ]
  For multiple channel use this format in config file 
       
       [
          {
          "id": "",
          "app_name": "discord",
          "channel_name": "",
          "webhookurl": ""
         },
         {
          "id": "",
          "app_name": "discord",
          "channel_name": "",
          "webhookurl": ""
         }
      ]
