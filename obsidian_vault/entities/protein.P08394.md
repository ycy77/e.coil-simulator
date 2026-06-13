---
entity_id: "protein.P08394"
entity_type: "protein"
name: "recB"
source_database: "UniProt"
source_id: "P08394"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "recB ior rorA b2820 JW2788"
---

# recB

`protein.P08394`

## Static

- Type: `protein`
- Source: `UniProt:P08394`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A helicase/nuclease that prepares dsDNA breaks (DSB) for recombinational DNA repair. Binds to DSBs and unwinds DNA via a rapid (>1 kb/second) and highly processive (>30 kb) ATP-dependent bidirectional helicase. Unwinds dsDNA until it encounters a Chi (crossover hotspot instigator, 5'-GCTGGTGG-3') sequence from the 3' direction. Cuts ssDNA a few nucleotides 3' to Chi site, by nicking one strand or switching the strand degraded (depending on the reaction conditions). The properties and activities of the enzyme are changed at Chi. The Chi-altered holoenzyme produces a long 3'-ssDNA overhang which facilitates RecA-binding to the ssDNA for homologous DNA recombination and repair. Holoenzyme degrades any linearized DNA that is unable to undergo homologous recombination (PubMed:123277, PubMed:4552016, PubMed:4562392). In the holoenzyme this subunit contributes ATPase, 3'-5' helicase, exonuclease activity and loads RecA onto ssDNA. The RecBC complex requires the RecD subunit for nuclease activity, but can translocate along ssDNA in both directions. The RecBCD complex does not unwind G-quadruplex DNA (PubMed:9765292). Probably interacts with a component of retron Ec48 which moniters RecBCD stability; when RecB is missing or impaired the retron is activated and becomes toxic (Probable) (PubMed:33157039)...

## Biological Role

Catalyzes RXN-11135 (reaction.ecocyc.RXN-11135). Component of exodeoxyribonuclease V (complex.ecocyc.RECBCD).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: A helicase/nuclease that prepares dsDNA breaks (DSB) for recombinational DNA repair. Binds to DSBs and unwinds DNA via a rapid (>1 kb/second) and highly processive (>30 kb) ATP-dependent bidirectional helicase. Unwinds dsDNA until it encounters a Chi (crossover hotspot instigator, 5'-GCTGGTGG-3') sequence from the 3' direction. Cuts ssDNA a few nucleotides 3' to Chi site, by nicking one strand or switching the strand degraded (depending on the reaction conditions). The properties and activities of the enzyme are changed at Chi. The Chi-altered holoenzyme produces a long 3'-ssDNA overhang which facilitates RecA-binding to the ssDNA for homologous DNA recombination and repair. Holoenzyme degrades any linearized DNA that is unable to undergo homologous recombination (PubMed:123277, PubMed:4552016, PubMed:4562392). In the holoenzyme this subunit contributes ATPase, 3'-5' helicase, exonuclease activity and loads RecA onto ssDNA. The RecBC complex requires the RecD subunit for nuclease activity, but can translocate along ssDNA in both directions. The RecBCD complex does not unwind G-quadruplex DNA (PubMed:9765292). Probably interacts with a component of retron Ec48 which moniters RecBCD stability; when RecB is missing or impaired the retron is activated and becomes toxic (Probable) (PubMed:33157039). {ECO:0000269|PubMed:10197988, ECO:0000269|PubMed:10518611, ECO:0000269|PubMed:10766864, ECO:0000269|PubMed:123277, ECO:0000269|PubMed:12815437, ECO:0000269|PubMed:12815438, ECO:0000269|PubMed:1535156, ECO:0000269|PubMed:16041061, ECO:0000269|PubMed:1618858, ECO:0000269|PubMed:16388588, ECO:0000269|PubMed:18079176, ECO:0000269|PubMed:20852646, ECO:0000269|PubMed:23851395, ECO:0000269|PubMed:25073102, ECO:0000269|PubMed:4268693, ECO:0000269|PubMed:4552016, ECO:0000269|PubMed:4562392, ECO:0000269|PubMed:7608206, ECO:0000269|PubMed:9192629, ECO:0000269|PubMed:9230304, ECO:0000269|PubMed:9448271, ECO:0000269|PubMed:9765292, ECO:0000269|PubMed:9790841, ECO:0000305|PubMed:33157039}.

## Pathways

- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-11135|reaction.ecocyc.RXN-11135]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.RECBCD|complex.ecocyc.RECBCD]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2820|gene.b2820]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08394`
- `KEGG:ecj:JW2788;eco:b2820;ecoc:C3026_15485;`
- `GeneID:947286;`
- `GO:GO:0000287; GO:0000724; GO:0000725; GO:0003677; GO:0003678; GO:0004520; GO:0005524; GO:0005829; GO:0006310; GO:0008094; GO:0008854; GO:0009314; GO:0009338; GO:0015616; GO:0016887; GO:0043138; GO:0044355`
- `EC:3.1.11.5; 5.6.2.4`

## Notes

RecBCD enzyme subunit RecB (EC 3.1.11.5) (EC 5.6.2.4) (DNA 3'-5' helicase subunit RecB) (Exodeoxyribonuclease V 135 kDa polypeptide) (Exodeoxyribonuclease V beta chain) (Exonuclease V subunit RecB) (ExoV subunit RecB) (Helicase/nuclease RecBCD subunit RecB)
