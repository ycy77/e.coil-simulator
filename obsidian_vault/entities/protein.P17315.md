---
entity_id: "protein.P17315"
entity_type: "protein"
name: "cirA"
source_database: "UniProt"
source_id: "P17315"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|PROSITE-ProRule:PRU01360}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU01360}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cirA cir feuA b2155 JW2142"
---

# cirA

`protein.P17315`

## Static

- Type: `protein`
- Source: `UniProt:P17315`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|PROSITE-ProRule:PRU01360}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU01360}.

## Enriched Summary

FUNCTION: Not yet known. Postulated to participate in iron transport. Outer membrane receptor for colicins IA and IB. Cir is a member of the Outer Membrane Receptor (OMR) family of porins. Cir is a TonB-dependent iron-siderophore complex uptake receptor . The substrate spectrum of Cir is very similar to that of Fiu. Cir transports monomers, dimers and linear trimers of 2,3-dihydroxybenzoylserine . Cir transports the ferric dicatecholate CPD-21612 Fe(DHBS)2 and the siderophore cephalosporin, CPD-28221 . Cir is also a receptor for colicins IA, IB, and V and microcins E492, H47, and M . Cir acts as both the receptor and translocator for colicin IA . Crystal structures of Cir alone and in complex with the receptor domain of colicin IA have been reported . The class IIb microcin MccM targets the TonB-dependent siderophore receptors G6414-MONOMER Fiu, CirA, and EG10293-MONOMER FepA for entry. Expression of CirA is posttranscriptionally regulated by several small RNAs as well as by Hfq. Outer membrane protein (OMP) localisation and turnover has been studied using labelled, modified colicin 1a which forms a complex with Cir but is blocked for import. OMPs cluster in islands which are stabilised by promiscuous protein-protein interactions; OMPs engage in both homologous and heterologous associations that slow their diffusion in the outer membrane...

## Biological Role

Component of ferric catecholate outer membrane transport complex II (complex.ecocyc.CPLX0-8553).

## Annotation

FUNCTION: Not yet known. Postulated to participate in iron transport. Outer membrane receptor for colicins IA and IB.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8553|complex.ecocyc.CPLX0-8553]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2155|gene.b2155]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17315`
- `KEGG:ecj:JW2142;eco:b2155;ecoc:C3026_12080;`
- `GeneID:949042;`
- `GO:GO:0006879; GO:0009279; GO:0015343; GO:0015344; GO:0016020; GO:0042912; GO:0044718; GO:1902495`

## Notes

Colicin I receptor
