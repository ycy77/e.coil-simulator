---
entity_id: "gene.b3170"
entity_type: "gene"
name: "rimP"
source_database: "NCBI RefSeq"
source_id: "gene-b3170"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3170"
  - "rimP"
---

# rimP

`gene.b3170`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3170`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rimP (gene.b3170) is a gene entity. It encodes rimP (protein.P0A8A8). Encoded protein function: FUNCTION: Required for maturation of 30S ribosomal subunits, probably at a late stage of ribosomal protein binding, while Era is associated and after RimM (PubMed:20188109). {ECO:0000269|PubMed:19150615, ECO:0000269|PubMed:20188109}. EcoCyc product frame: EG11179-MONOMER. EcoCyc synonyms: yhbC. Genomic coordinates: 3317554-3318006. EcoCyc protein note: RimP assists in the maturation of the 30S subunit of the ribosome. The protein associates with free 30S ribosomal subunits . The effect of RimP during in vitro reconstitution of the 30S ribosomal subunit has been investigated . RimP plays an important role in stabilization of the central pseudoknot structure of 16S rRNA and influences the assembly kinetics of certain ribosomal protein subunits . The secondary structure of RimP has been predicted from NMR data . Contrary to results reported earlier (, see below), a rimP in-frame deletion mutant has a reduced growth rate compared to the wild type, especially at higher temperatures, and shows a defect in 30S ribosomal subunit maturation . A rimP insertion mutant shows a more than 1000-fold increased level of transposition of IS903 . Expression of rimP decreased in a recombinant xylitol-producing strain; introduction of a rimP deletion into that strain increased production of xylitol...

## Biological Role

Repressed by argR (protein.P0A6D0), crp (protein.P0ACJ8), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8A8|protein.P0A8A8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rimP; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=rimP; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=rimP; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rimP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010417,ECOCYC:EG11179,GeneID:947680`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3317554-3318006:-; feature_type=gene
