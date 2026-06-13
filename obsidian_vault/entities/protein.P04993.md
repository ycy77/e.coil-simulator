---
entity_id: "protein.P04993"
entity_type: "protein"
name: "recD"
source_database: "UniProt"
source_id: "P04993"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "recD hopE b2819 JW2787"
---

# recD

`protein.P04993`

## Static

- Type: `protein`
- Source: `UniProt:P04993`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A helicase/nuclease that prepares dsDNA breaks (DSB) for recombinational DNA repair. Binds to DSBs and unwinds DNA via a rapid (>1 kb/second) and highly processive (>30 kb) ATP-dependent bidirectional helicase. Unwinds dsDNA until it encounters a Chi (crossover hotspot instigator, 5'-GCTGGTGG-3') sequence from the 3' direction. Cuts ssDNA a few nucleotides 3' to Chi site, by nicking one strand or switching the strand degraded (depending on the reaction conditions). The properties and activities of the enzyme are changed at Chi. The Chi-altered holoenzyme produces a long 3'-ssDNA overhang which facilitates RecA-binding to the ssDNA for homologous DNA recombination and repair. In the holoenzyme this subunit contributes ssDNA-dependent ATPase and fast 5'-3' helicase activity. When added to pre-assembled RecBC greatly stimulates nuclease activity and augments holoenzyme processivity. Negatively regulates the RecA-loading ability of RecBCD. The RecBCD complex does not unwind G-quadruplex DNA (PubMed:9765292)...

## Biological Role

Catalyzes RXN0-4261 (reaction.ecocyc.RXN0-4261). Component of exodeoxyribonuclease V (complex.ecocyc.RECBCD).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: A helicase/nuclease that prepares dsDNA breaks (DSB) for recombinational DNA repair. Binds to DSBs and unwinds DNA via a rapid (>1 kb/second) and highly processive (>30 kb) ATP-dependent bidirectional helicase. Unwinds dsDNA until it encounters a Chi (crossover hotspot instigator, 5'-GCTGGTGG-3') sequence from the 3' direction. Cuts ssDNA a few nucleotides 3' to Chi site, by nicking one strand or switching the strand degraded (depending on the reaction conditions). The properties and activities of the enzyme are changed at Chi. The Chi-altered holoenzyme produces a long 3'-ssDNA overhang which facilitates RecA-binding to the ssDNA for homologous DNA recombination and repair. In the holoenzyme this subunit contributes ssDNA-dependent ATPase and fast 5'-3' helicase activity. When added to pre-assembled RecBC greatly stimulates nuclease activity and augments holoenzyme processivity. Negatively regulates the RecA-loading ability of RecBCD. The RecBCD complex does not unwind G-quadruplex DNA (PubMed:9765292). {ECO:0000269|PubMed:10197988, ECO:0000269|PubMed:10840065, ECO:0000269|PubMed:12815437, ECO:0000269|PubMed:12815438, ECO:0000269|PubMed:1535156, ECO:0000269|PubMed:16041061, ECO:0000269|PubMed:1618858, ECO:0000269|PubMed:18079176, ECO:0000269|PubMed:23851395, ECO:0000269|PubMed:7608206, ECO:0000269|PubMed:9192629, ECO:0000269|PubMed:9230304, ECO:0000269|PubMed:9448271, ECO:0000269|PubMed:9765292, ECO:0000269|PubMed:9790841}.

## Pathways

- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4261|reaction.ecocyc.RXN0-4261]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.RECBCD|complex.ecocyc.RECBCD]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2819|gene.b2819]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04993`
- `KEGG:ecj:JW2787;eco:b2819;ecoc:C3026_15480;`
- `GeneID:75203789;947287;`
- `GO:GO:0000724; GO:0000725; GO:0003677; GO:0004386; GO:0005524; GO:0006310; GO:0006974; GO:0008854; GO:0009338; GO:0016887; GO:0017116; GO:0043139`
- `EC:5.6.2.3`

## Notes

RecBCD enzyme subunit RecD (EC 5.6.2.3) (DNA 5'-3' helicase subunit RecB) (Exodeoxyribonuclease V 67 kDa polypeptide) (Exodeoxyribonuclease V alpha chain) (Exonuclease V subunit RecD) (ExoV subunit RecD) (Helicase/nuclease RecBCD subunit RecD)
