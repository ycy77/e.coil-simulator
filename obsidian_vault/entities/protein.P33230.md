---
entity_id: "protein.P33230"
entity_type: "protein"
name: "rcbA"
source_database: "UniProt"
source_id: "P33230"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rcbA ydaC b1347 JW1341"
---

# rcbA

`protein.P33230`

## Static

- Type: `protein`
- Source: `UniProt:P33230`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Helps to maintain the integrity of the chromosome by lowering the steady-state level of double strand breaks (PubMed:22343303). This region of DNA acts as an antitoxin to toxin RalR, a DNase, but it seems to be sRNA RalA that has the antitoxin activity and not this putative protein. Therefore the identity of this as a protein-coding gene has been cast into doubt (PubMed:24748661). {ECO:0000269|PubMed:22343303, ECO:0000269|PubMed:24748661}. An rcbA deletion mutant has an increased level of chromosomal double strand breaks (DSB) . Overexpression of rcbA from a plasmid suppresses the lethal effect caused by the induced expression of the chromosomal replication initiation protein, DnaA, in DSB repair-defective mutants . Overproduction of DnaA is toxic in an rcbA deletion mutant but not in the isogenic rcbA+ strain . The mechanism of action of RcbA is not clear. Overexpression of rcbA increases fitness as well as resistance to toxic compounds and antibiotics, including erythromycin . It is possible that the RcbA phenotype is due to the expression of G0-16600 RalA, a small RNA antitoxin encoded on the opposite strand . rcbA: reduces the frequency of chromosome breaks

## Annotation

FUNCTION: Helps to maintain the integrity of the chromosome by lowering the steady-state level of double strand breaks (PubMed:22343303). This region of DNA acts as an antitoxin to toxin RalR, a DNase, but it seems to be sRNA RalA that has the antitoxin activity and not this putative protein. Therefore the identity of this as a protein-coding gene has been cast into doubt (PubMed:24748661). {ECO:0000269|PubMed:22343303, ECO:0000269|PubMed:24748661}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1347|gene.b1347]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33230`
- `KEGG:ecj:JW1341;eco:b1347;ecoc:C3026_07890;`
- `GeneID:947504;`
- `GO:GO:0006259; GO:0046677`

## Notes

Double-strand break reduction protein
