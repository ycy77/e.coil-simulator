---
entity_id: "protein.P0ACB0"
entity_type: "protein"
name: "dnaB"
source_database: "UniProt"
source_id: "P0ACB0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dnaB groP grpA b4052 JW4012"
---

# dnaB

`protein.P0ACB0`

## Static

- Type: `protein`
- Source: `UniProt:P0ACB0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The main replicative DNA helicase, it participates in initiation and elongation during chromosome replication. Travels ahead of the DNA replisome, separating dsDNA into templates for DNA synthesis. A processive ATP-dependent 5'-3' DNA helicase that acts on preformed replication forks (have single-stranded (ss)DNA tails) (PubMed:3007474). ATP is the best nucleotide for helicase activity; GTP, CTP, dCTP and dATP are poor substitutes (PubMed:3007474). Participates with DNA primase DnaG in primer RNA (pRNA) synthesis during initiation of DNA replication (PubMed:7532169). Has DNA-dependent ATPase activity (PubMed:7532169). Is loaded onto ssDNA via the action of DnaC; ssDNA binds to the central pore in the DnaB(6):DnaC(6) complex, making contacts with both subunits (PubMed:30797687). Required for restart of stalled replication forks, which reloads the DnaB replicative helicase on sites other than the origin of replication (PubMed:6454139, PubMed:8663104, PubMed:8663105). {ECO:0000269|PubMed:3007474, ECO:0000269|PubMed:30797687, ECO:0000269|PubMed:7532169}.; FUNCTION: Deletion or mutations in this gene were selected in directed evolution experiments for resistance to intense ionizing radiation (3000 Gy) (PubMed:24596148). {ECO:0000269|PubMed:24596148}.

## Biological Role

Component of replisome (complex.ecocyc.CPLX0-13320), replicative DNA helicase (complex.ecocyc.CPLX0-3621), DNA replication restart primosome (complex.ecocyc.CPLX0-3922).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)

## Annotation

FUNCTION: The main replicative DNA helicase, it participates in initiation and elongation during chromosome replication. Travels ahead of the DNA replisome, separating dsDNA into templates for DNA synthesis. A processive ATP-dependent 5'-3' DNA helicase that acts on preformed replication forks (have single-stranded (ss)DNA tails) (PubMed:3007474). ATP is the best nucleotide for helicase activity; GTP, CTP, dCTP and dATP are poor substitutes (PubMed:3007474). Participates with DNA primase DnaG in primer RNA (pRNA) synthesis during initiation of DNA replication (PubMed:7532169). Has DNA-dependent ATPase activity (PubMed:7532169). Is loaded onto ssDNA via the action of DnaC; ssDNA binds to the central pore in the DnaB(6):DnaC(6) complex, making contacts with both subunits (PubMed:30797687). Required for restart of stalled replication forks, which reloads the DnaB replicative helicase on sites other than the origin of replication (PubMed:6454139, PubMed:8663104, PubMed:8663105). {ECO:0000269|PubMed:3007474, ECO:0000269|PubMed:30797687, ECO:0000269|PubMed:7532169}.; FUNCTION: Deletion or mutations in this gene were selected in directed evolution experiments for resistance to intense ionizing radiation (3000 Gy) (PubMed:24596148). {ECO:0000269|PubMed:24596148}.

## Pathways

- `eco03030` DNA replication (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CPLX0-3621|complex.ecocyc.CPLX0-3621]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CPLX0-3922|complex.ecocyc.CPLX0-3922]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b4052|gene.b4052]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACB0`
- `KEGG:ecj:JW4012;eco:b4052;ecoc:C3026_21895;`
- `GeneID:93777780;948555;`
- `GO:GO:0003677; GO:0003678; GO:0004386; GO:0005524; GO:0005829; GO:0006260; GO:0006269; GO:0006270; GO:0010212; GO:0016887; GO:0030894; GO:0031297; GO:0033202; GO:0042802; GO:0043139; GO:1990077; GO:1990100; GO:1990156; GO:1990158; GO:1990159; GO:1990160`
- `EC:5.6.2.3`

## Notes

Replicative DNA helicase DnaB (EC 5.6.2.3) (DNA 5'-3' helicase DnaB)
