---
entity_id: "protein.P06996"
entity_type: "protein"
name: "ompC"
source_database: "UniProt"
source_id: "P06996"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:2464593}; Multi-pass membrane protein {ECO:0000269|PubMed:16949612}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ompC meoA par b2215 JW2203"
---

# ompC

`protein.P06996`

## Static

- Type: `protein`
- Source: `UniProt:P06996`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:2464593}; Multi-pass membrane protein {ECO:0000269|PubMed:16949612}.

## Enriched Summary

FUNCTION: Forms pores that allow passive diffusion of small molecules across the outer membrane.; FUNCTION: (Microbial infection) Supports colicin E5 entry in the absence of its major receptor OmpF. {ECO:0000305|PubMed:27723824}.; FUNCTION: (Microbial infection) A mixed OmpC-OmpF heterotrimer is the outer membrane receptor for toxin CdiA-EC536; polymorphisms in extracellular loops 4 and 5 of OmpC confer susceptibility to CdiA-EC536-mediated toxicity. {ECO:0000269|PubMed:27723824}. OmpC is a general outer membrane (OM) porin which mediates the non-specific diffusion of small solutes such as sugars, ions and amino acids; the major non-specific OM porins of E. coli K-12 (OmpC and CPLX0-7534 "OmpF") are typically defined by an exclusion limit based on substrate mass (~600 daltons) but there are large differences in penetration rates within solutes due to factors such as size, hydrophobicity and charge (discussed in ). OmpC acts as a receptor for bacteriophages 434, T4 and Bp7 (see and further ). Purified OmpC reconstituted into artificial lipid bilayer membranes forms an ion permeable channel with a slight preference for cations...

## Biological Role

Component of outer membrane porin C (complex.ecocyc.CPLX0-7533).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Forms pores that allow passive diffusion of small molecules across the outer membrane.; FUNCTION: (Microbial infection) Supports colicin E5 entry in the absence of its major receptor OmpF. {ECO:0000305|PubMed:27723824}.; FUNCTION: (Microbial infection) A mixed OmpC-OmpF heterotrimer is the outer membrane receptor for toxin CdiA-EC536; polymorphisms in extracellular loops 4 and 5 of OmpC confer susceptibility to CdiA-EC536-mediated toxicity. {ECO:0000269|PubMed:27723824}.

## Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b2215|gene.b2215]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06996`
- `KEGG:ecj:JW2203;eco:b2215;ecoc:C3026_12375;`
- `GeneID:946716;`
- `GO:GO:0001618; GO:0006974; GO:0009279; GO:0015288; GO:0034220; GO:0042802; GO:0046813; GO:0046872; GO:0046930; GO:0120010`

## Notes

Outer membrane porin C (Outer membrane protein 1B) (Outer membrane protein C) (Porin OmpC)
