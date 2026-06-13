---
entity_id: "protein.P0A937"
entity_type: "protein"
name: "bamE"
source_database: "UniProt"
source_id: "P0A937"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_00925, ECO:0000269|PubMed:17404237, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_00925, ECO:0000269|PubMed:17404237, ECO:0000269|PubMed:27686148}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bamE smpA b2617 JW2598"
---

# bamE

`protein.P0A937`

## Static

- Type: `protein`
- Source: `UniProt:P0A937`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_00925, ECO:0000269|PubMed:17404237, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_00925, ECO:0000269|PubMed:17404237, ECO:0000269|PubMed:27686148}.

## Enriched Summary

FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Nonessential member of the complex that stabilizes the interaction between the essential proteins BamA and BamD. May modulate the conformation of BamA, likely through interactions with BamD. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:17404237, ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21207987, ECO:0000269|PubMed:21586578, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:22178970, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}. Sequence analysis indicates that BamE is a lipoprotein in the outer membrane of Escherichia coli . Affinity purification experiments have shown BamE copurifies with BamA, BamD, BamB, and BamC...

## Biological Role

Component of outer membrane protein assembly complex (complex.ecocyc.CPLX0-3933).

## Annotation

FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Nonessential member of the complex that stabilizes the interaction between the essential proteins BamA and BamD. May modulate the conformation of BamA, likely through interactions with BamD. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:17404237, ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21207987, ECO:0000269|PubMed:21586578, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:22178970, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3933|complex.ecocyc.CPLX0-3933]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2617|gene.b2617]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A937`
- `KEGG:ecj:JW2598;eco:b2617;ecoc:C3026_14485;`
- `GeneID:93774466;945583;`
- `GO:GO:0016020; GO:0030674; GO:0042802; GO:0043165; GO:0046677; GO:0051205; GO:1990063`

## Notes

Outer membrane protein assembly factor BamE
