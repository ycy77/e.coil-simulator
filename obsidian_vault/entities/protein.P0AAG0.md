---
entity_id: "protein.P0AAG0"
entity_type: "protein"
name: "dppD"
source_database: "UniProt"
source_id: "P0AAG0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dppD b3541 JW3510"
---

# dppD

`protein.P0AAG0`

## Static

- Type: `protein`
- Source: `UniProt:P0AAG0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter DppABCDF involved in dipeptide transport (PubMed:7536291). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:7536291, ECO:0000305}.; FUNCTION: When a foreign outer membrane heme receptor is expressed in E.coli, DppABCDF can also transport heme and its precursor, 5-aminolevulinic acid (ALA), from the periplasm into the cytoplasm. {ECO:0000269|PubMed:16905647, ECO:0000269|PubMed:8444807}. dppD encodes the predicted ATP-binding subunit of a dipeptide ABC transport system; DppD contains conserved ATP binding motifs and an ABC signature motif . DppD contains an FeS-Centers iron-sulfur cluster; purified DppD binds approximately 4 molecules of iron per monomer .

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

- `encodes` <-- [[gene.b3541|gene.b3541]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAG0`
- `KEGG:ecj:JW3510;eco:b3541;ecoc:C3026_19190;`
- `GeneID:75173734;75201990;948065;`
- `GO:GO:0005524; GO:0005886; GO:0015031; GO:0015232; GO:0016020; GO:0016887; GO:0035351; GO:0042938; GO:0051539; GO:0055052; GO:0071916`
- `EC:7.4.2.9`

## Notes

Dipeptide transport ATP-binding protein DppD (EC 7.4.2.9)
