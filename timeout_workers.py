# Custom functions for the calculations with timeout
# We need this in a seprate .py as setting them in the notebook causes issues with multiprocessing on Windows
import pm4py

def _fitness_worker(result_queue, log, net, im, fm):
    try:
        fitness = pm4py.fitness_alignments(log, net, im, fm)
        result_queue.put(("ok", fitness))
    except Exception as e:
        result_queue.put(("error", str(e)))

def _precision_worker(result_queue, log, net, im, fm):
    try:
        precision = pm4py.precision_alignments(log, net, im, fm)
        result_queue.put(("ok", precision))
    except Exception as e:
        result_queue.put(("error", str(e)))

def _simplicity_worker(result_queue, net, im, fm, variant_name):
    try:
        val = pm4py.simplicity_petri_net(net, im, fm, variant=variant_name)
        result_queue.put(("ok", val))
    except Exception as e:
        result_queue.put(("error", str(e)))