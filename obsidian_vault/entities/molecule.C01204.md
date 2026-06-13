---
entity_id: "molecule.C01204"
entity_type: "small_molecule"
name: "Phytic acid"
source_database: "KEGG"
source_id: "C01204"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phytic acid"
  - "Phytate"
  - "myo-Inositol hexakisphosphate"
  - "1D-myo-Inositol 1,2,3,4,5,6-hexakisphosphate"
  - "D-myo-Inositol 1,2,3,4,5,6-hexakisphosphate"
  - "myo-Inositol 1,2,3,4,5,6-hexakisphosphate"
  - "Inositol 1,2,3,4,5,6-hexakisphosphate"
  - "1D-myo-Inositol hexakisphosphate"
---

# Phytic acid

`molecule.C01204`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01204`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phytic acid; Phytate; myo-Inositol hexakisphosphate; 1D-myo-Inositol 1,2,3,4,5,6-hexakisphosphate; D-myo-Inositol 1,2,3,4,5,6-hexakisphosphate; myo-Inositol 1,2,3,4,5,6-hexakisphosphate; Inositol 1,2,3,4,5,6-hexakisphosphate; 1D-myo-Inositol hexakisphosphate EcoCyc common name: phytate. MI-HEXAKISPHOSPHATE Phytate (phytic acid) is one of the most prevalent forms of phosphorylated inositols in the eukaryotic cell, with a total concentration of 15-100 μM . It's cellular distribution is not completely known - some of it is soluble, some is "wall-papered" around membranes, while some is bound to proteins . In plant seeds, large amount of phytate are complexed with cations and deposited as globular inclusions in membrane-bound storage bodies . The compound has been proposed to have a number of signaling roles, including regulation of insulin exocytosis , regulation of nuclear mRNA export , binding of the clathrin assembly proteins AP2 and AP3 , inhibition of clathrin cage assembly , and inhibition of serine and threonine protein phosphatases that are thought to regulate L-type Ca2+ channels .

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00562` Inositol phosphate metabolism (KEGG)

## Annotation

KEGG compound: Phytic acid; Phytate; myo-Inositol hexakisphosphate; 1D-myo-Inositol 1,2,3,4,5,6-hexakisphosphate; D-myo-Inositol 1,2,3,4,5,6-hexakisphosphate; myo-Inositol 1,2,3,4,5,6-hexakisphosphate; Inositol 1,2,3,4,5,6-hexakisphosphate; 1D-myo-Inositol hexakisphosphate

## Pathways

- `eco00562` Inositol phosphate metabolism (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.ecocyc.RXN-10940|reaction.ecocyc.RXN-10940]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1001|reaction.ecocyc.RXN0-1001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01204`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
