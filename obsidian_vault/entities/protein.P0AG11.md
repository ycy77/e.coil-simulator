---
entity_id: "protein.P0AG11"
entity_type: "protein"
name: "umuD"
source_database: "UniProt"
source_id: "P0AG11"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "umuD b1183 JW1172"
---

# umuD

`protein.P0AG11`

## Static

- Type: `protein`
- Source: `UniProt:P0AG11`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in UV protection and mutation. Poorly processive, error-prone DNA polymerase involved in translesion repair (PubMed:10801133). Essential for induced (or SOS) mutagenesis. Able to replicate DNA across DNA lesions (thymine photodimers and abasic sites, called translesion synthesis) in the presence of activated RecA; efficiency is maximal in the presence of the beta sliding-clamp and clamp-loading complex of DNA polymerase III plus single-stranded binding protein (SSB) (PubMed:10801133). RecA and to a lesser extent the beta clamp-complex may target Pol V to replication complexes stalled at DNA template lesions (PubMed:10801133). {ECO:0000269|PubMed:10801133}. Following induction of the SOS response, UmuD is proteolytically processed into UmuD' in a cleavage reaction that depends on activated RecA . UmuD has sequence similarity with LexA, which is also cleaved in a RecA-mediated fashion . This cleavage to produce UmuD' is required for UV mutagenesis and inclusion in the final Polymerase V (Pol V) protein complex . RecA does not actually cleave UmuD, instead somehow promoting cleavage of one member of an UmuD pair by its dimerization partner . The UmuD amino-terminus controls the rate of this cleavage, which occurs only after a lag time following UV irradiation . The full-length UmuD and truncated UmuD' proteins are both subject to proteolytic regulation...

## Biological Role

Component of DNA polymerase V (complex.ecocyc.CPLX0-3925).

## Annotation

FUNCTION: Involved in UV protection and mutation. Poorly processive, error-prone DNA polymerase involved in translesion repair (PubMed:10801133). Essential for induced (or SOS) mutagenesis. Able to replicate DNA across DNA lesions (thymine photodimers and abasic sites, called translesion synthesis) in the presence of activated RecA; efficiency is maximal in the presence of the beta sliding-clamp and clamp-loading complex of DNA polymerase III plus single-stranded binding protein (SSB) (PubMed:10801133). RecA and to a lesser extent the beta clamp-complex may target Pol V to replication complexes stalled at DNA template lesions (PubMed:10801133). {ECO:0000269|PubMed:10801133}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3925|complex.ecocyc.CPLX0-3925]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1183|gene.b1183]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG11`
- `KEGG:ecj:JW1172;eco:b1183;ecoc:C3026_06970;`
- `GeneID:93776251;945746;`
- `GO:GO:0001217; GO:0003676; GO:0003697; GO:0003887; GO:0005829; GO:0006281; GO:0006508; GO:0006974; GO:0008094; GO:0008236; GO:0009355; GO:0009432; GO:0019985; GO:0032993; GO:0042802; GO:0043565; GO:0045892`
- `EC:3.4.21.-`

## Notes

Protein UmuD (EC 3.4.21.-) (DNA polymerase V) (Pol V) [Cleaved into: Protein UmuD']
