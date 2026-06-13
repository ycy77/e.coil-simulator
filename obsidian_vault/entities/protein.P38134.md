---
entity_id: "protein.P38134"
entity_type: "protein"
name: "etk"
source_database: "UniProt"
source_id: "P38134"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein. Note=When the protein is overexpressed."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "etk yccC b0981 JW0964"
---

# etk

`protein.P38134`

## Static

- Type: `protein`
- Source: `UniProt:P38134`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein. Note=When the protein is overexpressed.

## Enriched Summary

Tyrosine-protein kinase etk (EC 2.7.10.-) Etk is a protein tyrosine kinase of the inner membrane that autophosphorylates and can be dephosphorylated by Etp . In contrast to the related kinase, G7105-MONOMER Wzc, Etk has minimal effect on biosynthesis of colanic acid . Etk, but not Wzc, plays a role in resistance to polymyxin B . Etk phosphorylates the heat shock sigma factor σ32 in vitro . A crystal structure of the C-terminal kinase domain has been solved at 2.5 Å resolution. Etk shows structural similarity to the ATPase MinD . Etk has two predicted transmembrane domains. The C terminus is located in the cytoplasm . The operon encoding YmcD, YmcC, YmcB, YmcA, YccZ, Etp, and Etk was characterized in the enteropathogenic E. coli strain O127:H6. There, all seven gene products are required for the production of the G4C capsule polysaccharide . That operon may not be expressed in E. coli K-12, because the promoter region that was mapped in E. coli O127:H6 is inactivated in E. coli K-12 by the insertion of an IS1 element 15 bp upstream of the YmcD translation start site . Reviews:

## Biological Role

Catalyzes RXN-24992 (reaction.ecocyc.RXN-24992).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

Tyrosine-protein kinase etk (EC 2.7.10.-)

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-24992|reaction.ecocyc.RXN-24992]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0981|gene.b0981]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P38134`
- `KEGG:ecj:JW0964;eco:b0981;ecoc:C3026_05985;`
- `GeneID:93776431;947409;`
- `GO:GO:0004713; GO:0005524; GO:0005886; GO:0016020; GO:0042802`
- `EC:2.7.10.-`

## Notes

Tyrosine-protein kinase etk (EC 2.7.10.-)
