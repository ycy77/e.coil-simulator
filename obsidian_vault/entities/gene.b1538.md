---
entity_id: "gene.b1538"
entity_type: "gene"
name: "dcp"
source_database: "NCBI RefSeq"
source_id: "gene-b1538"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1538"
  - "dcp"
---

# dcp

`gene.b1538`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1538`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dcp (gene.b1538) is a gene entity. It encodes dcp (protein.P24171). Encoded protein function: FUNCTION: Removes dipeptides from the C-termini of N-blocked tripeptides, tetrapeptides and larger peptides. {ECO:0000269|PubMed:8226676}. EcoCyc product frame: EG10212-MONOMER. Genomic coordinates: 1625335-1627380. EcoCyc protein note: Dipeptidyl carboxypeptidase is a peptidase capable of cleaving peptide bonds in amino-blocked small peptide substrates . It is required for growth when only amino-blocked peptides such as N-acetyl-alanylalanylalanine and N-benzoyl-glycylhistidylleucine are available as carbon sources . A fraction of the total pool of dipeptidyl carboxypeptidase is in the periplasm . Dcp- mutants are unable to grow with N-acetylalanylalanylalanine as the sole nitrogen source . Recombinant enzyme purified from cell extracts appeared to be a monomer based on an apparent molecular mass of 80 kDa by gel filtration chromatography and 78 kDa by SDS-PAGE . Protease inhibitors and divalent cations had varying effects on enzymatic activity. PMSF showed little inhibition; the cysteine protease inhibitor E64, trypsin inhibitors, pepstatin, EDTA, and NaCl showed some inhibition; chymostatin was a relatively stronger inhibitor; and 1,10-phenanthroline completely inhibited. Among divalent cations, some activation was seen with Mn2+, Mg2+, Ca2+ and Co2+...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24171|protein.P24171]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=dcp; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005133,ECOCYC:EG10212,GeneID:946084`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1625335-1627380:-; feature_type=gene
