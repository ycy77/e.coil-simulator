---
entity_id: "protein.P0AC02"
entity_type: "protein"
name: "bamD"
source_database: "UniProt"
source_id: "P0AC02"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_00922, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_00922, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:27686148}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bamD yfiO b2595 JW2577"
---

# bamD

`protein.P0AC02`

## Static

- Type: `protein`
- Source: `UniProt:P0AC02`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_00922, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_00922, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:27686148}.

## Enriched Summary

FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Constitutes, with BamA, the core component of the assembly machinery. Probably involved in transient protein interactions. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:16824102, ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21586578, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:22281737, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}. The BamD lipoprotein is part of the large multi-protein BAM complex responsible for the assembly and insertion of outer membrane β-barrel proteins. BamD is an essential outer membrane lipoprotein . BamD forms a complex with BamA, BamB and BamC . BamD interacts directly with BamA in vitro...

## Biological Role

Component of outer membrane protein assembly complex (complex.ecocyc.CPLX0-3933).

## Annotation

FUNCTION: Part of the outer membrane protein assembly complex (Bam), which is involved in assembly and insertion of beta-barrel proteins into the outer membrane. Constitutes, with BamA, the core component of the assembly machinery. Probably involved in transient protein interactions. Efficient substrate folding and insertion into the outer membrane requires all 5 subunits (PubMed:20378773, PubMed:21823654, PubMed:27686148). A lateral gate may open between the first and last strands of the BamA beta-barrel that allows substrate to insert into the outer membrane; comparison of the structures of complete and nearly complete Bam complexes show there is considerable movement of all 5 proteins (PubMed:26744406, PubMed:26900875, PubMed:26901871, PubMed:27686148). {ECO:0000269|PubMed:16824102, ECO:0000269|PubMed:20378773, ECO:0000269|PubMed:21586578, ECO:0000269|PubMed:21823654, ECO:0000269|PubMed:22281737, ECO:0000269|PubMed:26744406, ECO:0000269|PubMed:26900875, ECO:0000269|PubMed:26901871, ECO:0000269|PubMed:27686148}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3933|complex.ecocyc.CPLX0-3933]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2595|gene.b2595]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC02`
- `KEGG:ecj:JW2577;eco:b2595;ecoc:C3026_14380;`
- `GeneID:93774491;947086;`
- `GO:GO:0009279; GO:0016020; GO:0043165; GO:0051205; GO:1990063`

## Notes

Outer membrane protein assembly factor BamD
