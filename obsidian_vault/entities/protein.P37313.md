---
entity_id: "protein.P37313"
entity_type: "protein"
name: "dppF"
source_database: "UniProt"
source_id: "P37313"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dppF dppE b3540 JW3509"
---

# dppF

`protein.P37313`

## Static

- Type: `protein`
- Source: `UniProt:P37313`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter DppABCDF involved in dipeptide transport (PubMed:7536291). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:7536291, ECO:0000305}.; FUNCTION: When a foreign outer membrane heme receptor is expressed in E.coli, DppABCDF can also transport heme and its precursor, 5-aminolevulinic acid (ALA), from the periplasm into the cytoplasm. {ECO:0000269|PubMed:16905647, ECO:0000269|PubMed:8444807}. dppF encodes the predicted ATP-binding subunit of a dipeptide ABC transport system; DppF contains conserved ATP binding motifs .

## Biological Role

Component of dipeptide ABC transporter (complex.ecocyc.ABC-8-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter DppABCDF involved in dipeptide transport (PubMed:7536291). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:7536291, ECO:0000305}.; FUNCTION: When a foreign outer membrane heme receptor is expressed in E.coli, DppABCDF can also transport heme and its precursor, 5-aminolevulinic acid (ALA), from the periplasm into the cytoplasm. {ECO:0000269|PubMed:16905647, ECO:0000269|PubMed:8444807}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-8-CPLX|complex.ecocyc.ABC-8-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3540|gene.b3540]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37313`
- `KEGG:ecj:JW3509;eco:b3540;ecoc:C3026_19185;`
- `GeneID:948056;`
- `GO:GO:0005524; GO:0005886; GO:0009314; GO:0015031; GO:0015232; GO:0016020; GO:0016887; GO:0022857; GO:0035351; GO:0042938; GO:0055052; GO:0071916`
- `EC:7.4.2.9`

## Notes

Dipeptide transport ATP-binding protein DppF (EC 7.4.2.9)
