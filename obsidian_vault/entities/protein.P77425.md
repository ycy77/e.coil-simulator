---
entity_id: "protein.P77425"
entity_type: "protein"
name: "allC"
source_database: "UniProt"
source_id: "P77425"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "allC glxB7 ylbB b0516 JW0504"
---

# allC

`protein.P77425`

## Static

- Type: `protein`
- Source: `UniProt:P77425`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:10601204, PubMed:20038185). Catalyzes specifically the hydrolysis of allantoate to yield CO2, NH3 and S-ureidoglycine, which is unstable and readily undergoes a second deamination by S-ureidoglycine aminohydrolase AllE to yield S-ureidoglycolate and NH3 (PubMed:20038185). In vivo, the spontaneous release of S-ureidoglycolate and ammonia from S-ureidoglycine appears to be too slow to sustain an efficient flux of nitrogen (PubMed:20038185). {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:20038185}.

## Biological Role

Component of allantoate amidohydrolase (complex.ecocyc.CPLX-7524).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:10601204, PubMed:20038185). Catalyzes specifically the hydrolysis of allantoate to yield CO2, NH3 and S-ureidoglycine, which is unstable and readily undergoes a second deamination by S-ureidoglycine aminohydrolase AllE to yield S-ureidoglycolate and NH3 (PubMed:20038185). In vivo, the spontaneous release of S-ureidoglycolate and ammonia from S-ureidoglycine appears to be too slow to sustain an efficient flux of nitrogen (PubMed:20038185). {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:20038185}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-7524|complex.ecocyc.CPLX-7524]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0516|gene.b0516]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77425`
- `KEGG:ecj:JW0504;eco:b0516;ecoc:C3026_02530;`
- `GeneID:945150;`
- `GO:GO:0000256; GO:0005737; GO:0006144; GO:0008270; GO:0009442; GO:0030145; GO:0042803; GO:0047652`
- `EC:3.5.3.9`

## Notes

Allantoate amidohydrolase (AAH) (EC 3.5.3.9) (Allantoate deiminase)
