---
entity_id: "protein.P77774"
entity_type: "protein"
name: "bamB"
source_database: "UniProt"
source_id: "P77774"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_00923, ECO:0000269|PubMed:15851030, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_00923, ECO:0000269|PubMed:15851030, ECO:0000269|PubMed:27686148}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bamB yfgL b2512 JW2496"
---

# bamB

`protein.P77774`

## Static

- Type: `protein`
- Source: `UniProt:P77774`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_00923, ECO:0000269|PubMed:15851030, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_00923, ECO:0000269|PubMed:15851030, ECO:0000269|PubMed:27686148}.

## Enriched Summary

FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Nonessential member of the complex, which may orient the flexible periplasmic domain of BamA for interaction with other Bam components, chaperones and nascent outer membrane proteins. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21277859, ECO:0000269|PubMed:21586578, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}. The BamB (formerly YfgL) lipoprotein is part of the large multi-protein BAM complex responsible for the assembly and insertion of outer membrane β-barrel proteins in E.coli. BamB is an outer membrane lipoprotein that is attached via its N-terminal palmitate lipid anchor to the periplasmic side of the outer membrane . BamB forms a complex with BamA, BamC and BamD...

## Biological Role

Component of outer membrane protein assembly complex (complex.ecocyc.CPLX0-3933).

## Annotation

FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Nonessential member of the complex, which may orient the flexible periplasmic domain of BamA for interaction with other Bam components, chaperones and nascent outer membrane proteins. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21277859, ECO:0000269|PubMed:21586578, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3933|complex.ecocyc.CPLX0-3933]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2512|gene.b2512]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77774`
- `KEGG:ecj:JW2496;eco:b2512;ecoc:C3026_13930;`
- `GeneID:946982;`
- `GO:GO:0009279; GO:0016020; GO:0042802; GO:0043165; GO:0051205; GO:1990063`

## Notes

Outer membrane protein assembly factor BamB
