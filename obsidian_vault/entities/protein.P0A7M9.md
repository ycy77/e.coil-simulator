---
entity_id: "protein.P0A7M9"
entity_type: "protein"
name: "rpmE"
source_database: "UniProt"
source_id: "P0A7M9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpmE b3936 JW3907"
---

# rpmE

`protein.P0A7M9`

## Static

- Type: `protein`
- Source: `UniProt:P0A7M9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Binds the 23S rRNA. {ECO:0000250}. The L31 protein is a component of the 50S subunit of the ribosome. An atomic model for L31 within the 70S ribosome was obtained by single-particle cryo-EM. L31 bridges the 30S and 50S subunits between the 30S head and the 50S central protuberance. A flexible linker region in L31 accomodates large-scale rearrangements during ratcheting of the ribosome . L31 is involved in translation initiation, reading frame maintenance , stabilization of subunit association , and formation of 100S ribosomes in stationary phase . L31 also counteracts intrinsic ribosome destabilization by certain nascent peptide sequences . L31 can be isolated in a complex with 5S rRNA and L5, L18, and L25 and can be crosslinked to tRNA in the P site . Modeling shows that L31 may participate in the formation, dynamics and stabilization of the S13-L5 bridge . L31 may only be loosely associated with the ribosome . An extensive crosslinking and mass spectrometry study of ribosomal proteins clarified the localization and flexibility of L31 within the ribosome . Expression of L31 is autoregulated. The N-terminal residues 2-8 of L31 are required for autoregulatory activity. A conserved stem-loop structure upstream of the ribosome binding site is required for autoregulation and appears to separate two parts of a non-contiguous translation initiation region...

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: Binds the 23S rRNA. {ECO:0000250}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3936|gene.b3936]] `RegulonDB` `S` - regulator=RpmE; target=rpmE; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3936|gene.b3936]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7M9`
- `KEGG:ecj:JW3907;eco:b3936;ecoc:C3026_21270;`
- `GeneID:93777962;948425;`
- `GO:GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0006412; GO:0006413; GO:0008270; GO:0019843; GO:0022625; GO:1904689`

## Notes

Large ribosomal subunit protein bL31 (50S ribosomal protein L31)
