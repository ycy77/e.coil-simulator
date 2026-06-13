---
entity_id: "protein.P25736"
entity_type: "protein"
name: "endA"
source_database: "UniProt"
source_id: "P25736"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:4955462}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "endA b2945 JW2912"
---

# endA

`protein.P25736`

## Static

- Type: `protein`
- Source: `UniProt:P25736`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:4955462}.

## Enriched Summary

FUNCTION: Has double-strand break activity. Endonuclease I is a periplasmic enzyme that cleaves within duplex DNA. Its cellular role is unknown. Endonuclease I cleaves within duplex DNA, producing oligonucleotides that are on average 7 bp long and contain 5' phosphate groups . It is inhibited by tRNA and rRNA . Even though it was originally reported that mutants lacking endA show no apparent difference from wild type cells , several phenotypes were reported later. An endA deletion strain is sensitive to CPD0-1392 , and deletion of endA was found to facilitate plasmid isolation from E. coli strains . A UV-resistant mutant increased DNA polymerase I and endonuclease I activity . EndA: endonuclease I .

## Biological Role

Catalyzes 3.1.21.1-RXN (reaction.ecocyc.3.1.21.1-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Has double-strand break activity.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.1.21.1-RXN|reaction.ecocyc.3.1.21.1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2945|gene.b2945]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25736`
- `KEGG:ecj:JW2912;eco:b2945;ecoc:C3026_16120;`
- `GeneID:93779052;949092;`
- `GO:GO:0004519; GO:0004530; GO:0004536; GO:0006308; GO:0016888; GO:0042597`
- `EC:3.1.21.1`

## Notes

Endonuclease-1 (EC 3.1.21.1) (Endonuclease I) (Endo I)
