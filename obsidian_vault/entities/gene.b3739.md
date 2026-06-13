---
entity_id: "gene.b3739"
entity_type: "gene"
name: "atpI"
source_database: "NCBI RefSeq"
source_id: "gene-b3739"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3739"
  - "atpI"
---

# atpI

`gene.b3739`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3739`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atpI (gene.b3739) is a gene entity. It encodes atpI (protein.P0ABC0). Encoded protein function: FUNCTION: A possible function for this protein is to guide the assembly of the membrane sector of the ATPase enzyme complex. EcoCyc product frame: EG10106-MONOMER. EcoCyc synonyms: uncI. Genomic coordinates: 3922060-3922440. EcoCyc protein note: A nonpolar mutation in the atpI gene shows that the AtpI protein is not an essential component of the H+-ATPase complex. However, the mutant has a slightly lower growth yield, and membranes contain 20% less ATPase activity than wild-type . Expression of AtpI is 10 to 20-fold lower than expression of AtpB, which is encoded by the second open reading frame of the atp operon . Processing of the mRNA and low efficiency of translation initiation may account for lower levels of atpI transcript and AtpI protein . atpI appears to affect AtpB expression at a post-translation initiation step . unc: uncoupled mutants (see ). Review:

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABC0|protein.P0ABC0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=atpI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012224,ECOCYC:EG10106,GeneID:948251`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3922060-3922440:-; feature_type=gene
