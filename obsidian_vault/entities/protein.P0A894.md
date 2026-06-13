---
entity_id: "protein.P0A894"
entity_type: "protein"
name: "rapZ"
source_database: "UniProt"
source_id: "P0A894"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rapZ yhbJ b3205 JW3172"
---

# rapZ

`protein.P0A894`

## Static

- Type: `protein`
- Source: `UniProt:P0A894`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Modulates the synthesis of GlmS, by affecting the processing and stability of the regulatory small RNA GlmZ. When glucosamine-6-phosphate (GlcN6P) concentrations are high in the cell, RapZ binds GlmZ and targets it to cleavage by RNase E. Consequently, GlmZ is inactivated and unable to activate GlmS synthesis. Under low GlcN6P concentrations, RapZ is sequestered and inactivated by an other regulatory small RNA, GlmY, preventing GlmZ degradation and leading to synthesis of GlmS (PubMed:17824929, PubMed:23475961). Displays ATPase and GTPase activities in vitro. Can also hydrolyze pNPP (PubMed:19074378). {ECO:0000269|PubMed:17824929, ECO:0000269|PubMed:19074378, ECO:0000269|PubMed:23475961}.

## Biological Role

Component of RNase adaptor protein RapZ (complex.ecocyc.CPLX0-7998).

## Annotation

FUNCTION: Modulates the synthesis of GlmS, by affecting the processing and stability of the regulatory small RNA GlmZ. When glucosamine-6-phosphate (GlcN6P) concentrations are high in the cell, RapZ binds GlmZ and targets it to cleavage by RNase E. Consequently, GlmZ is inactivated and unable to activate GlmS synthesis. Under low GlcN6P concentrations, RapZ is sequestered and inactivated by an other regulatory small RNA, GlmY, preventing GlmZ degradation and leading to synthesis of GlmS (PubMed:17824929, PubMed:23475961). Displays ATPase and GTPase activities in vitro. Can also hydrolyze pNPP (PubMed:19074378). {ECO:0000269|PubMed:17824929, ECO:0000269|PubMed:19074378, ECO:0000269|PubMed:23475961}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7998|complex.ecocyc.CPLX0-7998]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3205|gene.b3205]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A894`
- `KEGG:ecj:JW3172;eco:b3205;ecoc:C3026_17440;`
- `GeneID:86862398;93778776;947727;`
- `GO:GO:0003723; GO:0005524; GO:0005525; GO:0032991; GO:0042802; GO:0050779; GO:0051289; GO:0060090; GO:0097367`

## Notes

RNase adapter protein RapZ
