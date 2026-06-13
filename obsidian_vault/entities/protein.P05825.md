---
entity_id: "protein.P05825"
entity_type: "protein"
name: "fepA"
source_database: "UniProt"
source_id: "P05825"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|PROSITE-ProRule:PRU01360}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU01360}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fepA fep feuB b0584 JW5086"
---

# fepA

`protein.P05825`

## Static

- Type: `protein`
- Source: `UniProt:P05825`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|PROSITE-ProRule:PRU01360}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU01360}.

## Enriched Summary

FUNCTION: This protein is involved in the initial step of iron uptake by binding ferrienterobactin (Fe-ENT), an iron chelatin siderophore that allows E.coli to extract iron from the environment. FepA also acts as a receptor for colicins B and D. FepA is an outer membrane (OM) protein that binds and transports ferric enterobactin (ferric enterochelin) ; it also binds and transports colicins B and D ( and reviewed in ). FepA mediated transport across the OM is energised by the inner membrane proton gradient; energy transduction is facilitated by the CPLX0-1923 (reviewed in ). FepA transports ferric enterobactin and its degradation products, CPD-21612 Fe(DHBS)2 and ferric dihydroxybenzoate (FeDHBA3) . FepA is a gated outer membrane porin . FepA is a 22-strand antiparallel β-barrel with an N-terminal globular domain which folds into the barrel plugging the pore. The structure contains several extracellular loops that would extend beyond the OM bilayer and may be involved ferric enterobactin binding . A 'ball and chain' mechanism of transport for FepA, in which the globular domain moves in and out of the channel to facilitate transport, has been proposed . The FepA channel is the largest OM channel characterised in E. coli . Purified FepA binds ferric enterobactin with high affinity . FepA physically interacts with TonB . FepA binds glucosylated enterobactin...

## Biological Role

Component of ferric enterobactin outer membrane transport complex (complex.ecocyc.CPLX0-1941).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: This protein is involved in the initial step of iron uptake by binding ferrienterobactin (Fe-ENT), an iron chelatin siderophore that allows E.coli to extract iron from the environment. FepA also acts as a receptor for colicins B and D.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1941|complex.ecocyc.CPLX0-1941]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0584|gene.b0584]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05825`
- `KEGG:ecj:JW5086;eco:b0584;ecoc:C3026_02910;`
- `GeneID:945193;`
- `GO:GO:0006879; GO:0009279; GO:0015344; GO:0015620; GO:0015685; GO:0016020; GO:0019904; GO:0022834; GO:0030313; GO:0033214; GO:0038023; GO:0042912; GO:0042914; GO:0042930; GO:0042931; GO:0044718; GO:1902495; GO:1903981`

## Notes

Ferrienterobactin receptor (Enterobactin outer-membrane receptor)
