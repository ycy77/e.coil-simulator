---
entity_id: "protein.P30177"
entity_type: "protein"
name: "ybiB"
source_database: "UniProt"
source_id: "P30177"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybiB b0800 JW0785"
---

# ybiB

`protein.P30177`

## Static

- Type: `protein`
- Source: `UniProt:P30177`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: DNA-binding protein that may be part of the LexA-controlled SOS response (PubMed:26063803). Binds with high affinity to DNA without sequence specificity (PubMed:26063803, PubMed:36864742). The difference in affinity between single- and double-stranded DNA is minor (PubMed:26063803). It also interacts with the GTPase ObgE, but does not influence ObgE GTP hydrolysis (PubMed:36864742). It may form a link between ObgE and the SOS response (PubMed:36864742). Does not show anthranilate phosphoribosyltransferase activity, nucleotide salvage activity or nucleoside phosphorylase activity (PubMed:26063803). {ECO:0000269|PubMed:26063803, ECO:0000269|PubMed:36864742}.

## Biological Role

Component of nonspecific DNA-binding protein YbiB (complex.ecocyc.CPLX0-8184).

## Annotation

FUNCTION: DNA-binding protein that may be part of the LexA-controlled SOS response (PubMed:26063803). Binds with high affinity to DNA without sequence specificity (PubMed:26063803, PubMed:36864742). The difference in affinity between single- and double-stranded DNA is minor (PubMed:26063803). It also interacts with the GTPase ObgE, but does not influence ObgE GTP hydrolysis (PubMed:36864742). It may form a link between ObgE and the SOS response (PubMed:36864742). Does not show anthranilate phosphoribosyltransferase activity, nucleotide salvage activity or nucleoside phosphorylase activity (PubMed:26063803). {ECO:0000269|PubMed:26063803, ECO:0000269|PubMed:36864742}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8184|complex.ecocyc.CPLX0-8184]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0800|gene.b0800]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30177`
- `KEGG:ecj:JW0785;eco:b0800;ecoc:C3026_05050;`
- `GeneID:75170865;75204915;945424;`
- `GO:GO:0000162; GO:0003677; GO:0003723; GO:0004048; GO:0005829; GO:0042803`

## Notes

DNA-binding protein YbiB
