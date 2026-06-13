---
entity_id: "gene.b3216"
entity_type: "gene"
name: "yhcD"
source_database: "NCBI RefSeq"
source_id: "gene-b3216"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3216"
  - "yhcD"
---

# yhcD

`gene.b3216`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3216`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhcD (gene.b3216) is a gene entity. It encodes yhcD (protein.P45420). Encoded protein function: FUNCTION: Involved in the export and assembly of a fimbrial subunit across the outer membrane. {ECO:0000250}. EcoCyc product frame: G7670-MONOMER. Genomic coordinates: 3362807-3365188. EcoCyc protein note: In the Transporter Classification Database E. coli YhcD is a member of the Outer Membrane Fimbrial Usher Porin (FUP) Family . YhcD binds human complement component C3 in vitro; YhcD is implicated in a pathway of glycine-promoted, complement-dependent, cell death . CRP-cAMP, FlhC and CsgD regulate the expression of yhcD during glycine dependent serum mediated cell death . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including gltF-yhcADEF; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Repressed by glaR (protein.P37338), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45420|protein.P45420]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yhcD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yhcD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010554,ECOCYC:G7670,GeneID:947738`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3362807-3365188:+; feature_type=gene
