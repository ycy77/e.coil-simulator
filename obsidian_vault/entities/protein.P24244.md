---
entity_id: "protein.P24244"
entity_type: "protein"
name: "appX"
source_database: "UniProt"
source_id: "P24244"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}. Note=In sucrose cushions fractionates with the outer membrane, in sarcosyl fractionation with the inner membrane. May have its C-terminus in the cytoplasm (PubMed:21778229). {ECO:0000269|PubMed:21778229}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "appX yccB b4592 JW0961.1 b0979.1"
---

# appX

`protein.P24244`

## Static

- Type: `protein`
- Source: `UniProt:P24244`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}. Note=In sucrose cushions fractionates with the outer membrane, in sarcosyl fractionation with the inner membrane. May have its C-terminus in the cytoplasm (PubMed:21778229). {ECO:0000269|PubMed:21778229}.

## Enriched Summary

FUNCTION: Might be part of cytochrome bd-II oxidase (appB and appC). Able to restore reductant resistance to a cydX deletion mutant upon overexpression. CydX and this protein may have some functional overlap. {ECO:0000269|PubMed:23749980}. AppX is a small, single transmembrane, accessory subunit of cytochrome bd-II. AppX and MONOMER0-2663 "CydX" are paralogs and may have overlapping functions in E. coli K-12 . Analysis of intact protein complexes released directly from native membranes indicates that AppX and CydX are able to interact simultaneously with CydAB to form a heterotetramer . In the cryo-EM structure of AppBCX reported by (a homodimer of two AppBCX heterotrimers with inhibitor bound) AppX interacts with AppC and forms the major contact between the two heterotrimers. AppX is expressed during stationary phase . Expression of AppX is higher in minimal glucose medium than in rich medium, increases upon extended heat shock, and is dramatically increased during oxygen-limited growth . AppX is predicted to contain a single transmembrane region; the majority of AppX partitions into the outer membrane fraction using a sucrose fractionation protocol . AppX is predicted to be a bitopic inner membrane protein .

## Biological Role

Component of cytochrome bd-II ubiquinol:oxygen oxidoreductase (complex.ecocyc.APP-UBIOX-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Might be part of cytochrome bd-II oxidase (appB and appC). Able to restore reductant resistance to a cydX deletion mutant upon overexpression. CydX and this protein may have some functional overlap. {ECO:0000269|PubMed:23749980}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.APP-UBIOX-CPLX|complex.ecocyc.APP-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4592|gene.b4592]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24244`
- `KEGG:eco:b4592;ecoc:C3026_05975;`
- `GeneID:93776433;948955;`
- `GO:GO:0005886; GO:0009279`

## Notes

Putative cytochrome bd-II ubiquinol oxidase subunit AppX
