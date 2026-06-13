---
entity_id: "protein.P33931"
entity_type: "protein"
name: "ccmA"
source_database: "UniProt"
source_id: "P33931"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01707}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01707}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ccmA yejW b2201 JW5366"
---

# ccmA

`protein.P33931`

## Static

- Type: `protein`
- Source: `UniProt:P33931`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01707}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01707}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex CcmAB involved in the biogenesis of c-type cytochromes; once thought to export heme, this does not seem to be the case, but its exact role is uncertain. Responsible for energy coupling to the transport system. CcmA is the ATP-binding protein of a PWY-8147 "type I cytochrome c biogenesis system". ccmA is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmA deletion mutant cannot synthesize holocytochrome c but does produce heme-bound CCME-MONOMER CcmE (when CCMC-MONOMER CcmC is overproduced); CcmA and CCMB-MONOMER CcmB are implicated in heme transfer from holo-CcmE and attachment to apocytochrome c; CcmAB does not transport heme to the periplasm (and ). CcmA contains the 'Walker' ATP-binding sequence and the ABC signature motif; CcmA is detected in the membrane when CcmB is present and purified CcmAB has ATPase activity; inactivation of this activity does not abolish formation of holo-CcmE but does prevent production of c-type cytochromes...

## Biological Role

Component of CcmAB (complex.ecocyc.CPLX-9493), CcmABCD release complex (complex.ecocyc.CPLX-9495).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex CcmAB involved in the biogenesis of c-type cytochromes; once thought to export heme, this does not seem to be the case, but its exact role is uncertain. Responsible for energy coupling to the transport system.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX-9493|complex.ecocyc.CPLX-9493]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX-9495|complex.ecocyc.CPLX-9495]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2201|gene.b2201]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33931`
- `KEGG:ecj:JW5366;eco:b2201;`
- `GeneID:75172328;75206453;946714;`
- `GO:GO:0005524; GO:0015439; GO:0016887; GO:0017004; GO:0043190; GO:1903607; GO:1904334`
- `EC:7.6.2.5`

## Notes

Cytochrome c biogenesis ATP-binding export protein CcmA (EC 7.6.2.5) (Heme exporter protein A)
