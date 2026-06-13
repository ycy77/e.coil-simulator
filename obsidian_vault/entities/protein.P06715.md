---
entity_id: "protein.P06715"
entity_type: "protein"
name: "gor"
source_database: "UniProt"
source_id: "P06715"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:6393625}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gor b3500 JW3467"
---

# gor

`protein.P06715`

## Static

- Type: `protein`
- Source: `UniProt:P06715`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:6393625}.

## Enriched Summary

FUNCTION: Catalyzes the reduction of glutathione disulfide (GSSG) to reduced glutathione (GSH). Constitutes the major mechanism to maintain a high GSH:GSSG ratio in the cytosol. {ECO:0000269|PubMed:6393625}.

## Biological Role

Catalyzes glutathione:NAD+ oxidoreductase (reaction.R00094), glutathione:NADP+ oxidoreductase (reaction.R00115). Component of glutathione reductase (complex.ecocyc.GLUTATHIONE-REDUCT-NADPH-CPLX).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of glutathione disulfide (GSSG) to reduced glutathione (GSH). Constitutes the major mechanism to maintain a high GSH:GSSG ratio in the cytosol. {ECO:0000269|PubMed:6393625}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00094|reaction.R00094]] `KEGG` `database` - via EC:1.8.1.7
- `catalyzes` --> [[reaction.R00115|reaction.R00115]] `KEGG` `database` - via EC:1.8.1.7
- `is_component_of` --> [[complex.ecocyc.GLUTATHIONE-REDUCT-NADPH-CPLX|complex.ecocyc.GLUTATHIONE-REDUCT-NADPH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3500|gene.b3500]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06715`
- `KEGG:ecj:JW3467;eco:b3500;`
- `GeneID:948014;`
- `GO:GO:0004362; GO:0005829; GO:0006749; GO:0016020; GO:0034599; GO:0045454; GO:0050660; GO:0050661; GO:0071949`
- `EC:1.8.1.7`

## Notes

Glutathione reductase (GR) (GRase) (EC 1.8.1.7)
