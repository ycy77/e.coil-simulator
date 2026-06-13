---
entity_id: "gene.b1707"
entity_type: "gene"
name: "rflP"
source_database: "NCBI RefSeq"
source_id: "gene-b1707"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1707"
  - "rflP"
---

# rflP

`gene.b1707`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1707`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rflP (gene.b1707) is a gene entity. It encodes ydiV (protein.P76204). Encoded protein function: FUNCTION: Upon overexpression acts as a novel anti-FlhC(2)FlhD(4) factor, decreasing its DNA-binding activity, able to negatively regulate expression of flagellar class II operons including FliC. EcoCyc product frame: G6925-MONOMER. EcoCyc synonyms: ydiV. Genomic coordinates: 1791307-1792020. EcoCyc protein note: RflP is involved in the control of motility and may be involved in quorum sensing . However, impaired translation leads to low levels of RflP protein in vivo and makes flagellar synthesis insensitive to RflP-mediated inhibition in E. coli K-12 . RflP contains a degenerate EAL phosphodiesterase domain . Both E. coli and Salmonella regulate expression of flagella and motility in response to nutrient availability, but in opposite directions. E. coli shows higher motility under nutrient-poor conditions, while Salmonella is more motile under nutrient-rich conditions. The function of RflP was first studied in Salmonella, where it was shown to regulate flagellar biosynthesis by acting as an anti-FlhDC factor. It has now been shown that RflP functions as an anti-CPLX0-3930 "FlhDC" factor in E. coli as well. In vitro, RflP interacts with both FlhD and FlhC and inhibits fliA promoter binding of FlhDC in a gel shift assay...

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by sdiA (protein.P07026), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76204|protein.P76204]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P07026|protein.P07026]] `RegulonDB` `S` - regulator=SdiA; target=rflP; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rflP; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005696,ECOCYC:G6925,GeneID:946217`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1791307-1792020:-; feature_type=gene
