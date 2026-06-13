---
entity_id: "gene.b2077"
entity_type: "gene"
name: "mdtD"
source_database: "NCBI RefSeq"
source_id: "gene-b2077"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2077"
  - "mdtD"
---

# mdtD

`gene.b2077`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2077`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtD (gene.b2077) is a gene entity. It encodes mdtD (protein.P36554). Encoded protein function: Putative multidrug resistance protein MdtD EcoCyc product frame: B2077-MONOMER. EcoCyc synonyms: yegB, iceT. Genomic coordinates: 2161464-2162879. EcoCyc protein note: In the Transporter Classification Database, MdtD is a member of the Drug:H+ Antiporter-2 (DHA2) family within the major facilitator superfamily (MFS) . Overexpression of cloned mdtD in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) does not impact resistance to a range of toxic compounds (dyes, detergents, antibiotics and others) compared to the mutant parent . Intracellular arabinose concentration (measured indirectly though araBAD promoter activity) is increased in a ΔmdtD strain compared to wild type; overexpression of mdtD does not affect intracellular arabinose levels . Accumulation of the cationic fluorescent dyes 3,3'-dipropylthiadicarbocyanine iodide (diS-C3) and SYBR Green is greater in mdtD knockout cells compared to wild type...

## Biological Role

Activated by rob (protein.P0ACI0), cpxR (protein.P0AE88), baeR (protein.P69228).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36554|protein.P36554]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=mdtD; function=+
- `activates` <-- [[protein.P69228|protein.P69228]] `RegulonDB` `S` - regulator=BaeR; target=mdtD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006879,ECOCYC:EG12136,GeneID:946601`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2161464-2162879:+; feature_type=gene
