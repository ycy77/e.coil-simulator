---
entity_id: "protein.P37774"
entity_type: "protein"
name: "tcyN"
source_database: "UniProt"
source_id: "P37774"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tcyN yecC b1917 JW1902"
---

# tcyN

`protein.P37774`

## Static

- Type: `protein`
- Source: `UniProt:P37774`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex TcyJLN involved in L-cystine import (PubMed:20351115, PubMed:25139244, PubMed:25837721, PubMed:26350134). This high affinity cystine transporter is involved in resistance to oxidative stress by forming a L-cysteine/L-cystine shuttle system with the EamA transporter, which exports L-cysteine as reducing equivalents to the periplasm to prevent the cells from oxidative stress. Exported L-cysteine can reduce the periplasmic hydrogen peroxide to water, and then generated L-cystine is imported back into the cytoplasm via the TcyJLN complex (PubMed:20351115, PubMed:25837721). Functions at low cystine concentrations (PubMed:26350134). The system can also transport L-cysteine, diaminopimelic acid (DAP), djenkolate, lanthionine, D-cystine, homocystine, and it mediates accumulation of the toxic compounds L-selenaproline (SCA) and L-selenocystine (SeCys) (PubMed:25139244, PubMed:26350134). Could also facilitate threonine efflux (PubMed:28911185). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:20351115, ECO:0000269|PubMed:25139244, ECO:0000269|PubMed:25837721, ECO:0000269|PubMed:26350134, ECO:0000269|PubMed:28911185, ECO:0000305}. tcyN encodes the ATP binding subunit of a cystine ABC transporter complex . TcyN contains sequence motifs conserved in ATP-binding cassette (ABC) proteins...

## Biological Role

Component of cystine ABC transporter (complex.ecocyc.CPLX0-8152).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex TcyJLN involved in L-cystine import (PubMed:20351115, PubMed:25139244, PubMed:25837721, PubMed:26350134). This high affinity cystine transporter is involved in resistance to oxidative stress by forming a L-cysteine/L-cystine shuttle system with the EamA transporter, which exports L-cysteine as reducing equivalents to the periplasm to prevent the cells from oxidative stress. Exported L-cysteine can reduce the periplasmic hydrogen peroxide to water, and then generated L-cystine is imported back into the cytoplasm via the TcyJLN complex (PubMed:20351115, PubMed:25837721). Functions at low cystine concentrations (PubMed:26350134). The system can also transport L-cysteine, diaminopimelic acid (DAP), djenkolate, lanthionine, D-cystine, homocystine, and it mediates accumulation of the toxic compounds L-selenaproline (SCA) and L-selenocystine (SeCys) (PubMed:25139244, PubMed:26350134). Could also facilitate threonine efflux (PubMed:28911185). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:20351115, ECO:0000269|PubMed:25139244, ECO:0000269|PubMed:25837721, ECO:0000269|PubMed:26350134, ECO:0000269|PubMed:28911185, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8152|complex.ecocyc.CPLX0-8152]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1917|gene.b1917]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37774`
- `KEGG:ecj:JW1902;eco:b1917;ecoc:C3026_10880;`
- `GeneID:946422;`
- `GO:GO:0005524; GO:0005886; GO:0015184; GO:0015424; GO:0015811; GO:0016887; GO:0042626; GO:0055052; GO:1903712`
- `EC:7.4.2.12`

## Notes

L-cystine transport system ATP-binding protein TcyN (EC 7.4.2.12)
