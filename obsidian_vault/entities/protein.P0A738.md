---
entity_id: "protein.P0A738"
entity_type: "protein"
name: "moaC"
source_database: "UniProt"
source_id: "P0A738"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "moaC chlA3 b0783 JW0766"
---

# moaC

`protein.P0A738`

## Static

- Type: `protein`
- Source: `UniProt:P0A738`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate to cyclic pyranopterin monophosphate (cPMP). {ECO:0000255|HAMAP-Rule:MF_01224, ECO:0000269|PubMed:25941396}.

## Biological Role

Catalyzes (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate lyase (cyclic pyranopterin phosphate-forming) (reaction.R11372). Component of cyclic pyranopterin monophosphate synthase (complex.ecocyc.CPLX-8331).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate to cyclic pyranopterin monophosphate (cPMP). {ECO:0000255|HAMAP-Rule:MF_01224, ECO:0000269|PubMed:25941396}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R11372|reaction.R11372]] `KEGG` `database` - via EC:4.6.1.17
- `is_component_of` --> [[complex.ecocyc.CPLX-8331|complex.ecocyc.CPLX-8331]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0783|gene.b0783]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A738`
- `KEGG:ecj:JW0766;eco:b0783;ecoc:C3026_04965;`
- `GeneID:86863293;86945666;945397;`
- `GO:GO:0006777; GO:0032991; GO:0042802; GO:0061799`
- `EC:4.6.1.17`

## Notes

Cyclic pyranopterin monophosphate synthase (EC 4.6.1.17) (Molybdenum cofactor biosynthesis protein C)
