---
entity_id: "reaction.ecocyc.NICOTINATEPRIBOSYLTRANS-RXN"
entity_type: "reaction"
name: "NICOTINATEPRIBOSYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "NICOTINATEPRIBOSYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Niacin ribonucleotidase"
  - "Nicotinic acid mononucleotide pyrophosphorylase"
  - "Nicotinic acid mononucleotide glycohydrolase"
  - "Nicotinic acid phosphoribosyltransferase"
---

# NICOTINATEPRIBOSYLTRANS-RXN

`reaction.ecocyc.NICOTINATEPRIBOSYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NICOTINATEPRIBOSYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first step in the Preiss-Handler pathway leading to the synthesis of the pyrimidine ring of NAD starting with nicotinic acid. A salvage recycling reaction. EcoCyc reaction equation: NIACINE + PRPP + ATP + WATER -> NICOTINATE_NUCLEOTIDE + PPI + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first step in the Preiss-Handler pathway leading to the synthesis of the pyrimidine ring of NAD starting with nicotinic acid. A salvage recycling reaction.

## Biological Role

Catalyzed by pncB (protein.P18133). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119), Nicotinate (molecule.C00253). Products: ADP (molecule.C00008), Diphosphate (molecule.C00013), Nicotinate D-ribonucleotide (molecule.C01185), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)

## Annotation

This is the first step in the Preiss-Handler pathway leading to the synthesis of the pyrimidine ring of NAD starting with nicotinic acid. A salvage recycling reaction.

## Pathways

- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P18133|protein.P18133]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01185|molecule.C01185]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00253|molecule.C00253]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NICOTINATEPRIBOSYLTRANS-RXN`

## Notes

NIACINE + PRPP + ATP + WATER -> NICOTINATE_NUCLEOTIDE + PPI + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
