---
entity_id: "protein.P0A940"
entity_type: "protein"
name: "bamA"
source_database: "UniProt"
source_id: "P0A940"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_01430, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:23882017, ECO:0000269|PubMed:24619089, ECO:0000269|PubMed:24914988, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:9298646}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bamA yaeT yzzN yzzY b0177 JW0172"
---

# bamA

`protein.P0A940`

## Static

- Type: `protein`
- Source: `UniProt:P0A940`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_01430, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:23882017, ECO:0000269|PubMed:24619089, ECO:0000269|PubMed:24914988, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:9298646}.

## Enriched Summary

FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Constitutes, with BamD, the core component of the assembly machinery. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:15951436, ECO:0000269|PubMed:16102012, ECO:0000269|PubMed:16824102, ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}.; FUNCTION: (Microbial infection) Acts as a receptor for CdiA-EC93, the contact-dependent growth inhibition (CDI) effector of E.coli strain EC93; antibodies against extracellular epitopes decrease CDI. Its role in CDI is independent of the other Bam complex components (PubMed:18761695). Is not the receptor for CdiA from E...

## Biological Role

Component of outer membrane protein assembly complex (complex.ecocyc.CPLX0-3933).

## Annotation

FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Constitutes, with BamD, the core component of the assembly machinery. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:15951436, ECO:0000269|PubMed:16102012, ECO:0000269|PubMed:16824102, ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}.; FUNCTION: (Microbial infection) Acts as a receptor for CdiA-EC93, the contact-dependent growth inhibition (CDI) effector of E.coli strain EC93; antibodies against extracellular epitopes decrease CDI. Its role in CDI is independent of the other Bam complex components (PubMed:18761695). Is not the receptor for CdiA from E.coli strain 536 / UPEC, which does not have the same mode of toxicity as CdiA from strain EC93; the decreased expression of bamA101 in some experiments decreases the level of outer membrane proteins in general (PubMed:23469034, PubMed:23882017). Susceptibility to CdiA-EC93 is dependent on E.coli BamA; replacing BamA with the gene from S.typhimurium LT2, E.cloacae ATCC 13047 or D.dadantii 3937 renders cells resistant to CdiA-EC93. Cells with BamA from another bacteria no longer form CdiA-EC93-induced aggregates with EC93 cells. A chimera in which E.cloacae extracellular loops 6 and 7 are replaced with loops 6 and 7 from E.coli is susceptible to CdiA-EC93 and to CdiA-CT from strain 536 / UPEC (PubMed:23882017). {ECO:0000269|PubMed:18761695, ECO:0000269|PubMed:23469034, ECO:0000269|PubMed:23882017}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3933|complex.ecocyc.CPLX0-3933]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0177|gene.b0177]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A940`
- `KEGG:ecj:JW0172;eco:b0177;ecoc:C3026_00810;`
- `GeneID:93777248;944870;`
- `GO:GO:0007155; GO:0009279; GO:0016020; GO:0043165; GO:0051087; GO:0051205; GO:1990063`

## Notes

Outer membrane protein assembly factor BamA (Omp85)
