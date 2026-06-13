---
entity_id: "protein.P62617"
entity_type: "protein"
name: "ispF"
source_database: "UniProt"
source_id: "P62617"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ispF mecS ygbB b2746 JW2716"
---

# ispF

`protein.P62617`

## Static

- Type: `protein`
- Source: `UniProt:P62617`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the biosynthesis of isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP), two major building blocks of isoprenoid compounds. Catalyzes the conversion of 4-diphosphocytidyl-2-C-methyl-D-erythritol 2-phosphate (CDP-ME2P) to 2-C-methyl-D-erythritol 2,4-cyclodiphosphate (ME-CPP) with a corresponding release of cytidine 5-monophosphate (CMP). Also converts 4-diphosphocytidyl-2-C-methyl-D-erythritol into 2-C-methyl-D-erythritol 3,4-cyclophosphate and CMP. {ECO:0000269|PubMed:10694574, ECO:0000269|PubMed:22839733}.

## Biological Role

Component of 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase (complex.ecocyc.CPLX0-721).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP), two major building blocks of isoprenoid compounds. Catalyzes the conversion of 4-diphosphocytidyl-2-C-methyl-D-erythritol 2-phosphate (CDP-ME2P) to 2-C-methyl-D-erythritol 2,4-cyclodiphosphate (ME-CPP) with a corresponding release of cytidine 5-monophosphate (CMP). Also converts 4-diphosphocytidyl-2-C-methyl-D-erythritol into 2-C-methyl-D-erythritol 3,4-cyclophosphate and CMP. {ECO:0000269|PubMed:10694574, ECO:0000269|PubMed:22839733}.

## Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-721|complex.ecocyc.CPLX0-721]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b2746|gene.b2746]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P62617`
- `KEGG:ecj:JW2716;eco:b2746;ecoc:C3026_15100;`
- `GeneID:86860837;93779260;945057;`
- `GO:GO:0006744; GO:0008270; GO:0008685; GO:0016114; GO:0019288; GO:0030145; GO:0042802; GO:0046872`
- `EC:4.6.1.12`

## Notes

2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase (MECDP-synthase) (MECPP-synthase) (MECPS) (EC 4.6.1.12)
