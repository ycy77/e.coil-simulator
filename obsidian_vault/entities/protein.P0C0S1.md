---
entity_id: "protein.P0C0S1"
entity_type: "protein"
name: "mscS"
source_database: "UniProt"
source_id: "P0C0S1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10202137, ECO:0000269|PubMed:12551944, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:23012406, ECO:0000269|PubMed:23074248, ECO:0000269|PubMed:2436228, ECO:0000269|PubMed:7595939}; Multi-pass membrane protein {ECO:0000269|PubMed:12446901, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:23012406, ECO:0000269|PubMed:23339071, ECO:0000269|PubMed:26551077}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mscS yggB b2924 JW2891"
---

# mscS

`protein.P0C0S1`

## Static

- Type: `protein`
- Source: `UniProt:P0C0S1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10202137, ECO:0000269|PubMed:12551944, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:23012406, ECO:0000269|PubMed:23074248, ECO:0000269|PubMed:2436228, ECO:0000269|PubMed:7595939}; Multi-pass membrane protein {ECO:0000269|PubMed:12446901, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:23012406, ECO:0000269|PubMed:23339071, ECO:0000269|PubMed:26551077}.

## Enriched Summary

FUNCTION: Mechanosensitive channel that participates in the regulation of osmotic pressure changes within the cell, opening in response to stretch forces in the membrane lipid bilayer, without the need for other proteins. Contributes to normal resistance to hypoosmotic shock. Forms an ion channel of 1.0 nanosiemens conductance with a slight preference for anions. The channel is sensitive to voltage; as the membrane is depolarized, less tension is required to open the channel and vice versa. The channel is characterized by short bursts of activity that last for a few seconds. {ECO:0000269|PubMed:10202137, ECO:0000269|PubMed:12015316, ECO:0000269|PubMed:12080120, ECO:0000269|PubMed:12446901, ECO:0000269|PubMed:12551944, ECO:0000269|PubMed:12767977, ECO:0000269|PubMed:23012406, ECO:0000269|PubMed:23074248, ECO:0000269|PubMed:2436228, ECO:0000269|PubMed:26551077, ECO:0000269|PubMed:7595939}. MscS is a mechanosensitive channel of small conductance; MscS conductance is 0.8-1 nanosiemens in E. coli giant protoplasts . MscS activity is adaptive, that is, it declines in response to sustained stimulation . In patch clamp experiments MscS activity occurs in short bursts that last for a few seconds . Gating of MscS is controlled by tension within, or voltage across the lipid bilayer...

## Biological Role

Component of small conductance mechanosensitive channel MscS (complex.ecocyc.CPLX0-7626).

## Annotation

FUNCTION: Mechanosensitive channel that participates in the regulation of osmotic pressure changes within the cell, opening in response to stretch forces in the membrane lipid bilayer, without the need for other proteins. Contributes to normal resistance to hypoosmotic shock. Forms an ion channel of 1.0 nanosiemens conductance with a slight preference for anions. The channel is sensitive to voltage; as the membrane is depolarized, less tension is required to open the channel and vice versa. The channel is characterized by short bursts of activity that last for a few seconds. {ECO:0000269|PubMed:10202137, ECO:0000269|PubMed:12015316, ECO:0000269|PubMed:12080120, ECO:0000269|PubMed:12446901, ECO:0000269|PubMed:12551944, ECO:0000269|PubMed:12767977, ECO:0000269|PubMed:23012406, ECO:0000269|PubMed:23074248, ECO:0000269|PubMed:2436228, ECO:0000269|PubMed:26551077, ECO:0000269|PubMed:7595939}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7626|complex.ecocyc.CPLX0-7626]] `EcoCyc` `database` - EcoCyc component coefficient=7 | EcoCyc protcplxs.col coefficient=7

## Incoming Edges (1)

- `encodes` <-- [[gene.b2924|gene.b2924]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C0S1`
- `KEGG:ecj:JW2891;eco:b2924;ecoc:C3026_16020;`
- `GeneID:93779074;947416;`
- `GO:GO:0005886; GO:0008381; GO:0009992; GO:0016020; GO:0034220; GO:0042802; GO:0051260`

## Notes

Small-conductance mechanosensitive channel
