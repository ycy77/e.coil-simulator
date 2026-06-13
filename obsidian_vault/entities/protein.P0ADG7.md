---
entity_id: "protein.P0ADG7"
entity_type: "protein"
name: "guaB"
source_database: "UniProt"
source_id: "P0ADG7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "guaB guaR b2508 JW5401"
---

# guaB

`protein.P0ADG7`

## Static

- Type: `protein`
- Source: `UniProt:P0ADG7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of inosine 5'-phosphate (IMP) to xanthosine 5'-phosphate (XMP), the first committed and rate-limiting step in the de novo synthesis of guanine nucleotides, and therefore plays an important role in the regulation of cell growth. {ECO:0000255|HAMAP-Rule:MF_01964, ECO:0000269|PubMed:9341229}.

## Biological Role

Component of inosine 5'-monophosphate dehydrogenase (complex.ecocyc.IMP-DEHYDROG-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of inosine 5'-phosphate (IMP) to xanthosine 5'-phosphate (XMP), the first committed and rate-limiting step in the de novo synthesis of guanine nucleotides, and therefore plays an important role in the regulation of cell growth. {ECO:0000255|HAMAP-Rule:MF_01964, ECO:0000269|PubMed:9341229}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.IMP-DEHYDROG-CPLX|complex.ecocyc.IMP-DEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2508|gene.b2508]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADG7`
- `KEGG:ecj:JW5401;eco:b2508;ecoc:C3026_13910;`
- `GeneID:86860630;93774628;946985;`
- `GO:GO:0003697; GO:0003938; GO:0005524; GO:0005829; GO:0006177; GO:0006183; GO:0009411; GO:0032991; GO:0042802; GO:0046872; GO:0051289; GO:0097216; GO:1990829`
- `EC:1.1.1.205`

## Notes

Inosine-5'-monophosphate dehydrogenase (IMP dehydrogenase) (IMPD) (IMPDH) (EC 1.1.1.205)
