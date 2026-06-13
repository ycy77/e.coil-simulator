---
entity_id: "reaction.ecocyc.PYRIMSYN1-RXN"
entity_type: "reaction"
name: "PYRIMSYN1-RXN"
source_database: "EcoCyc"
source_id: "PYRIMSYN1-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYRIMSYN1-RXN

`reaction.ecocyc.PYRIMSYN1-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRIMSYN1-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first part of the multistep synthesis of the pyrimidine moiety of thiamine. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 5-PHOSPHORIBOSYL-5-AMINOIMIDAZOLE -> AMINO-HYDROXYMETHYL-METHYL-PYR-P + CH33ADO + MET + FORMATE + CARBON-MONOXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first part of the multistep synthesis of the pyrimidine moiety of thiamine.

## Biological Role

Catalyzed by thiC (protein.P30136). Substrates: S-Adenosyl-L-methionine (molecule.C00019), Aminoimidazole ribotide (molecule.C03373). Products: Formate (molecule.C00058), L-Methionine (molecule.C00073), H+ (molecule.C00080), CO (molecule.C00237), 4-Amino-2-methyl-5-(phosphooxymethyl)pyrimidine (molecule.C04556), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO).

## Enriched Pathways

- `ecocyc.PWY-6890` 4-amino-2-methyl-5-diphosphomethylpyrimidine biosynthesis I (EcoCyc)

## Annotation

This is the first part of the multistep synthesis of the pyrimidine moiety of thiamine.

## Pathways

- `ecocyc.PWY-6890` 4-amino-2-methyl-5-diphosphomethylpyrimidine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P30136|protein.P30136]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00237|molecule.C00237]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04556|molecule.C04556]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03373|molecule.C03373]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PYRIMSYN1-RXN`

## Notes

S-ADENOSYLMETHIONINE + 5-PHOSPHORIBOSYL-5-AMINOIMIDAZOLE -> AMINO-HYDROXYMETHYL-METHYL-PYR-P + CH33ADO + MET + FORMATE + CARBON-MONOXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
