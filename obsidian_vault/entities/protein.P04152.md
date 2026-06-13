---
entity_id: "protein.P04152"
entity_type: "protein"
name: "umuC"
source_database: "UniProt"
source_id: "P04152"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "umuC b1184 JW1173"
---

# umuC

`protein.P04152`

## Static

- Type: `protein`
- Source: `UniProt:P04152`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in UV protection and mutation. Poorly processive, error-prone DNA polymerase involved in translesion repair (PubMed:10801133). Essential for induced (or SOS) mutagenesis. Able to replicate DNA across DNA lesions (thymine photodimers and abasic sites, translesion synthesis) in the presence of activated RecA; efficiency is maximal in the presence of the beta sliding-clamp and clamp-loading complex of DNA polymerase III plus single-stranded binding protein (SSB) (PubMed:10801133). RecA and to a lesser extent the beta clamp-complex may target Pol V to replication complexes stalled at DNA template lesions (PubMed:10801133). {ECO:0000269|PubMed:10801133}. UmuC is a DNA polymerase specialized for trans-lesion synthesis (TLS) in E. coli K-12 . UmuC requires UmuD', RecA and SSB for TLS in vitro UmuC is degraded by the Lon protease, limiting total UmuC abundance . Most, but not all UV-induced mutation requires functional UmuC . Loss of umuC results in UV sensitivity and difficulty repairing daughter strand gaps, but not double-strand breaks . UmuC is required for some spontaneous base-pair substitutions . Following UV irradiation, UmuC synthesis increases and it is sequestered at the inner membrane; release of UmuC requires UmuD cleavage to UmuD' . The chaperones Hsp70 (DnaK) and Hsp60 (MopA) help fold UmuC into its functional form...

## Biological Role

Component of DNA polymerase V (complex.ecocyc.CPLX0-3925).

## Annotation

FUNCTION: Involved in UV protection and mutation. Poorly processive, error-prone DNA polymerase involved in translesion repair (PubMed:10801133). Essential for induced (or SOS) mutagenesis. Able to replicate DNA across DNA lesions (thymine photodimers and abasic sites, translesion synthesis) in the presence of activated RecA; efficiency is maximal in the presence of the beta sliding-clamp and clamp-loading complex of DNA polymerase III plus single-stranded binding protein (SSB) (PubMed:10801133). RecA and to a lesser extent the beta clamp-complex may target Pol V to replication complexes stalled at DNA template lesions (PubMed:10801133). {ECO:0000269|PubMed:10801133}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3925|complex.ecocyc.CPLX0-3925]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1184|gene.b1184]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04152`
- `KEGG:ecj:JW1173;eco:b1184;ecoc:C3026_06975;`
- `GeneID:946359;`
- `GO:GO:0003684; GO:0003697; GO:0003887; GO:0005829; GO:0005886; GO:0006281; GO:0006974; GO:0008094; GO:0009355; GO:0009432; GO:0016020; GO:0019985; GO:0042276`

## Notes

Protein UmuC (DNA polymerase V) (Pol V)
