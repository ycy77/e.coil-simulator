---
entity_id: "protein.P0AEM9"
entity_type: "protein"
name: "tcyJ"
source_database: "UniProt"
source_id: "P0AEM9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:20351115}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tcyJ fliY yzzR b1920 JW1905"
---

# tcyJ

`protein.P0AEM9`

## Static

- Type: `protein`
- Source: `UniProt:P0AEM9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:20351115}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex TcyJLN involved in L-cystine import (PubMed:20351115, PubMed:25139244, PubMed:25837721, PubMed:26350134). This high affinity cystine transporter is involved in resistance to oxidative stress by forming a L-cysteine/L-cystine shuttle system with the EamA transporter, which exports L-cysteine as reducing equivalents to the periplasm to prevent the cells from oxidative stress. Exported L-cysteine can reduce the periplasmic hydrogen peroxide to water, and then generated L-cystine is imported back into the cytoplasm via the TcyJLN complex (PubMed:20351115, PubMed:25837721). Functions at low cystine concentrations (PubMed:26350134). The system can also transport L-cysteine, diaminopimelic acid (DAP), djenkolate, lanthionine, D-cystine, homocystine, and it mediates accumulation of the toxic compounds L-selenaproline (SCA) and L-selenocystine (SeCys) (PubMed:25139244, PubMed:26350134). Binds cystine and DAP (PubMed:4564569, PubMed:8450713). {ECO:0000269|PubMed:20351115, ECO:0000269|PubMed:25139244, ECO:0000269|PubMed:25837721, ECO:0000269|PubMed:26350134, ECO:0000269|PubMed:4564569, ECO:0000269|PubMed:8450713}. TcyJ (formerly FliY) is the periplasmic binding protein of a cystine ABC transport system in E. coli K-12 . Purified FliY binds cystine in vitro (see further )...

## Biological Role

Component of cystine ABC transporter (complex.ecocyc.CPLX0-8152).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex TcyJLN involved in L-cystine import (PubMed:20351115, PubMed:25139244, PubMed:25837721, PubMed:26350134). This high affinity cystine transporter is involved in resistance to oxidative stress by forming a L-cysteine/L-cystine shuttle system with the EamA transporter, which exports L-cysteine as reducing equivalents to the periplasm to prevent the cells from oxidative stress. Exported L-cysteine can reduce the periplasmic hydrogen peroxide to water, and then generated L-cystine is imported back into the cytoplasm via the TcyJLN complex (PubMed:20351115, PubMed:25837721). Functions at low cystine concentrations (PubMed:26350134). The system can also transport L-cysteine, diaminopimelic acid (DAP), djenkolate, lanthionine, D-cystine, homocystine, and it mediates accumulation of the toxic compounds L-selenaproline (SCA) and L-selenocystine (SeCys) (PubMed:25139244, PubMed:26350134). Binds cystine and DAP (PubMed:4564569, PubMed:8450713). {ECO:0000269|PubMed:20351115, ECO:0000269|PubMed:25139244, ECO:0000269|PubMed:25837721, ECO:0000269|PubMed:26350134, ECO:0000269|PubMed:4564569, ECO:0000269|PubMed:8450713}.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8152|complex.ecocyc.CPLX0-8152]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1920|gene.b1920]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEM9`
- `KEGG:ecj:JW1905;eco:b1920;ecoc:C3026_10895;`
- `GeneID:93776227;948833;`
- `GO:GO:0006791; GO:0015184; GO:0015276; GO:0015811; GO:0015830; GO:0016597; GO:0030288; GO:0055052; GO:1903712`

## Notes

L-cystine-binding protein TcyJ (CBP) (Protein FliY) (Sulfate starvation-induced protein 7) (SSI7)
