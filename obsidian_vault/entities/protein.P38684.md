---
entity_id: "protein.P38684"
entity_type: "protein"
name: "torR"
source_database: "UniProt"
source_id: "P38684"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "torR b0995 JW0980"
---

# torR

`protein.P38684`

## Static

- Type: `protein`
- Source: `UniProt:P38684`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system TorS/TorR involved in the anaerobic utilization of trimethylamine-N-oxide (TMAO). Phosphorylated TorR activates the transcription of the torCAD operon by binding to four decameric boxes located in the torCAD promoter. Box1, 2 and 4 contain the DNA sequence 5'-CTGTTCATAT-3' and box3 contains the DNA sequence 5'-CCGTTCATCC-3'. Phosphorylated as well as unphosphorylated TorR negatively regulates its own expression by binding to box1 and 2. A knockout mutant of this gene was sensitive to boric acid exposure compared to most other gene knockouts; a complementation assay restored its intrinsic boric acid resistance .

## Biological Role

Component of TorR-TorI (complex.ecocyc.CPLX0-2821), DNA-binding transcriptional dual regulator TorR (complex.ecocyc.TORR-CPLX), DNA-binding transcriptional dual regulator TorR-phosphorylated (protein.ecocyc.PHOSPHO-TORR).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system TorS/TorR involved in the anaerobic utilization of trimethylamine-N-oxide (TMAO). Phosphorylated TorR activates the transcription of the torCAD operon by binding to four decameric boxes located in the torCAD promoter. Box1, 2 and 4 contain the DNA sequence 5'-CTGTTCATAT-3' and box3 contains the DNA sequence 5'-CCGTTCATCC-3'. Phosphorylated as well as unphosphorylated TorR negatively regulates its own expression by binding to box1 and 2.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (11)

- `activates` --> [[gene.b0996|gene.b0996]] `RegulonDB` `C` - regulator=TorR; target=torC; function=+
- `activates` --> [[gene.b0997|gene.b0997]] `RegulonDB` `S` - regulator=TorR; target=torA; function=+
- `activates` --> [[gene.b0998|gene.b0998]] `RegulonDB` `S` - regulator=TorR; target=torD; function=+
- `activates` --> [[gene.b2741|gene.b2741]] `RegulonDB` `C` - regulator=TorR; target=rpoS; function=+
- `activates` --> [[gene.b3707|gene.b3707]] `RegulonDB` `S` - regulator=TorR; target=tnaC; function=+
- `activates` --> [[gene.b3708|gene.b3708]] `RegulonDB` `S` - regulator=TorR; target=tnaA; function=+
- `activates` --> [[gene.b3709|gene.b3709]] `RegulonDB` `S` - regulator=TorR; target=tnaB; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-2821|complex.ecocyc.CPLX0-2821]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TORR-CPLX|complex.ecocyc.TORR-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0995|gene.b0995]] `RegulonDB` `C` - regulator=TorR; target=torR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0995|gene.b0995]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P38684`
- `KEGG:ecj:JW0980;eco:b0995;ecoc:C3026_06065;`
- `GeneID:946182;`
- `GO:GO:0000156; GO:0000976; GO:0005829; GO:0006355; GO:0032993; GO:0097532`

## Notes

TorCAD operon transcriptional regulatory protein TorR
