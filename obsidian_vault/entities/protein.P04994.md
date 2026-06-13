---
entity_id: "protein.P04994"
entity_type: "protein"
name: "xseA"
source_database: "UniProt"
source_id: "P04994"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:6284744}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xseA b2509 JW2493"
---

# xseA

`protein.P04994`

## Static

- Type: `protein`
- Source: `UniProt:P04994`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:6284744}.

## Enriched Summary

FUNCTION: Bidirectionally degrades single-stranded DNA into large acid-insoluble oligonucleotides, which are then degraded further into small acid-soluble oligonucleotides. It can degrade 3' or 5' ss regions extending from the termini of duplex DNA molecules and displaced ss regions. It can also excise thymine dimers in vitro (Probable) (PubMed:22718974, PubMed:4602029, PubMed:4602030). ssDNA-binding requires both subunits (PubMed:22718974). Required for production of the mature 5'-end of retron Ec78 or Ec83 msDNA. Overproduction of this subunit in the absence of an equivalent quantity of the small subunit is toxic, causing cell elongation and chromosome fragmentation or loss; its toxicity is mostly suppressed by RecA (PubMed:26626352). {ECO:0000269|PubMed:22718974, ECO:0000269|PubMed:26626352, ECO:0000269|PubMed:4602029, ECO:0000269|PubMed:4602030, ECO:0000305|PubMed:6284744}. XseA is the large subunit of exonuclease VII (ExoVII) - a single-strand DNA exonuclease implicated in various aspects of DNA repair.

## Biological Role

Component of exodeoxyribonuclease VII (complex.ecocyc.CPLX-3946).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

FUNCTION: Bidirectionally degrades single-stranded DNA into large acid-insoluble oligonucleotides, which are then degraded further into small acid-soluble oligonucleotides. It can degrade 3' or 5' ss regions extending from the termini of duplex DNA molecules and displaced ss regions. It can also excise thymine dimers in vitro (Probable) (PubMed:22718974, PubMed:4602029, PubMed:4602030). ssDNA-binding requires both subunits (PubMed:22718974). Required for production of the mature 5'-end of retron Ec78 or Ec83 msDNA. Overproduction of this subunit in the absence of an equivalent quantity of the small subunit is toxic, causing cell elongation and chromosome fragmentation or loss; its toxicity is mostly suppressed by RecA (PubMed:26626352). {ECO:0000269|PubMed:22718974, ECO:0000269|PubMed:26626352, ECO:0000269|PubMed:4602029, ECO:0000269|PubMed:4602030, ECO:0000305|PubMed:6284744}.

## Pathways

- `eco03430` Mismatch repair (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-3946|complex.ecocyc.CPLX-3946]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2509|gene.b2509]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04994`
- `KEGG:ecj:JW2493;eco:b2509;ecoc:C3026_13915;`
- `GeneID:946988;`
- `GO:GO:0003677; GO:0005737; GO:0006298; GO:0006308; GO:0008855; GO:0009318`
- `EC:3.1.11.6`

## Notes

Exodeoxyribonuclease 7 large subunit (EC 3.1.11.6) (Exodeoxyribonuclease VII large subunit) (ExoVII large subunit) (Exonuclease VII large subunit)
