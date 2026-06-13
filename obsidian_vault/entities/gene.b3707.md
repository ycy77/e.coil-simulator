---
entity_id: "gene.b3707"
entity_type: "gene"
name: "tnaC"
source_database: "NCBI RefSeq"
source_id: "gene-b3707"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3707"
  - "tnaC"
---

# tnaC

`gene.b3707`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3707`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tnaC (gene.b3707) is a gene entity. It encodes tnaC (protein.P0AD89). Encoded protein function: FUNCTION: Required for tryptophan-regulated expression of the tna operon. In the presence of high levels of L-Trp release of this nascent peptide by release factor 2 (RF2, prfB) is inhibited. The ribosome stalls with Pro-24 in the P site and a UGA stop codon in the A site. This prevents transcription termination factor Rho binding, and thus allows transcription and translation of downstream TnaA and TnaB (PubMed:12228716, PubMed:34504068). The presence of TnaC and L-Trp prevents the catalytic GGQ motif of RF2 from engaging with the peptidyl-transferase center (PTC); nucleotides of the PTC are perturbed while Arg-23 probably clashes with 'N5-methyl-Gln-252' of RF2, preventing RF2 from reaching the PTC, and from releasing the translated TnaC peptide (PubMed:34403461, PubMed:34504068). Translation of this peptide turns the ribosome into a small-molecule sensor specifically recognizing L-Trp (PubMed:34403461, PubMed:34504068). {ECO:0000269|PubMed:12228716, ECO:0000269|PubMed:34403461, ECO:0000269|PubMed:34504068}. EcoCyc product frame: EG11276-MONOMER. EcoCyc synonyms: tnaL. Genomic coordinates: 3888435-3888509. EcoCyc protein note: The TnaC leader peptide is required for regulation by attenuation of the TU00085 operon...

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), torR (protein.P38684), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD89|protein.P0AD89]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tnaC; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=tnaC; function=+
- `activates` <-- [[protein.P38684|protein.P38684]] `RegulonDB` `S` - regulator=TorR; target=tnaC; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=tnaC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012128,ECOCYC:EG11276,GeneID:948223`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3888435-3888509:+; feature_type=gene
