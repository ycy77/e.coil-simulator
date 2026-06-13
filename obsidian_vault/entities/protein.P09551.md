---
entity_id: "protein.P09551"
entity_type: "protein"
name: "argT"
source_database: "UniProt"
source_id: "P09551"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000250|UniProtKB:P02911}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argT b2310 JW2307"
---

# argT

`protein.P09551`

## Static

- Type: `protein`
- Source: `UniProt:P09551`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000250|UniProtKB:P02911}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Binds lysine, arginine and ornithine. Stimulates ATPase activity of HisP. {ECO:0000250|UniProtKB:P02911}. ArgT is the periplasmic binding protein of an ATP-dependent uptake system for the basic amino acids lysine, arginine and ornithine. E. coli argT is 89% similar to argT from Salmonella typhimurium which encodes a lysing/arginine/ornithine (LAO) periplasmic binding protein . argT is a member of the NtrC regulon; expression is increased in response to nitrogen starvation . argT expression increases during the early response to glucose limitation ). The level of ArgT is decreased after 4hrs exposure to zinc stress . ArgT is induced during stationary phase and further induced in late stationary phase; this induction is reduced in clpP, clpA and clpX protease mutants .

## Biological Role

Component of lysine / arginine / ornithine ABC transporter (complex.ecocyc.ABC-3-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Binds lysine, arginine and ornithine. Stimulates ATPase activity of HisP. {ECO:0000250|UniProtKB:P02911}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-3-CPLX|complex.ecocyc.ABC-3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2310|gene.b2310]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09551`
- `KEGG:ecj:JW2307;eco:b2310;ecoc:C3026_12880;`
- `GeneID:949030;`
- `GO:GO:0006995; GO:0009267; GO:0015822; GO:0016020; GO:0016597; GO:0030288; GO:0055052; GO:0071294; GO:0089718; GO:1902022`

## Notes

Lysine/arginine/ornithine-binding periplasmic protein (LAO-binding protein)
