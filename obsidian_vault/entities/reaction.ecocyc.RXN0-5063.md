---
entity_id: "reaction.ecocyc.RXN0-5063"
entity_type: "reaction"
name: "RXN0-5063"
source_database: "EcoCyc"
source_id: "RXN0-5063"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5063

`reaction.ecocyc.RXN0-5063`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5063`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 6-Dimethylallyladenosine37-tRNAs + 3FE-4S + Donor-H2 -> CPD-11592 + ADENOSYL-HOMO-CYS + CPD-23 + CH33ADO + MET + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 6-Dimethylallyladenosine37-tRNAs + 3FE-4S + Donor-H2 -> CPD-11592 + ADENOSYL-HOMO-CYS + CPD-23 + CH33ADO + MET + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by miaB (protein.P0AEI1). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a [3Fe-4S] iron-sulfur cluster (molecule.ecocyc.3FE-4S), N6-(3-methylbut-2-en-1-yl)-adenine37 in tRNA (molecule.ecocyc.6-Dimethylallyladenosine37-tRNAs). Products: S-Adenosyl-L-homocysteine (molecule.C00021), L-Methionine (molecule.C00073), H+ (molecule.C00080), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO), 2-(methylsulfanyl)-N6-prenyladenosine37 in tRNA (molecule.ecocyc.CPD-11592), a [3Fe-3S] iron-sulfur cluster (molecule.ecocyc.CPD-23).

## Annotation

S-ADENOSYLMETHIONINE + 6-Dimethylallyladenosine37-tRNAs + 3FE-4S + Donor-H2 -> CPD-11592 + ADENOSYL-HOMO-CYS + CPD-23 + CH33ADO + MET + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P0AEI1|protein.P0AEI1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-11592|molecule.ecocyc.CPD-11592]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-23|molecule.ecocyc.CPD-23]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.3FE-4S|molecule.ecocyc.3FE-4S]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.6-Dimethylallyladenosine37-tRNAs|molecule.ecocyc.6-Dimethylallyladenosine37-tRNAs]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5063`

## Notes

S-ADENOSYLMETHIONINE + 6-Dimethylallyladenosine37-tRNAs + 3FE-4S + Donor-H2 -> CPD-11592 + ADENOSYL-HOMO-CYS + CPD-23 + CH33ADO + MET + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
