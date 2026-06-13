---
entity_id: "protein.P0A9V1"
entity_type: "protein"
name: "lptB"
source_database: "UniProt"
source_id: "P0A9V1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137}. Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}; Cytoplasmic side {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lptB yhbG b3201 JW3168"
---

# lptB

`protein.P0A9V1`

## Static

- Type: `protein`
- Source: `UniProt:P0A9V1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137}. Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}; Cytoplasmic side {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex LptBFG involved in the translocation of lipopolysaccharide (LPS) from the inner membrane to the outer membrane. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:17056748, ECO:0000269|PubMed:18424520}. LptB is a cytoplasmic ATPase that energises the transport and assembly of lipopolysaccharide (LPS) by the Lpt system. Depletion of LptB results in impaired LPS transport and outer membrane biogenesis . LptB forms a complex with LptF, LptG and LptC . Sequence analysis suggests that LptB has an ATP binding fold . Purified LptB has ATPase activity in vitro; purified LptB has a KM for ATP of 0.56 mM; ATP binding to LptB is cooperative . Crystal structures of LptB bound to ADP and a catalytically inactive LptB mutant (LptBE163Q) bound to ATP have been obtained and suggest that ATP hydrolysis induces conformational change in LptB . Purified, crystallised LptB is an L-shaped molecule consisting of an ATPase domain containing the characteristic motifs (Walker A and B, and Q loop) and an α-helical domain . LptB contains a binding site (which includes residues F90, R91, L93 and R150) which contacts the coupling helices of LptF and LptG...

## Biological Role

Component of lipopolysaccharide transport system (complex.ecocyc.CPLX0-7992).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex LptBFG involved in the translocation of lipopolysaccharide (LPS) from the inner membrane to the outer membrane. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:17056748, ECO:0000269|PubMed:18424520}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7992|complex.ecocyc.CPLX0-7992]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3201|gene.b3201]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9V1`
- `KEGG:ecj:JW3168;eco:b3201;ecoc:C3026_17420;`
- `GeneID:86862402;93778780;947725;`
- `GO:GO:0005524; GO:0005737; GO:0005886; GO:0015920; GO:0016020; GO:0016887; GO:0043165; GO:0043190; GO:0055085; GO:1990351`
- `EC:7.5.2.-`

## Notes

Lipopolysaccharide export system ATP-binding protein LptB (EC 7.5.2.-)
