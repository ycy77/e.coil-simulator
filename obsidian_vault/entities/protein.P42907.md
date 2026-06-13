---
entity_id: "protein.P42907"
entity_type: "protein"
name: "agaS"
source_database: "UniProt"
source_id: "P42907"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "agaS yraB b3136 JW3105"
---

# agaS

`protein.P42907`

## Static

- Type: `protein`
- Source: `UniProt:P42907`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the isomerization-deamination of galactosamine 6-phosphate to form tagatofuranose 6-phosphate and ammonium ion. {ECO:0000250|UniProtKB:Q9KIP9}. AgaS has been predicted to be an isomerase involved in N-acetylgalactosamine (GalNAc) utilization in some strains of E. coli . Because E. coli K-12 contains a partial deletion of the aga gene cluster and does not utilize GalNAc, functional studies have been carried out in E. coli C. There, a ΔagaS mutant becomes unable to utilize GalNAc . Expression of the agaS operon is induced by galactosamine and N--acetylgalactosamine and repressed by AgaR .

## Biological Role

Catalyzes RXN-13548 (reaction.ecocyc.RXN-13548).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the isomerization-deamination of galactosamine 6-phosphate to form tagatofuranose 6-phosphate and ammonium ion. {ECO:0000250|UniProtKB:Q9KIP9}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-13548|reaction.ecocyc.RXN-13548]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3136|gene.b3136]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42907`
- `KEGG:ecj:JW3105;eco:b3136;ecoc:C3026_17090;`
- `GeneID:947645;`
- `GO:GO:0005886; GO:0009401; GO:0016787; GO:0016853; GO:0097367; GO:1901135`
- `EC:3.5.99.-`

## Notes

Putative D-galactosamine-6-phosphate deaminase AgaS (EC 3.5.99.-) (Gam-6-P deaminase/isomerase)
