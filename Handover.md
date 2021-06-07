## Classic Handover
The classic Handover process is based on the transfer of message between UE, eNBs and MME. The whole Process is divided into 3 parts:
* Handover preparetion  
  Data flows between UE and serving eNB (measurement control and report)
* Handover execution  
  Handover Request to target eNB, Request Ack to serving eNB, Handover Command to UE,     Synchronisation and Handover Confirm to target eNB 
* Handover completion  
  Path Switch Request to MME, Request Ack to target eNB, Resource in serving eNB release  
  |Events|description|formula|  
  |----|----|-----|  
  |A1|Serving becomes better than threshold|RSRQ(s)>threshold1|  
  |A2|Serving becomes worse than threshold|RSRQ(s)<threshold2|  
  |A3|Neighbour becomes offset better than serving|RSRQ(t)-RSRQ(S)>offset|  
  |A4|Neighbour becomes better than threshold|RSRQ(t)>threshold3|  
