---
entity_id: "gene.b0636"
entity_type: "gene"
name: "rlmH"
source_database: "NCBI RefSeq"
source_id: "gene-b0636"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0636"
  - "rlmH"
---

# rlmH

`gene.b0636`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0636`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlmH (gene.b0636) is a gene entity. It encodes rlmH (protein.P0A8I8). Encoded protein function: FUNCTION: Specifically methylates the pseudouridine at position 1915 (m3Psi1915) in 23S rRNA. Specific for fully assembled 70S ribosomes. {ECO:0000269|PubMed:18755835, ECO:0000269|PubMed:18755836, ECO:0000269|PubMed:20817755, ECO:0000269|PubMed:28428565}. EcoCyc product frame: EG11254-MONOMER. EcoCyc synonyms: ybeA. Genomic coordinates: 668248-668715. EcoCyc protein note: RlmH is a methyltransferase that catalyzes the addition of a methyl group in the N3 position of the pseudouridine (Ψ) residue at nucleotide 1915 in 23S rRNA . The enzyme requires the intact ribosome and the presence of pseudouridine at position 1915 in 23S rRNA for activity . m3Ψ1915 is the only currently known methylated pseudouridine residue in bacterial RNAs. Computational docking between RlmH and the ribosome shows contacts with both ribosomal subunits , consistent with the requirement for intact ribosomes for in vitro activity . RlmH is a member of the SPOUT superfamily of methyltransferases and belongs to the α/β knot superfamily of proteins . Thermodynamic and kinetic analysis of folding of RlmH shows that the protein folds via a simple three-state sequential mechanism . Folding may involve a slipknot intermediate...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8I8|protein.P0A8I8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002180,ECOCYC:EG11254,GeneID:945239`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:668248-668715:-; feature_type=gene
