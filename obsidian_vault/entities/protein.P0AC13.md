---
entity_id: "protein.P0AC13"
entity_type: "protein"
name: "folP"
source_database: "UniProt"
source_id: "P0AC13"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "folP dhpS b3177 JW3144"
---

# folP

`protein.P0AC13`

## Static

- Type: `protein`
- Source: `UniProt:P0AC13`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the condensation of para-aminobenzoate (pABA) with 6-hydroxymethyl-7,8-dihydropterin diphosphate (DHPt-PP) to form 7,8-dihydropteroate (H2Pte), the immediate precursor of folate derivatives. {ECO:0000269|PubMed:368012, ECO:0000269|PubMed:37419898}.

## Biological Role

Component of dihydropteroate synthase (complex.ecocyc.H2PTEROATESYNTH-CPLX).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the condensation of para-aminobenzoate (pABA) with 6-hydroxymethyl-7,8-dihydropterin diphosphate (DHPt-PP) to form 7,8-dihydropteroate (H2Pte), the immediate precursor of folate derivatives. {ECO:0000269|PubMed:368012, ECO:0000269|PubMed:37419898}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.H2PTEROATESYNTH-CPLX|complex.ecocyc.H2PTEROATESYNTH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3177|gene.b3177]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC13`
- `KEGG:ecj:JW3144;eco:b3177;ecoc:C3026_17300;`
- `GeneID:93778804;947691;`
- `GO:GO:0004156; GO:0005737; GO:0005829; GO:0009410; GO:0046654; GO:0046656; GO:0046872`
- `EC:2.5.1.15`

## Notes

Dihydropteroate synthase (DHPS) (EC 2.5.1.15) (Dihydropteroate pyrophosphorylase)
