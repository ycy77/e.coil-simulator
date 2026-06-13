---
entity_id: "protein.P15032"
entity_type: "protein"
name: "recE"
source_database: "UniProt"
source_id: "P15032"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "recE b1350 JW1344"
---

# recE

`protein.P15032`

## Static

- Type: `protein`
- Source: `UniProt:P15032`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Is involved in the RecE pathway of recombination. Catalyzes the degradation of double-stranded DNA. Acts progressively in a 5' to 3' direction, releasing 5'-phosphomononucleotides. Has a strong preference for linear duplex substrate DNA and appears to be unable to initiate degradation from single-stranded breaks in DNA. DNA damage can occur due to a variety of environmental assaults including UV irradiation and chemical agents. Escherichia coli has a number of complex enzymatic pathways for the repair of DNA damage. Most DNA damage involves lesions to one strand of DNA, but in some cases damage can occur to both strands. Double strand breaks (DSBs) cannot be repaired via excision repair pathways because by their nature they lack an intact strand to be used as a template. Repair of DSBs utilize the RecA pathway of homologous recombination with a separate, intact, homologous region of DNA. The RecE (also known as exonuclease VIII) pathway is an alternative pathway for the initiation of homologous recombination in Escherichia coli. The RecE pathway is activated in recB, recC sbcA (suppressors of recB and recC) mutants. Activation of the RecE pathway results in the production of at least two phage proteins relevant for recombinational repair...

## Biological Role

Catalyzes RXN0-5039 (reaction.ecocyc.RXN0-5039).

## Annotation

FUNCTION: Is involved in the RecE pathway of recombination. Catalyzes the degradation of double-stranded DNA. Acts progressively in a 5' to 3' direction, releasing 5'-phosphomononucleotides. Has a strong preference for linear duplex substrate DNA and appears to be unable to initiate degradation from single-stranded breaks in DNA.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5039|reaction.ecocyc.RXN0-5039]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1350|gene.b1350]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15032`
- `KEGG:ecj:JW1344;eco:b1350;ecoc:C3026_07905;`
- `GeneID:945918;`
- `GO:GO:0042802; GO:0051908`
- `EC:3.1.11.-`

## Notes

Exodeoxyribonuclease 8 (EC 3.1.11.-) (Exodeoxyribonuclease VIII) (EXO VIII)
