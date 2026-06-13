---
entity_id: "gene.b3179"
entity_type: "gene"
name: "rlmE"
source_database: "NCBI RefSeq"
source_id: "gene-b3179"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3179"
  - "rlmE"
---

# rlmE

`gene.b3179`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3179`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlmE (gene.b3179) is a gene entity. It encodes rlmE (protein.P0C0R7). Encoded protein function: FUNCTION: Specifically methylates the uridine in position 2552 of 23S rRNA at the 2'-O position of the ribose in the fully assembled 50S ribosomal subunit. {ECO:0000269|PubMed:10748051}. EcoCyc product frame: EG11507-MONOMER. EcoCyc synonyms: ftsJ, mrsF, rrmJ. Genomic coordinates: 3327035-3327664. EcoCyc protein note: RlmE is the methyltransferase responsible for methylation of 23S rRNA at the 2'-O position of the ribose at the universally conserved U2552 nucleotide . In vitro, the enzyme is active on ribosomes and the 50S ribosomal subunit, but not free rRNA . The 45S ribosomal subunit precursor that accumulates in an rlmE mutant is a true intermediate on the pathway of 50S subunit assembly. 2'-O-methylation of U2552 promotes association between helices 92 and 71 of 23S rRNA; together with incorporation of EG11232-MONOMER, it promotes late steps of 50S ribosomal subunit assembly . Cryo-EM structures and biochemical assays show that 2'-O-methylation of U2552 plays a role in ribosome biogenesis and protein translation . A crystal structure of RlmE has been solved at 1.5 Å resolution . Site-directed mutagenesis has identified possible active site and substrate binding residues, and a reaction mechanism has been proposed...

## Biological Role

Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C0R7|protein.P0C0R7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rlmE; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rlmE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010447,ECOCYC:EG11507,GeneID:947689`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3327035-3327664:-; feature_type=gene
