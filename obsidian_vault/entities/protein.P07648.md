---
entity_id: "protein.P07648"
entity_type: "protein"
name: "recC"
source_database: "UniProt"
source_id: "P07648"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "recC b2822 JW2790"
---

# recC

`protein.P07648`

## Static

- Type: `protein`
- Source: `UniProt:P07648`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A helicase/nuclease that prepares dsDNA breaks (DSB) for recombinational DNA repair. Binds to DSBs and unwinds DNA via a rapid (>1 kb/second) and highly processive (>30 kb) ATP-dependent bidirectional helicase. Unwinds dsDNA until it encounters a Chi (crossover hotspot instigator, 5'-GCTGGTGG-3') sequence from the 3' direction. Cuts ssDNA a few nucleotides 3' to Chi site, by nicking one strand or switching the strand degraded (depending on the reaction conditions). The properties and activities of the enzyme are changed at Chi. The Chi-altered holoenzyme produces a long 3'-ssDNA overhang which facilitates RecA-binding to the ssDNA for homologous DNA recombination and repair. Holoenzyme degrades any linearized DNA that is unable to undergo homologous recombination (PubMed:123277, PubMed:4552016, PubMed:4562392). In the holoenzyme this subunit almost certainly recognizes the wild-type Chi sequence, when added to isolated RecB increases its ATP-dependent helicase processivity. The RecBC complex requires the RecD subunit for nuclease activity, but can translocate along ssDNA in both directions. The RecBCD complex does not unwind G-quadruplex DNA (PubMed:9765292)...

## Biological Role

Component of exodeoxyribonuclease V (complex.ecocyc.RECBCD).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: A helicase/nuclease that prepares dsDNA breaks (DSB) for recombinational DNA repair. Binds to DSBs and unwinds DNA via a rapid (>1 kb/second) and highly processive (>30 kb) ATP-dependent bidirectional helicase. Unwinds dsDNA until it encounters a Chi (crossover hotspot instigator, 5'-GCTGGTGG-3') sequence from the 3' direction. Cuts ssDNA a few nucleotides 3' to Chi site, by nicking one strand or switching the strand degraded (depending on the reaction conditions). The properties and activities of the enzyme are changed at Chi. The Chi-altered holoenzyme produces a long 3'-ssDNA overhang which facilitates RecA-binding to the ssDNA for homologous DNA recombination and repair. Holoenzyme degrades any linearized DNA that is unable to undergo homologous recombination (PubMed:123277, PubMed:4552016, PubMed:4562392). In the holoenzyme this subunit almost certainly recognizes the wild-type Chi sequence, when added to isolated RecB increases its ATP-dependent helicase processivity. The RecBC complex requires the RecD subunit for nuclease activity, but can translocate along ssDNA in both directions. The RecBCD complex does not unwind G-quadruplex DNA (PubMed:9765292). {ECO:0000269|PubMed:10197988, ECO:0000269|PubMed:10884344, ECO:0000269|PubMed:123277, ECO:0000269|PubMed:12815437, ECO:0000269|PubMed:12815438, ECO:0000269|PubMed:1535156, ECO:0000269|PubMed:16041061, ECO:0000269|PubMed:1618858, ECO:0000269|PubMed:20852646, ECO:0000269|PubMed:23851395, ECO:0000269|PubMed:4268693, ECO:0000269|PubMed:4552016, ECO:0000269|PubMed:4562392, ECO:0000269|PubMed:7608206, ECO:0000269|PubMed:9192629, ECO:0000269|PubMed:9230304, ECO:0000269|PubMed:9448271, ECO:0000269|PubMed:9765292, ECO:0000269|PubMed:9790841}.

## Pathways

- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.RECBCD|complex.ecocyc.RECBCD]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2822|gene.b2822]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07648`
- `KEGG:ecj:JW2790;eco:b2822;ecoc:C3026_15495;`
- `GeneID:75203786;947294;`
- `GO:GO:0000724; GO:0000725; GO:0003677; GO:0003678; GO:0005524; GO:0006310; GO:0008854; GO:0009314; GO:0009338; GO:0044355`

## Notes

RecBCD enzyme subunit RecC (Exodeoxyribonuclease V 125 kDa polypeptide) (Exodeoxyribonuclease V gamma chain) (Exonuclease V subunit RecC) (ExoV subunit RecC) (Helicase/nuclease RecBCD subunit RecC)
