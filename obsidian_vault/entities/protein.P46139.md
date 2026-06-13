---
entity_id: "protein.P46139"
entity_type: "protein"
name: "dgcN"
source_database: "UniProt"
source_id: "P46139"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}. Note=Localizes to the midcell in a Z ring-dependent manner in response to cell envelope stress. {ECO:0000269|PubMed:27507823}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgcN yfiN b2604 JW2585"
---

# dgcN

`protein.P46139`

## Static

- Type: `protein`
- Source: `UniProt:P46139`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}. Note=Localizes to the midcell in a Z ring-dependent manner in response to cell envelope stress. {ECO:0000269|PubMed:27507823}.

## Enriched Summary

FUNCTION: Bifunctional protein that catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) in response to reductive stress and then dynamically relocates to the division site to arrest cell division in response to envelope stress. In the presence of high intracellular c-di-GMP levels, and in response to envelope stress, interacts with cell division proteins and halts cell division, without disassembling the Z ring, but by blocking its further progress toward cytokinesis (PubMed:27507823). Part of a network that regulates cell motility by altering levels of c-di-GMP (PubMed:20303158). {ECO:0000269|PubMed:20303158, ECO:0000269|PubMed:27507823}. DgcN is a diguanylate cyclase (DGC) that dynamically relocates to the division site in response to envelope stress. DgcN localizes to the Z ring in an FtsZ- and ZipA-dependent manner in the presence of high levels of c-di-GMP. G7354-MONOMER YfiR counteracts relocation of DgcN to the Z ring . During growth on gluconeogenic carbon sources (glycerol, mannitol, sorbitol) DgcN activity depletes cellular GTP and promotes growth arrest - this function of DgcN is also associated with an increased tolerance to various antibiotics DgcN is an inner membrane protein with two predicted transmembrane domains. The C terminus is located in the cytoplasm . DgcN contains an N-terminal CHASE (cyclases/histidine kinases associated sensory) domain...

## Biological Role

Catalyzes RXN0-5359 (reaction.ecocyc.RXN0-5359).

## Annotation

FUNCTION: Bifunctional protein that catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) in response to reductive stress and then dynamically relocates to the division site to arrest cell division in response to envelope stress. In the presence of high intracellular c-di-GMP levels, and in response to envelope stress, interacts with cell division proteins and halts cell division, without disassembling the Z ring, but by blocking its further progress toward cytokinesis (PubMed:27507823). Part of a network that regulates cell motility by altering levels of c-di-GMP (PubMed:20303158). {ECO:0000269|PubMed:20303158, ECO:0000269|PubMed:27507823}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2604|gene.b2604]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46139`
- `KEGG:ecj:JW2585;eco:b2604;`
- `GeneID:75205865;947091;`
- `GO:GO:0005525; GO:0005886; GO:0007165; GO:0032153; GO:0036460; GO:0042802; GO:0043709; GO:0046872; GO:0052621; GO:1902201`
- `EC:2.7.7.65`

## Notes

Diguanylate cyclase DgcN (DGC) (EC 2.7.7.65)
