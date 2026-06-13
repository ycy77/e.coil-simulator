---
entity_id: "protein.P09980"
entity_type: "protein"
name: "rep"
source_database: "UniProt"
source_id: "P09980"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rep b3778 JW5604"
---

# rep

`protein.P09980`

## Static

- Type: `protein`
- Source: `UniProt:P09980`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Rep helicase is a single-stranded (ss)DNA-dependent ATPase involved in DNA replication; it can initiate unwinding at a nick in the DNA. It binds to ssDNA and acts in a progressive fashion along the DNA in the 3' to 5' direction (PubMed:221901, PubMed:11428893, PubMed:17382604). Binds double-stranded (ds)DNA with a 5' ss- but not 3' ss-extension and forked structures with either lagging or leading ssDNA (PubMed:17382604). Part of the PriC-Rep pathway for restart of stalled replication forks, which reloads the DnaB replicative helicase on sites other than the origin of replication (PubMed:10835375). {ECO:0000255|HAMAP-Rule:MF_01920, ECO:0000269|PubMed:10835375, ECO:0000269|PubMed:11428893, ECO:0000269|PubMed:17382604, ECO:0000269|PubMed:221901}.

## Biological Role

Component of ATP-dependent DNA helicase Rep (complex.ecocyc.CPLX0-3931).

## Annotation

FUNCTION: Rep helicase is a single-stranded (ss)DNA-dependent ATPase involved in DNA replication; it can initiate unwinding at a nick in the DNA. It binds to ssDNA and acts in a progressive fashion along the DNA in the 3' to 5' direction (PubMed:221901, PubMed:11428893, PubMed:17382604). Binds double-stranded (ds)DNA with a 5' ss- but not 3' ss-extension and forked structures with either lagging or leading ssDNA (PubMed:17382604). Part of the PriC-Rep pathway for restart of stalled replication forks, which reloads the DnaB replicative helicase on sites other than the origin of replication (PubMed:10835375). {ECO:0000255|HAMAP-Rule:MF_01920, ECO:0000269|PubMed:10835375, ECO:0000269|PubMed:11428893, ECO:0000269|PubMed:17382604, ECO:0000269|PubMed:221901}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3931|complex.ecocyc.CPLX0-3931]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3778|gene.b3778]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09980`
- `KEGG:ecj:JW5604;eco:b3778;ecoc:C3026_20455;`
- `GeneID:948292;`
- `GO:GO:0000725; GO:0003678; GO:0003697; GO:0005524; GO:0005829; GO:0006260; GO:0006269; GO:0009314; GO:0016887; GO:0031297; GO:0042803; GO:0043138; GO:0043600; GO:0044787; GO:1990077; GO:1990160`
- `EC:5.6.2.4`

## Notes

ATP-dependent DNA helicase Rep (EC 5.6.2.4) (DNA 3'-5' helicase Rep)
