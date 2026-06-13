---
entity_id: "protein.P67701"
entity_type: "protein"
name: "higA"
source_database: "UniProt"
source_id: "P67701"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "higA ygjM b3082 JW3053"
---

# higA

`protein.P67701`

## Static

- Type: `protein`
- Source: `UniProt:P67701`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Functions as an mRNA interferase antitoxin; overexpression prevents HigB-mediated cessation of cell growth and inhibition of cell proliferation. {ECO:0000269|PubMed:19943910}.

## Biological Role

Component of antitoxin/DNA-binding transcriptional repressor HigA (complex.ecocyc.CPLX0-8229), HigB-HigA toxin/antitoxin complex and DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-8230).

## Annotation

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Functions as an mRNA interferase antitoxin; overexpression prevents HigB-mediated cessation of cell growth and inhibition of cell proliferation. {ECO:0000269|PubMed:19943910}.

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8229|complex.ecocyc.CPLX0-8229]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8230|complex.ecocyc.CPLX0-8230]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b3082|gene.b3082]] `RegulonDB` `S` - regulator=HigA; target=higA; function=-
- `represses` --> [[gene.b3083|gene.b3083]] `RegulonDB` `S` - regulator=HigA; target=higB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3082|gene.b3082]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P67701`
- `KEGG:ecj:JW3053;eco:b3082;ecoc:C3026_16830;`
- `GeneID:947593;`
- `GO:GO:0001046; GO:0006355; GO:0040008; GO:0042803; GO:0110001`

## Notes

Antitoxin HigA
