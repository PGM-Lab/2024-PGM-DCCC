import os

import pandas as pd
from bcause.models.cmodel import StructuralCausalModel
from bcause.util.equtils import seq_to_pandas

from ctfzeros.model_utils import get_state_mapping


def load_and_preprocess(modelfile, datapath=None):
    model = StructuralCausalModel.read(modelfile)
    datapath = datapath or modelfile.replace(".uai",".csv")
    data = pd.read_csv(datapath, index_col=0)


    non_root = [v for v in model.endogenous if len(model.get_edogenous_parents(v))>0]
    root = sorted([v for v in model.endogenous if len(model.get_edogenous_parents(v))==0])

    if len(non_root)>1: raise ValueError("Wrong topology")
    if not root == [f"V{i}" for i in range(1,len(root)+1)]: raise ValueError("Error with root variables names")
    if non_root[0] != "V0": raise ValueError("Error with non root variables names")

    # Rename variables
    model_endo_names = {v:v.replace("V", "X") for v in root}
    model_endo_names["V0"] = "Y"
    data_names = {k.replace("V",""):v for k,v in model_endo_names.items()}
    model_exo_names = {u:"U" + model_endo_names[model.get_children(u)[0]].lower() for u in model.exogenous}

    # get queries
    qpath = modelfile.replace(".uai", "_query.csv")

    queries = None
    if os.path.exists(qpath):
        queries = pd.read_csv(qpath).replace(model_endo_names) if os.path.exists(qpath) else None



    model = model.rename_vars({**model_endo_names, **model_exo_names})
    data = data.rename(columns=data_names)

    f = model.factors["Y"]
    # Reorder the variables
    f = f.reorder(*(sorted(f.right_vars) + f.left_vars))
    model.set_factor("Y", f)

    # Get the missing states and correct names
    state_map = get_state_mapping(model.factors["Y"], "Uy")
    missing_states = [s for s,v in state_map.items() if v==None]
    non_missing_states = [s for s,v in state_map.items() if v != None]

    # sort states in Uy
    values = f.values_array()
    v_states = [v for v in state_map.values() if v != None]
    new_values = values[v_states]
    model.set_factor("Y", f.builder(domain=f.domain, values=new_values))

    # Rename U domain
    new_dom = dict(Uy = non_missing_states)
    model = model.update_domains(**new_dom)

    return model,data,queries,missing_states


if __name__=="__main__":
    model,data,queries,missing_states  = load_and_preprocess("./models/synthetic/simple_nparents2_nzr02_zdr05_2.uai")
    print(model,data,queries,missing_states)

    f = model.factors["Y"]
    df = seq_to_pandas(f, exovar="Uy")



    model.domains


