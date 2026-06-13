---
entity_id: "protein.P75780"
entity_type: "protein"
name: "fiu"
source_database: "UniProt"
source_id: "P75780"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|PROSITE-ProRule:PRU01360}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU01360}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fiu ybiL b0805 JW0790"
---

# fiu

`protein.P75780`

## Static

- Type: `protein`
- Source: `UniProt:P75780`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|PROSITE-ProRule:PRU01360}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU01360}.

## Enriched Summary

FUNCTION: Involved in the active transport across the outer membrane of iron complexed with catecholate siderophores such as dihydroxybenzoylserine and dihydroxybenzoate. It derives its energy for transport by interacting with the trans-periplasmic membrane protein TonB. Can also transport catechol-substituted cephalosporins. Receptor for microcins M, H47 and E492. {ECO:0000269|PubMed:12949180, ECO:0000269|PubMed:16718603, ECO:0000269|PubMed:2139424, ECO:0000269|PubMed:2407721, ECO:0000269|PubMed:3072926}. Fiu is an integral outer membrane protein which mediates the TonB-dependent import of iron-catecholate complexes. Early work characterized an fiu mutant and identified an 83 kDa protein, produced in large amounts under iron limiting conditions which mediated the TonB dependent uptake of dihydroxybenzoylserine-iron complexes and 2-3-DIHYDROXYBENZOATE "dihydroxybenzoate" (an enterobactin precursor) (see also ). The physiological function of Fiu may be to recapture enterobactin hydrolysis products such as 2,3-dihydroxybenzoylserine and dihydroxybenzoate . Fiu is able to provide the cell with iron when it is present as the only outer-membrane iron transporter, likely through the transport of iron-complexed enterobactin breakdown products although this may not be its physiological (high-affinity) substrate...

## Biological Role

Component of ferric catecholate outer membrane transport complex I (complex.ecocyc.CPLX0-8541).

## Annotation

FUNCTION: Involved in the active transport across the outer membrane of iron complexed with catecholate siderophores such as dihydroxybenzoylserine and dihydroxybenzoate. It derives its energy for transport by interacting with the trans-periplasmic membrane protein TonB. Can also transport catechol-substituted cephalosporins. Receptor for microcins M, H47 and E492. {ECO:0000269|PubMed:12949180, ECO:0000269|PubMed:16718603, ECO:0000269|PubMed:2139424, ECO:0000269|PubMed:2407721, ECO:0000269|PubMed:3072926}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8541|complex.ecocyc.CPLX0-8541]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0805|gene.b0805]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75780`
- `KEGG:ecj:JW0790;eco:b0805;ecoc:C3026_05075;`
- `GeneID:946246;`
- `GO:GO:0006879; GO:0009279; GO:0015344; GO:0015891; GO:0016020; GO:0033214; GO:0038023; GO:0042884; GO:1902495`

## Notes

Catecholate siderophore receptor Fiu (Ferric iron uptake protein) (TonB-dependent receptor Fiu)
