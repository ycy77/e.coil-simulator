---
entity_id: "reaction.ecocyc.RXN-11860"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:tRNA (cytidine34/5-carboxymethylaminomethyluridine34-2'-O)-methyltransferase"
source_database: "EcoCyc"
source_id: "RXN-11860"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "tRNA (cytidine<sup>34</sup>/5-carboxymethylaminomethyluridine<sup>34</sup>-2'-<i>O</i>)-methyltransferase"
  - "methyltransferase yibK"
  - "YibK (gene name)"
---

# S-adenosyl-L-methionine:tRNA (cytidine34/5-carboxymethylaminomethyluridine34-2'-O)-methyltransferase

`reaction.ecocyc.RXN-11860`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11860`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + Cytidine-34-tRNAs -> 2-O-Methylcytidine-34-tRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Cytidine-34-tRNAs -> 2-O-Methylcytidine-34-tRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA (cytidine/uridine-2'-O)-ribose methyltransferase (complex.ecocyc.CPLX0-7421). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a cytidine34 in tRNA (molecule.ecocyc.Cytidine-34-tRNAs). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 2'-O-methylcytidine34 in tRNA (molecule.ecocyc.2-O-Methylcytidine-34-tRNAs).

## Annotation

S-ADENOSYLMETHIONINE + Cytidine-34-tRNAs -> 2-O-Methylcytidine-34-tRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7421|complex.ecocyc.CPLX0-7421]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-O-Methylcytidine-34-tRNAs|molecule.ecocyc.2-O-Methylcytidine-34-tRNAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Cytidine-34-tRNAs|molecule.ecocyc.Cytidine-34-tRNAs]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11860`

## Notes

S-ADENOSYLMETHIONINE + Cytidine-34-tRNAs -> 2-O-Methylcytidine-34-tRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
