## 20.09.2021
* Throughput should not be simplely proportional to RSRP and SNR, it should be influenced by dynamic number of connected UEs.
* consider inserting step function in throughput model to simulate switch to high code modulation.   
## 10.09.2021
* need a more sophisticated simulator so the RL algorithm can learn a more intersting policy than simply switching to the BS with the maximal RSRP. 
* work on a simple model for the throughput of the system.  
Things to consider could be:
* A simple mobility model of mobile devices. Here you can for example say that some vehicles are driving along a road with a fixed velocity so that the distance to a particular BS first gets smaller linearly, then has a minimum and then linearly increases again.
* Then we can compute the SNR as a function of the distance.
* This can also be influenced by changing noise levels that might also be different on different parts of the road.
* The throughput can then be a step function of the SNR because at predefined levels of SNR we can switch to a higher or lower coding scheme.
* You can also consider multiple vehicles and have the number of connected devices of a BS influence the throughput.
## 06.09.2021 
* Try to make the simple model more complex
   * Add more Base Station
   * Add noise in the signal 
   * Related SNR with reward function
* Think about what the difference between our work with other papers
* Write Thesis as early as possible

## 30.08.2021
* Verify that your `ns3-mock` example works properly (does the agent learn a policy that makes sense?)
* Christian will provide a `RlHandoverAlgorithm` minimum example for `ns3`; use example scripts of `ns3` and let them use `RlHandoverAlgorithm`

## 16.08.2021
* Do not use your own implementations for QLearning etc.; use libraries like stable-baselines instead.
* Have a look at [the CartPole Environment example from stable baselines](https://stable-baselines.readthedocs.io/en/master/guide/examples.html). We want to use our `ProtoHostEnv` together with `ns3-mock.py` as the `env` for RL libraries. Please create a proof of concept.

## 02.08.2021
* Christian provided code with interface between `ns3` and Python based on inter-process communication with TCP/IP and protocol buffers (protobuf)
* Write a `ns3-mock.py` file to test the interface (based on `host.py`)
  * Scenario with two cells and one UE
  * Environment
      * Keep track of the UE's current serving cell over time
      * Let RSRP values vary over time (sin waves with phase shift)
      * State: RSRP values of both cells (serving and neighbor)
      * Reward: Proportional to serving cell RSRP
  * Action: Either stay in currrent cell or change to neighbor
* Train an agent in the `ns3-mock` environment (create new file that uses `ProtoHostEnv` as the `env` for the agent)
  * Expected behaviour: Agent wants to stay connected to cell with the highest `RSRP`

## 26.07.2021
* Interface between `ns3` and Python will be ready soon (Christian)
* Write `RLHandoverAlgorithm` in `ns3` (Christian)

## 19.07.2021
* Check list online (Google docs)
  * Fill in your matr. number
  * Add signature as an image
  * Check the information of the check list for errors (e.g., check all dates)
* ns3 handover interface specifications ((cpp file)[https://www.nsnam.org/doxygen/a2-a4-rsrq-handover-algorithm_8cc_source.html]:
  * `void DoReportUeMeas (uint16_t rnti, LteRrcSap::MeasResults measResults)` is called whenever a handover event (A1-A4) happens
    * `rnti` identifies UEs uniquely
    * `MeasResults` contains `RSRP`, `RSRQ` values for the serving cell and neighbors
  * `void TriggerHandover (uint16_t rnti, uint16_t targetCellId)`
    * Triggers handover of UE identified by `rnti` to cell with `targetCellId`
  * Rethink state space, action space and rewards based on that interface
* Build `ns3` and run examples from the `LTE` module 
   * `lena-x2-handover.cc`
   * `lena-x2-handover-measures.cc`
* Christian writes first `ns3` handover algorithm and interface to Python
   * Use that with examples once done

## 05.07.2021
* Possible scenarios:
  * A9 scenario; compare implemented `ns3` algorithms (like A2A4) with your `RL` algorithm
  * Small cell scenario (like in 5G) with user mobility (ultra-dense networks); problem is `ns3` does not have 5G Radio (NewRadio); could be an extension
* Check available data from measurement reports in `ns3`; read and understand the `A2A4` algorithm
* Johnny and Christian write a draft of task description until next meeting; we can discuss it then
* Christian continues implementing the A9 scenario, so we can use it for this thesis

## 28.06.2021
* One more week to clarify the exact task (all of us work on that)
  * How is our topic different to other state of the art literature?

## 21.06.2021
* State of the art overview is done; next step is to figure out what **we** want to do in your work
* Long list of features (state space variables) could be helpful
* Johnny and Christian will clarify simulation details and think about the scope of the work

## 07.06.2021
* Started literature review (needs to be more precise, maybe use a table?).
* Goal is to get an overview of the problem domain (handovers) first, then we formulate a precise task description.
* List handover terms / variables (e.g., A1-A4 events, handover rate, etc.) and explain them shortly. How are they used by handover algorithms?
* How can the performance of handover algorithms be measured (e.g., see [1])? Create a list of metrics.

## 14.06.2021
* Add new columns to RL table (state, action, reward)
* Clarify time-to-trigger (TTT)
* `ns3` only uses triggered measurement reports (no periodic reports)
