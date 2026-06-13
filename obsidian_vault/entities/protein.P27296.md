---
entity_id: "protein.P27296"
entity_type: "protein"
name: "dinG"
source_database: "UniProt"
source_id: "P27296"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dinG rarB b0799 JW0784"
---

# dinG

`protein.P27296`

## Static

- Type: `protein`
- Source: `UniProt:P27296`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: DNA-dependent ATPase and 5'-3' DNA helicase (PubMed:12748189, PubMed:17416902, PubMed:25059658, PubMed:37537265). Can also unwind DNA:RNA hybrid duplexes (PubMed:17416902). Is active on D-loops, R-loops, and on forked structures (PubMed:17416902, PubMed:37537265). Unwinds G-quadruplex DNA in a 5'-3' direction; unwinding efficiency differs on different substrates (PubMed:25059658, PubMed:37537265). Does not appear to unwind replication forks or Holliday junctions (PubMed:25059658). Translocates on single-stranded (ss)DNA with a 5'-3' polarity (PubMed:25059658). In vitro at high concentrations also unwinds in a 3'-5' direction (PubMed:25059658). May be involved in recombinational DNA repair and the resumption of replication after DNA damage (PubMed:17416902). The [4Fe-4S] cluster is redox active at cellular potentials and is involved in DNA-mediated charge-transport signaling between DNA repair proteins from distinct pathways (PubMed:24738733). DinG cooperates at long-range with endonuclease III, a base excision repair enzyme, using DNA charge transport to redistribute to regions of DNA damage (PubMed:24738733). Binds 10-11 nucleotides of ssDNA in a positively-charged groove across the helicase domains (PubMed:30520735)...

## Biological Role

Catalyzes RXN0-4261 (reaction.ecocyc.RXN0-4261). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

FUNCTION: DNA-dependent ATPase and 5'-3' DNA helicase (PubMed:12748189, PubMed:17416902, PubMed:25059658, PubMed:37537265). Can also unwind DNA:RNA hybrid duplexes (PubMed:17416902). Is active on D-loops, R-loops, and on forked structures (PubMed:17416902, PubMed:37537265). Unwinds G-quadruplex DNA in a 5'-3' direction; unwinding efficiency differs on different substrates (PubMed:25059658, PubMed:37537265). Does not appear to unwind replication forks or Holliday junctions (PubMed:25059658). Translocates on single-stranded (ss)DNA with a 5'-3' polarity (PubMed:25059658). In vitro at high concentrations also unwinds in a 3'-5' direction (PubMed:25059658). May be involved in recombinational DNA repair and the resumption of replication after DNA damage (PubMed:17416902). The [4Fe-4S] cluster is redox active at cellular potentials and is involved in DNA-mediated charge-transport signaling between DNA repair proteins from distinct pathways (PubMed:24738733). DinG cooperates at long-range with endonuclease III, a base excision repair enzyme, using DNA charge transport to redistribute to regions of DNA damage (PubMed:24738733). Binds 10-11 nucleotides of ssDNA in a positively-charged groove across the helicase domains (PubMed:30520735). {ECO:0000269|PubMed:12748189, ECO:0000269|PubMed:17416902, ECO:0000269|PubMed:24738733, ECO:0000269|PubMed:25059658, ECO:0000269|PubMed:30520735, ECO:0000269|PubMed:37537265}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4261|reaction.ecocyc.RXN0-4261]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0799|gene.b0799]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27296`
- `KEGG:ecj:JW0784;eco:b0799;ecoc:C3026_05045;`
- `GeneID:945431;`
- `GO:GO:0003677; GO:0003678; GO:0005524; GO:0006281; GO:0009432; GO:0016887; GO:0033677; GO:0043139; GO:0046872; GO:0051539; GO:0140640`
- `EC:5.6.2.3`

## Notes

ATP-dependent DNA helicase DinG (EC 5.6.2.3) (DNA 5'-3' helicase DinG)
