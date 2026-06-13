---
entity_id: "protein.P52697"
entity_type: "protein"
name: "pgl"
source_database: "UniProt"
source_id: "P52697"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgl ybhE b0767 JW0750"
---

# pgl

`protein.P52697`

## Static

- Type: `protein`
- Source: `UniProt:P52697`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of 6-phosphogluconolactone to 6-phosphogluconate. {ECO:0000269|PubMed:15576773}. 6-phosphogluconolactonase is an enzyme of the oxidative pentose phosphate pathway. A pgl mutant strain grows only slightly slower than wild type on glucose as the sole source of carbon . Growth on glucose may be due to non-enzymatic hydrolysis of D-6-P-GLUCONO-DELTA-LACTONE or a bypass pathway that involves dephosphorylation and export of gluconolactone, hydrolysis to gluconate, followed by gluconate re-import and phosphorylation . When grown on maltose medium, strains lacking Pgl activity turn blue after iodine treatment . The phenotype of a pgl deletion strain can be complemented by expression of the pgl gene from Pseudomonas putida, although there is no detectable similarity between the two genes . A metabolic flux balance experiment revealed that the inefficient growth when pgl is deleted results solely from the extracellular bypass mechanism . Unlike some other enzymes that participate in the pentose phosphate pathway, Pgl is robust towards oxidative inactivation by peroxyl radicals...

## Biological Role

Catalyzes 6PGLUCONOLACT-RXN (reaction.ecocyc.6PGLUCONOLACT-RXN).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of 6-phosphogluconolactone to 6-phosphogluconate. {ECO:0000269|PubMed:15576773}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.6PGLUCONOLACT-RXN|reaction.ecocyc.6PGLUCONOLACT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0767|gene.b0767]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52697`
- `KEGG:ecj:JW0750;eco:b0767;ecoc:C3026_03890;`
- `GeneID:86863277;86945650;946398;`
- `GO:GO:0005829; GO:0006006; GO:0006098; GO:0009051; GO:0017057`
- `EC:3.1.1.31`

## Notes

6-phosphogluconolactonase (6-P-gluconolactonase) (Pgl) (EC 3.1.1.31)
