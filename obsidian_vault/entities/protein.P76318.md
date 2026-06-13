---
entity_id: "protein.P76318"
entity_type: "protein"
name: "yedK"
source_database: "UniProt"
source_id: "P76318"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yedK yedG b1931 JW1916"
---

# yedK

`protein.P76318`

## Static

- Type: `protein`
- Source: `UniProt:P76318`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Sensor of abasic sites in single-stranded DNA (ssDNA) required to preserve genome integrity by promoting error-free repair of abasic sites (PubMed:30554877). Recognizes and binds abasic sites in ssDNA at replication forks and chemically modifies the lesion by forming a covalent cross-link with DNA: forms a stable thiazolidine linkage between a ring-opened abasic site and the alpha-amino and sulfhydryl substituents of its N-terminal catalytic cysteine residue (PubMed:30554877, PubMed:31235915, PubMed:31504793). The DNA-protein cross-link is then reversed: able to catalyze the reversal of the thiazolidine cross-link and cycle between a cross-link and a non-cross-linked state depending on DNA context: mediates self-reversal of the thiazolidine cross-link in double stranded DNA (PubMed:35934051, PubMed:37519246). May act as a protease: mediates autocatalytic processing of its N-terminal methionine in order to expose the catalytic cysteine (By similarity). {ECO:0000250|UniProtKB:Q8R1M0, ECO:0000269|PubMed:30554877, ECO:0000269|PubMed:31235915, ECO:0000269|PubMed:31504793, ECO:0000269|PubMed:35934051, ECO:0000269|PubMed:37519246}...

## Biological Role

Catalyzes RXN-21016 (reaction.ecocyc.RXN-21016).

## Annotation

FUNCTION: Sensor of abasic sites in single-stranded DNA (ssDNA) required to preserve genome integrity by promoting error-free repair of abasic sites (PubMed:30554877). Recognizes and binds abasic sites in ssDNA at replication forks and chemically modifies the lesion by forming a covalent cross-link with DNA: forms a stable thiazolidine linkage between a ring-opened abasic site and the alpha-amino and sulfhydryl substituents of its N-terminal catalytic cysteine residue (PubMed:30554877, PubMed:31235915, PubMed:31504793). The DNA-protein cross-link is then reversed: able to catalyze the reversal of the thiazolidine cross-link and cycle between a cross-link and a non-cross-linked state depending on DNA context: mediates self-reversal of the thiazolidine cross-link in double stranded DNA (PubMed:35934051, PubMed:37519246). May act as a protease: mediates autocatalytic processing of its N-terminal methionine in order to expose the catalytic cysteine (By similarity). {ECO:0000250|UniProtKB:Q8R1M0, ECO:0000269|PubMed:30554877, ECO:0000269|PubMed:31235915, ECO:0000269|PubMed:31504793, ECO:0000269|PubMed:35934051, ECO:0000269|PubMed:37519246}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-21016|reaction.ecocyc.RXN-21016]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1931|gene.b1931]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76318`
- `KEGG:ecj:JW1916;eco:b1931;ecoc:C3026_10950;`
- `GeneID:946435;`
- `GO:GO:0003697; GO:0006508; GO:0006974; GO:0008233; GO:0009432; GO:0106300; GO:0160129`
- `EC:3.4.-.-; 4.-.-.-`

## Notes

Abasic site processing protein YedK (EC 4.-.-.-) (Peptidase YedK) (EC 3.4.-.-)
