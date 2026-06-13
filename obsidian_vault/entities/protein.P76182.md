---
entity_id: "protein.P76182"
entity_type: "protein"
name: "rsxD"
source_database: "UniProt"
source_id: "P76182"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00462}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00462}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsxD rnfD ydgO b1630 JW1622"
---

# rsxD

`protein.P76182`

## Static

- Type: `protein`
- Source: `UniProt:P76182`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00462}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00462}.

## Enriched Summary

FUNCTION: Part of a membrane-bound complex that couples electron transfer with translocation of ions across the membrane (By similarity). Required to maintain the reduced state of SoxR. Probably transfers electron from NAD(P)H to SoxR (PubMed:12773378). {ECO:0000255|HAMAP-Rule:MF_00462, ECO:0000269|PubMed:12773378}. Products of the rsxABCDGE cluster and G7347 rseC are implicated in a pathway that functions to reduce the PD04132 SoxR iron-sulfur cluster; in-frame deletion of any gene within the cluster results in SoxR-mediated constitutive activation of EG10958 soxS transcription in the absence of oxidative stress . SoxR exists in a more oxidized form in rsx and rseC mutants . The periplasmic flavin transferase EG12073-MONOMER ApbE (renamed Ftp ) is also a component of this system; the RsxABCDGE, RseC and AbpE proteins likely form a complex that uses NAD(P)H to reduce SoxR . rsxD is predicted to encode an integral inner membrane protein; the proteins encoded by the rsxABCDGE gene cluster are predicted to form a membrane-associated complex . RsxD is predicted to contain a periplasmic flavin-binding domain . The rsxABCDGE gene cluster has similarity to the TAX-1061 rnf cluster (rnfABCDGEH ), which plays a role in nitrogenase reduction (see further )...

## Biological Role

Component of SoxR [2Fe-2S] reducing system, Rsx complex (complex.ecocyc.CPLX0-10852), SoxR [2Fe-2S] reducing system (complex.ecocyc.CPLX0-10853).

## Annotation

FUNCTION: Part of a membrane-bound complex that couples electron transfer with translocation of ions across the membrane (By similarity). Required to maintain the reduced state of SoxR. Probably transfers electron from NAD(P)H to SoxR (PubMed:12773378). {ECO:0000255|HAMAP-Rule:MF_00462, ECO:0000269|PubMed:12773378}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10852|complex.ecocyc.CPLX0-10852]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-10853|complex.ecocyc.CPLX0-10853]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1630|gene.b1630]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76182`
- `KEGG:ecj:JW1622;eco:b1630;ecoc:C3026_09365;`
- `GeneID:946134;`
- `GO:GO:0005886; GO:0022900; GO:0055085; GO:0098797; GO:1990204`
- `EC:7.-.-.-`

## Notes

Ion-translocating oxidoreductase complex subunit D (EC 7.-.-.-) (Rsx electron transport complex subunit D)
