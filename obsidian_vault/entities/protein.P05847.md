---
entity_id: "protein.P05847"
entity_type: "protein"
name: "ttdA"
source_database: "UniProt"
source_id: "P05847"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ttdA ygjA b3061 JW3033"
---

# ttdA

`protein.P05847`

## Static

- Type: `protein`
- Source: `UniProt:P05847`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

L(+)-tartrate dehydratase subunit alpha (L-TTD alpha) (EC 4.2.1.32) The ttdA gene encodes the α subunit of L-tartrate dehydratase . Transcription of ttdA is activated by the LysR-type transcriptional activator TtdR in the presence of L-tartrate or meso-tartrate and is repressed by O2 and nitrate. Binding of TtdR to the ttdA-ttdR intergenic region has been shown . Anaerobic induction depends on FNR . TtdA appears to be involved in biofilm formation. A ΔttdA mutant shows a significant decrease in biofilm formation. Deletion of tqsA increases biofilm formation and increases expression of ttdA 11-fold . TtdA: "L-tartrate dehydratase A"

## Biological Role

Catalyzes (R,R)-tartrate hydro-lyase (oxaloacetate-forming) (reaction.R00339). Component of L(+)-tartrate dehydratase (complex.ecocyc.LTARTDEHYDRA-CPLX).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

L(+)-tartrate dehydratase subunit alpha (L-TTD alpha) (EC 4.2.1.32)

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00339|reaction.R00339]] `KEGG` `database` - via EC:4.2.1.32
- `is_component_of` --> [[complex.ecocyc.LTARTDEHYDRA-CPLX|complex.ecocyc.LTARTDEHYDRA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3061|gene.b3061]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05847`
- `KEGG:ecj:JW3033;eco:b3061;`
- `GeneID:93778932;947565;`
- `GO:GO:0004333; GO:0005829; GO:0006099; GO:0008730; GO:0044010; GO:0046872; GO:0051539; GO:1901275; GO:1901276; GO:1902494`
- `EC:4.2.1.32`

## Notes

L(+)-tartrate dehydratase subunit alpha (L-TTD alpha) (EC 4.2.1.32)
