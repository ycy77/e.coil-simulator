---
entity_id: "protein.P0A903"
entity_type: "protein"
name: "bamC"
source_database: "UniProt"
source_id: "P0A903"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_00924, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_00924, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:27686148}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bamC dapX nlpB b2477 JW2462"
---

# bamC

`protein.P0A903`

## Static

- Type: `protein`
- Source: `UniProt:P0A903`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_00924, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_00924, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:27686148}.

## Enriched Summary

FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Nonessential member of the complex that stabilizes the interaction between the essential proteins BamA and BamD. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:22178970, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}. The BamC (formerly NlpB) lipoprotein is part of the large multi-protein BAM complex responsible for the assembly and insertion of outer membrane β-barrel proteins in E.coli. BamC is a non-essential outer membrane lipoprotein . BamC is exposed on the cell surface . BamC forms a complex with BamA, BamB and BamD . BamC interacts directly with BamD in vitro...

## Biological Role

Component of outer membrane protein assembly complex (complex.ecocyc.CPLX0-3933).

## Annotation

FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Nonessential member of the complex that stabilizes the interaction between the essential proteins BamA and BamD. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:22178970, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3933|complex.ecocyc.CPLX0-3933]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2477|gene.b2477]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A903`
- `KEGG:ecj:JW2462;eco:b2477;ecoc:C3026_13750;`
- `GeneID:93774661;946954;`
- `GO:GO:0009986; GO:0016020; GO:0042802; GO:0043165; GO:0051205; GO:1990063`

## Notes

Outer membrane protein assembly factor BamC
