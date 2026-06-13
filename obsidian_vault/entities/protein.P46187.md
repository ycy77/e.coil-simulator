---
entity_id: "protein.P46187"
entity_type: "protein"
name: "rseC"
source_database: "UniProt"
source_id: "P46187"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rseC b2570 JW2554"
---

# rseC

`protein.P46187`

## Static

- Type: `protein`
- Source: `UniProt:P46187`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: May play a role in reduction of the SoxR iron-sulfur cluster. May work together with the RsxABCDGE complex. {ECO:0000269|PubMed:12773378}. RseC is encoded as the fourth protein of the rpoE-rseABC operon . RseC, along with proteins encoded by the rsxABCDGE operon, may play a role in reduction of the SoxR iron-sulfur cluster . The periplasmic flavin transferase EG12073-MONOMER ApbE (renamed Ftp ) is also a component of this system; the RsxABCDGE, RseC and AbpE proteins likely form a complex that uses NAD(P)H to reduce SoxR . RseC may have additional SoxR-independent roles . RseC is predicted to be an inner membrane protein with two transmembrane domains; experimental topology analysis suggests that both the N-terminal and C-terminal domains are located in the cytoplasm . The N-terminal region of RseC contains a conserved cysteine motif (CX2CX5C); the purified N-terminal domain (residues 1-70) can form an oxygen-sensitive Fe-S cluster . Genetic evidence suggests that RseC has a subtle positive effect on σE activity and a minor positive role in the regulation of cell lysis . However, an rseC mutant is also reported to show wild-type σE activity under inducing or non-inducing conditions . An rseC mutant exhibits constitutive soxS expression mediated by oxidized SoxR protein , as well as increased motility and biofilm formation compared to wild type...

## Biological Role

Component of SoxR [2Fe-2S] reducing system (complex.ecocyc.CPLX0-10853).

## Annotation

FUNCTION: May play a role in reduction of the SoxR iron-sulfur cluster. May work together with the RsxABCDGE complex. {ECO:0000269|PubMed:12773378}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10853|complex.ecocyc.CPLX0-10853]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2570|gene.b2570]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46187`
- `KEGG:ecj:JW2554;eco:b2570;ecoc:C3026_14235;`
- `GeneID:947052;`
- `GO:GO:0005886; GO:0006979; GO:0016651; GO:0098797; GO:1990204`

## Notes

Protein RseC
