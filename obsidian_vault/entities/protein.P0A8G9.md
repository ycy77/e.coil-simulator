---
entity_id: "protein.P0A8G9"
entity_type: "protein"
name: "xseB"
source_database: "UniProt"
source_id: "P0A8G9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00337, ECO:0000305|PubMed:6284744}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xseB yajE b0422 JW0412"
---

# xseB

`protein.P0A8G9`

## Static

- Type: `protein`
- Source: `UniProt:P0A8G9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00337, ECO:0000305|PubMed:6284744}.

## Enriched Summary

FUNCTION: Bidirectionally degrades single-stranded DNA into large acid-insoluble oligonucleotides, which are then degraded further into small acid-soluble oligonucleotides. It can degrade 3' or 5' ss regions extending from the termini of duplex DNA molecules and displaced ss regions. It can also excise thymine dimers in vitro (Probable) (PubMed:22718974, PubMed:4602029, PubMed:4602030). Required for production of the mature 5'-end of retron Ec78 or Ec83 msDNA. When in excess of the large subunit, counteracts the large subunit's toxicity (PubMed:26626352). {ECO:0000269|PubMed:22718974, ECO:0000269|PubMed:26626352, ECO:0000269|PubMed:4602029, ECO:0000269|PubMed:4602030, ECO:0000305|PubMed:6284744}. XseB is the small subunit of exonuclease VII (ExoVII) - a single-strand DNA exonuclease implicated in various aspects of DNA repair.

## Biological Role

Component of exodeoxyribonuclease VII (complex.ecocyc.CPLX-3946).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

FUNCTION: Bidirectionally degrades single-stranded DNA into large acid-insoluble oligonucleotides, which are then degraded further into small acid-soluble oligonucleotides. It can degrade 3' or 5' ss regions extending from the termini of duplex DNA molecules and displaced ss regions. It can also excise thymine dimers in vitro (Probable) (PubMed:22718974, PubMed:4602029, PubMed:4602030). Required for production of the mature 5'-end of retron Ec78 or Ec83 msDNA. When in excess of the large subunit, counteracts the large subunit's toxicity (PubMed:26626352). {ECO:0000269|PubMed:22718974, ECO:0000269|PubMed:26626352, ECO:0000269|PubMed:4602029, ECO:0000269|PubMed:4602030, ECO:0000305|PubMed:6284744}.

## Pathways

- `eco03430` Mismatch repair (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-3946|complex.ecocyc.CPLX-3946]] `EcoCyc` `database` - EcoCyc component coefficient=24 | EcoCyc protcplxs.col coefficient=24

## Incoming Edges (1)

- `encodes` <-- [[gene.b0422|gene.b0422]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8G9`
- `KEGG:ecj:JW0412;eco:b0422;ecoc:C3026_02060;`
- `GeneID:75170440;75202844;945069;`
- `GO:GO:0005829; GO:0006298; GO:0006308; GO:0008855; GO:0009318`
- `EC:3.1.11.6`

## Notes

Exodeoxyribonuclease 7 small subunit (EC 3.1.11.6) (Exodeoxyribonuclease VII small subunit) (ExoVII small subunit) (Exonuclease VII small subunit)
