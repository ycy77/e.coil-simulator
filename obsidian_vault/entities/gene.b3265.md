---
entity_id: "gene.b3265"
entity_type: "gene"
name: "acrE"
source_database: "NCBI RefSeq"
source_id: "gene-b3265"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3265"
  - "acrE"
---

# acrE

`gene.b3265`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3265`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acrE (gene.b3265) is a gene entity. It encodes acrE (protein.P24180). Encoded protein function: FUNCTION: Part of the tripartite efflux system AcrEF-TolC. Involved in the efflux of indole and organic solvents. {ECO:0000269|PubMed:10518736, ECO:0000269|PubMed:11274125}. EcoCyc product frame: EG10266-MONOMER. EcoCyc synonyms: envC. Genomic coordinates: 3413864-3415021. EcoCyc protein note: AcrE shares 65% amino acid identity with the membrane fusion protein EG11703-MONOMER "AcrA" of the AcrAB efflux pump complex . acrEF is not expressed at significant levels in wild-type K-12 strains (see ) but is expressed at high level upon integration of IS1 or IS2 into the upstream region of the operon or upon deletion of the PD00288 "H-NS repressor protein" ; when expressed AcrE functions in Escherichia coli as part of a drug efflux system with the AcrF RND type permease and the TolC outer membrane protein (see CPLX0-2141 for more details). Cloned AcrE is an inner membrane anchored lipoprotein .

## Biological Role

Repressed by nac (protein.Q47005). Activated by zraR (protein.P14375).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24180|protein.P24180]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=acrE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=acrE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010722,ECOCYC:EG10266,GeneID:947706`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3413864-3415021:+; feature_type=gene
