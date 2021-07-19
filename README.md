# Studienarbeit


## Meeting Minutes

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

## State of the Art

## Timeline

## References
[1] [LTE Handover Performance Evaluation Based on Power Budget Handover Algorithm](https://upcommons.upc.edu/bitstream/handle/2099.1/21093/LTE+Handover+Performance+Evaluation.pdf?sequence=4)
