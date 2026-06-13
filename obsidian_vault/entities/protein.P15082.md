---
entity_id: "protein.P15082"
entity_type: "protein"
name: "srlR"
source_database: "UniProt"
source_id: "P15082"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "srlR gutR b2707 JW2676"
---

# srlR

`protein.P15082`

## Static

- Type: `protein`
- Source: `UniProt:P15082`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Glucitol operon repressor The "glucitol repressor," GutR (also called SrlR), is a DNA-binding transcription factor that represses an operon (gut) involved in transport and utilization of glucitol . This regulator is located in the unusual gut operon, which contains two glucitol-specific transcription factors, GutR and GutM, that regulate this operon negatively and positively, respectively; both regulators control transcription of glucitol PTS permease . Expression of gutR is activated in the presence of glucitol and in the absence of glucose. Although DNA binding by GutM does not depend on the presence of glucitol, this compound appears to be necessary for derepressing gutM, perhaps by interacting with GutR . In addition, Yamada et al. suggested that these regulators have contrary effects, but in the presence of glucitol, GutR interacts with this carbohydrate to dissociate from DNA, causing increments of GutM in sufficient amounts to increase transcription of the gut operon . To repress transcription, GutR recognizes DNA-binding sites, but no consensus sequence has been identified. When this protein represses genes involved in glucitol transport and utilization, it appears to bind to their regulatory regions without a coeffector . This regulator belongs to the DeoR family of repressors...

## Biological Role

Component of SrlR-D-sorbitol (complex.ecocyc.MONOMER-56).

## Annotation

Glucitol operon repressor

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MONOMER-56|complex.ecocyc.MONOMER-56]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b2707|gene.b2707]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15082`
- `KEGG:ecj:JW2676;eco:b2707;ecoc:C3026_14900;`
- `GeneID:75172789;948942;`
- `GO:GO:0000987; GO:0006355; GO:0009401; GO:0045892; GO:0098531`

## Notes

Glucitol operon repressor
