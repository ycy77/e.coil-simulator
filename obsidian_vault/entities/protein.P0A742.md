---
entity_id: "protein.P0A742"
entity_type: "protein"
name: "mscL"
source_database: "UniProt"
source_id: "P0A742"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00115, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23416054, ECO:0000269|PubMed:7511799, ECO:0000269|PubMed:8890153, ECO:0000269|PubMed:9632260, ECO:0000305|PubMed:21151884, ECO:0000305|PubMed:23875651}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00115, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8890153}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mscL yhdC b3291 JW3252"
---

# mscL

`protein.P0A742`

## Static

- Type: `protein`
- Source: `UniProt:P0A742`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00115, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23416054, ECO:0000269|PubMed:7511799, ECO:0000269|PubMed:8890153, ECO:0000269|PubMed:9632260, ECO:0000305|PubMed:21151884, ECO:0000305|PubMed:23875651}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00115, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8890153}.

## Enriched Summary

FUNCTION: Mechanosensitive channel that opens in response to stretch forces in the membrane lipid bilayer. Forms a nonselective ion channel with a conductance of about 4 nanosiemens. Participates in the regulation of osmotic pressure changes within the cell. Opens at a pressure just below that which would cause cell disruption and death. The force required to trigger channel opening depends on the membrane lipids composition. {ECO:0000269|PubMed:10202137, ECO:0000269|PubMed:23416054, ECO:0000269|PubMed:23875651, ECO:0000269|PubMed:7511799, ECO:0000269|PubMed:9632260}. MscL is a mechanosensitive channel of large conductance. MscL converts mechanical tension in the cell membrane into an electrochemical response. Upon osmotic downshift water flows into a cell, increasing pressure on the membrane which activates MscL and allows solutes to exit. MscL acts as a pressure release valve, preventing cell lysis due to increased osmotic pressure. The protein was originally discovered by patch clamp studies on protein fractions reconstituted into liposomes . MscL conductance is 2.5 nanosiemens in E. coli spheroplasts . MscL activates at pressures close to those causing cell lysis . MscL was the first cloned protein shown to respond to mechanical force by opening a large aqueous pore...

## Biological Role

Component of large conductance mechanosensitive channel (complex.ecocyc.CPLX0-7627).

## Annotation

FUNCTION: Mechanosensitive channel that opens in response to stretch forces in the membrane lipid bilayer. Forms a nonselective ion channel with a conductance of about 4 nanosiemens. Participates in the regulation of osmotic pressure changes within the cell. Opens at a pressure just below that which would cause cell disruption and death. The force required to trigger channel opening depends on the membrane lipids composition. {ECO:0000269|PubMed:10202137, ECO:0000269|PubMed:23416054, ECO:0000269|PubMed:23875651, ECO:0000269|PubMed:7511799, ECO:0000269|PubMed:9632260}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7627|complex.ecocyc.CPLX0-7627]] `EcoCyc` `database` - EcoCyc component coefficient=5 | EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5

## Incoming Edges (1)

- `encodes` <-- [[gene.b3291|gene.b3291]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A742`
- `KEGG:ecj:JW3252;eco:b3291;ecoc:C3026_17890;`
- `GeneID:75173461;947787;`
- `GO:GO:0005886; GO:0006811; GO:0008381; GO:0009992; GO:0016020; GO:0034220; GO:0042802`

## Notes

Large-conductance mechanosensitive channel
