---
entity_id: "reaction.ecocyc.RXN0-6366"
entity_type: "reaction"
name: "RXN0-6366"
source_database: "EcoCyc"
source_id: "RXN0-6366"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6366

`reaction.ecocyc.RXN0-6366`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6366`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + Ribosomal-protein-S12-Asp89 + 3FE-4S + Donor-H2 -> Ribosomal-protein-S12-3-methylthio-Asp89 + ADENOSYL-HOMO-CYS + CPD-23 + MET + CH33ADO + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Ribosomal-protein-S12-Asp89 + 3FE-4S + Donor-H2 -> Ribosomal-protein-S12-3-methylthio-Asp89 + ADENOSYL-HOMO-CYS + CPD-23 + MET + CH33ADO + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rimO (protein.P0AEI4). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a [3Fe-4S] iron-sulfur cluster (molecule.ecocyc.3FE-4S), a [ribosomal protein uS12] L-aspartate89 (molecule.ecocyc.Ribosomal-protein-S12-Asp89). Products: S-Adenosyl-L-homocysteine (molecule.C00021), L-Methionine (molecule.C00073), H+ (molecule.C00080), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO), a [3Fe-3S] iron-sulfur cluster (molecule.ecocyc.CPD-23), a [ribosomal protein uS12]-3-methylsulfanyl-L-aspartate89 (molecule.ecocyc.Ribosomal-protein-S12-3-methylthio-Asp89).

## Annotation

S-ADENOSYLMETHIONINE + Ribosomal-protein-S12-Asp89 + 3FE-4S + Donor-H2 -> Ribosomal-protein-S12-3-methylthio-Asp89 + ADENOSYL-HOMO-CYS + CPD-23 + MET + CH33ADO + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P0AEI4|protein.P0AEI4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-23|molecule.ecocyc.CPD-23]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ribosomal-protein-S12-3-methylthio-Asp89|molecule.ecocyc.Ribosomal-protein-S12-3-methylthio-Asp89]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.3FE-4S|molecule.ecocyc.3FE-4S]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ribosomal-protein-S12-Asp89|molecule.ecocyc.Ribosomal-protein-S12-Asp89]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6366`

## Notes

S-ADENOSYLMETHIONINE + Ribosomal-protein-S12-Asp89 + 3FE-4S + Donor-H2 -> Ribosomal-protein-S12-3-methylthio-Asp89 + ADENOSYL-HOMO-CYS + CPD-23 + MET + CH33ADO + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT
