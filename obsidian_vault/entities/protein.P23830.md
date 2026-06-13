---
entity_id: "protein.P23830"
entity_type: "protein"
name: "pssA"
source_database: "UniProt"
source_id: "P23830"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm. Cell inner membrane {ECO:0000269|PubMed:39693441}; Peripheral membrane protein; Cytoplasmic side {ECO:0000269|PubMed:39693441}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pssA pss b2585 JW2569"
---

# pssA

`protein.P23830`

## Static

- Type: `protein`
- Source: `UniProt:P23830`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm. Cell inner membrane {ECO:0000269|PubMed:39693441}; Peripheral membrane protein; Cytoplasmic side {ECO:0000269|PubMed:39693441}.

## Enriched Summary

FUNCTION: Catalyzes the conversion of cytidine diphosphate diacylglycerol (CDP-DG) and L-serine into phosphatidylserine (PubMed:39693441, PubMed:8824831). Essential for biosynthesis of phosphatidylethanolamine, one of the major membrane phospholipids (PubMed:39693441, PubMed:8824831). Phosphatidylserine is later converted into phosphatidylethanolamine via the action of phosphatidylserine decarboxylase psd (PubMed:39693441, PubMed:8824831). Associates with the bacterial membrane for its role, which depends on the levels of anionic phospholipids in the membrane (PubMed:39693441, PubMed:8824831). {ECO:0000269|PubMed:39693441, ECO:0000269|PubMed:8824831}.

## Biological Role

Component of phosphatidylserine synthase (complex.ecocyc.CPLX0-12524).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of cytidine diphosphate diacylglycerol (CDP-DG) and L-serine into phosphatidylserine (PubMed:39693441, PubMed:8824831). Essential for biosynthesis of phosphatidylethanolamine, one of the major membrane phospholipids (PubMed:39693441, PubMed:8824831). Phosphatidylserine is later converted into phosphatidylethanolamine via the action of phosphatidylserine decarboxylase psd (PubMed:39693441, PubMed:8824831). Associates with the bacterial membrane for its role, which depends on the levels of anionic phospholipids in the membrane (PubMed:39693441, PubMed:8824831). {ECO:0000269|PubMed:39693441, ECO:0000269|PubMed:8824831}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12524|complex.ecocyc.CPLX0-12524]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2585|gene.b2585]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23830`
- `KEGG:ecj:JW2569;eco:b2585;ecoc:C3026_14325;`
- `GeneID:75172701;75206279;947059;`
- `GO:GO:0003882; GO:0005543; GO:0005737; GO:0005829; GO:0005886; GO:0008444; GO:0008654; GO:0032049`
- `EC:2.7.8.8`

## Notes

CDP-diacylglycerol--serine O-phosphatidyltransferase PssA (EC 2.7.8.8) (Phosphatidylserine synthase)
