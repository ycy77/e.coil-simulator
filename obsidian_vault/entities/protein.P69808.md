---
entity_id: "protein.P69808"
entity_type: "protein"
name: "fryB"
source_database: "UniProt"
source_id: "P69808"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fryB ypdH b2387 JW5389"
---

# fryB

`protein.P69808`

## Static

- Type: `protein`
- Source: `UniProt:P69808`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FryABC PTS system is involved in fructose transport. {ECO:0000250|UniProtKB:P20966}. fryB encodes a predicted Enzyme IIB component of a PTS permease of unknown specificity. FryB shows similarity to the IIB domain of the PTS Enzyme II specific for fructose

## Biological Role

Component of putative PTS enzyme II FryBCA (complex.ecocyc.CPLX0-8119).

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FryABC PTS system is involved in fructose transport. {ECO:0000250|UniProtKB:P20966}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8119|complex.ecocyc.CPLX0-8119]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2387|gene.b2387]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69808`
- `KEGG:ecj:JW5389;eco:b2387;ecoc:C3026_13270;`
- `GeneID:93774741;949087;`
- `GO:GO:0005737; GO:0009401; GO:0016301; GO:0022877; GO:0090582`
- `EC:2.7.1.202`

## Notes

PTS system fructose-like EIIB component 1 (EC 2.7.1.202) (Fructose-like phosphotransferase enzyme IIB component 1)
