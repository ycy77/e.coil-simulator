---
entity_id: "protein.P28903"
entity_type: "protein"
name: "nrdD"
source_database: "UniProt"
source_id: "P28903"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nrdD b4238 JW4197"
---

# nrdD

`protein.P28903`

## Static

- Type: `protein`
- Source: `UniProt:P28903`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of ribonucleotides into deoxyribonucleotides, which are required for DNA synthesis and repair (PubMed:1460049, PubMed:24827372, PubMed:7568012, PubMed:7929317, PubMed:8381402, PubMed:9305874). Can reduce each of the four common ribonucleoside triphosphates (PubMed:7929317). {ECO:0000269|PubMed:1460049, ECO:0000269|PubMed:24827372, ECO:0000269|PubMed:7568012, ECO:0000269|PubMed:7929317, ECO:0000269|PubMed:8381402, ECO:0000269|PubMed:9305874}. Ribonucleotide reductases (RNRs) catalyze the conversion of ribonucleotides into deoxyribonucleotides, which are required for DNA synthesis and repair. Nucleotide reduction involves a transient protein-based thiyl radical that abstracts a hydrogen atom from the 2'-position of the nucleotide. Three classes of RNR enzymes have been identified; they differ in the metallocofactor required for generating the thiyl radical. E. coli contains three RNRs, the class Ia RIBONUCLEOSIDE-DIP-REDUCTI-CPLX, the class Ib RIBONUCLEOSIDE-DIP-REDUCTII-CPLX, and the class III anaerobic ribonucleoside-triphosphate reductase (NrdD) described here. The existence of an RNR specifically active under anaerobic conditions was first shown by . The NrdD reductase is activated by a tightly associated activase enzyme (NrdG) under anaerobic conditions and is inactivated by oxygen...

## Biological Role

Component of oxidized ribonucleoside-triphosphate reductase (complex.ecocyc.MONOMER0-2863), anaerobic nucleoside-triphosphate reductase activating system (complex.ecocyc.NRDACTMULTI-CPLX), anaerobic ribonucleoside-triphosphate reductase (complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of ribonucleotides into deoxyribonucleotides, which are required for DNA synthesis and repair (PubMed:1460049, PubMed:24827372, PubMed:7568012, PubMed:7929317, PubMed:8381402, PubMed:9305874). Can reduce each of the four common ribonucleoside triphosphates (PubMed:7929317). {ECO:0000269|PubMed:1460049, ECO:0000269|PubMed:24827372, ECO:0000269|PubMed:7568012, ECO:0000269|PubMed:7929317, ECO:0000269|PubMed:8381402, ECO:0000269|PubMed:9305874}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-2863|complex.ecocyc.MONOMER0-2863]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.NRDACTMULTI-CPLX|complex.ecocyc.NRDACTMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX|complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4238|gene.b4238]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28903`
- `KEGG:ecj:JW4197;eco:b4238;ecoc:C3026_22875;`
- `GeneID:948755;`
- `GO:GO:0005524; GO:0006260; GO:0008270; GO:0008998; GO:0009265; GO:0015949; GO:0031250; GO:0032556; GO:0032564; GO:0032567`
- `EC:1.1.98.6`

## Notes

Anaerobic ribonucleoside-triphosphate reductase (EC 1.1.98.6) (Class III ribonucleoside-triphosphate reductase)
