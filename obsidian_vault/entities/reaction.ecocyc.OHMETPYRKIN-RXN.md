---
entity_id: "reaction.ecocyc.OHMETPYRKIN-RXN"
entity_type: "reaction"
name: "OHMETPYRKIN-RXN"
source_database: "EcoCyc"
source_id: "OHMETPYRKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# OHMETPYRKIN-RXN

`reaction.ecocyc.OHMETPYRKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:OHMETPYRKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in two biosynthetic pathways. It is one of the first steps in the biosynthesis of thiamine pyrophosphate and it is a reaction in the second part of the multistep synthesis of the pyrimidine moiety of thiamine. EcoCyc reaction equation: ATP + HMP -> PROTON + ADP + AMINO-HYDROXYMETHYL-METHYL-PYR-P; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is involved in two biosynthetic pathways. It is one of the first steps in the biosynthesis of thiamine pyrophosphate and it is a reaction in the second part of the multistep synthesis of the pyrimidine moiety of thiamine.

## Biological Role

Catalyzed by hydroxymethylpyrimidine kinase / phosphomethylpyrimidine kinase (complex.ecocyc.HMP-P-KIN-CPLX), pyridoxal kinase 1 / hydroxymethylpyrimidine kinase (complex.ecocyc.PDXK-CPLX). Substrates: ATP (molecule.C00002), 4-Amino-5-hydroxymethyl-2-methylpyrimidine (molecule.C01279). Products: ADP (molecule.C00008), H+ (molecule.C00080), 4-Amino-2-methyl-5-(phosphooxymethyl)pyrimidine (molecule.C04556).

## Enriched Pathways

- `ecocyc.PWY-6910` hydroxymethylpyrimidine salvage (EcoCyc)

## Annotation

This reaction is involved in two biosynthetic pathways. It is one of the first steps in the biosynthesis of thiamine pyrophosphate and it is a reaction in the second part of the multistep synthesis of the pyrimidine moiety of thiamine.

## Pathways

- `ecocyc.PWY-6910` hydroxymethylpyrimidine salvage (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.HMP-P-KIN-CPLX|complex.ecocyc.HMP-P-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.PDXK-CPLX|complex.ecocyc.PDXK-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04556|molecule.C04556]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01279|molecule.C01279]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00314|molecule.C00314]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:OHMETPYRKIN-RXN`

## Notes

ATP + HMP -> PROTON + ADP + AMINO-HYDROXYMETHYL-METHYL-PYR-P; direction=PHYSIOL-LEFT-TO-RIGHT
