---
entity_id: "protein.P12998"
entity_type: "protein"
name: "bioF"
source_database: "UniProt"
source_id: "P12998"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bioF b0776 JW0759"
---

# bioF

`protein.P12998`

## Static

- Type: `protein`
- Source: `UniProt:P12998`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the decarboxylative condensation of pimeloyl-[acyl-carrier protein] and L-alanine to produce 8-amino-7-oxononanoate (AON), [acyl-carrier protein], and carbon dioxide. Can also use pimeloyl-CoA instead of pimeloyl-ACP as substrate, but it is believed that pimeloyl-ACP rather than pimeloyl-CoA is the physiological substrate of BioF. {ECO:0000269|PubMed:10642176, ECO:0000269|PubMed:20693992}.

## Biological Role

Component of 8-amino-7-oxononanoate synthase (complex.ecocyc.7KAPSYN-CPLX).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the decarboxylative condensation of pimeloyl-[acyl-carrier protein] and L-alanine to produce 8-amino-7-oxononanoate (AON), [acyl-carrier protein], and carbon dioxide. Can also use pimeloyl-CoA instead of pimeloyl-ACP as substrate, but it is believed that pimeloyl-ACP rather than pimeloyl-CoA is the physiological substrate of BioF. {ECO:0000269|PubMed:10642176, ECO:0000269|PubMed:20693992}.

## Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.7KAPSYN-CPLX|complex.ecocyc.7KAPSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0776|gene.b0776]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P12998`
- `KEGG:ecj:JW0759;eco:b0776;ecoc:C3026_04930;`
- `GeneID:945384;`
- `GO:GO:0008710; GO:0009102; GO:0030170; GO:0042803`
- `EC:2.3.1.47`

## Notes

8-amino-7-oxononanoate synthase (AONS) (EC 2.3.1.47) (7-keto-8-amino-pelargonic acid synthase) (7-KAP synthase) (KAPA synthase) (8-amino-7-ketopelargonate synthase)
