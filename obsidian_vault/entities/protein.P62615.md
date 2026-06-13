---
entity_id: "protein.P62615"
entity_type: "protein"
name: "ispE"
source_database: "UniProt"
source_id: "P62615"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ispE ipk ychB b1208 JW1199"
---

# ispE

`protein.P62615`

## Static

- Type: `protein`
- Source: `UniProt:P62615`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of the position 2 hydroxy group of 4-diphosphocytidyl-2C-methyl-D-erythritol (PubMed:10570138, PubMed:10655484, Ref.6). Phosphorylates isopentenyl phosphate at low rates. Also acts on isopentenol, and, much less efficiently, dimethylallyl alcohol. Dimethylallyl monophosphate does not serve as a substrate (PubMed:10570138). {ECO:0000269|PubMed:10570138, ECO:0000269|PubMed:10655484, ECO:0000269|Ref.6}.

## Biological Role

Component of 4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol kinase (complex.ecocyc.CPLX0-3841).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of the position 2 hydroxy group of 4-diphosphocytidyl-2C-methyl-D-erythritol (PubMed:10570138, PubMed:10655484, Ref.6). Phosphorylates isopentenyl phosphate at low rates. Also acts on isopentenol, and, much less efficiently, dimethylallyl alcohol. Dimethylallyl monophosphate does not serve as a substrate (PubMed:10570138). {ECO:0000269|PubMed:10570138, ECO:0000269|PubMed:10655484, ECO:0000269|Ref.6}.

## Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3841|complex.ecocyc.CPLX0-3841]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1208|gene.b1208]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P62615`
- `KEGG:ecj:JW1199;eco:b1208;ecoc:C3026_07100;`
- `GeneID:945774;`
- `GO:GO:0005524; GO:0016114; GO:0019288; GO:0050515`
- `EC:2.7.1.148`

## Notes

4-diphosphocytidyl-2-C-methyl-D-erythritol kinase (CMK) (EC 2.7.1.148) (4-(cytidine-5'-diphospho)-2-C-methyl-D-erythritol kinase)
