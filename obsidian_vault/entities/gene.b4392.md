---
entity_id: "gene.b4392"
entity_type: "gene"
name: "slt"
source_database: "NCBI RefSeq"
source_id: "gene-b4392"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4392"
  - "slt"
---

# slt

`gene.b4392`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4392`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

slt (gene.b4392) is a gene entity. It encodes slt (protein.P0AGC3). Encoded protein function: FUNCTION: Murein-degrading enzyme. Catalyzes the cleavage of the glycosidic bonds between N-acetylmuramic acid and N-acetylglucosamine residues in peptidoglycan. May play a role in recycling of muropeptides during cell elongation and/or cell division. EcoCyc product frame: EG10950-MONOMER. EcoCyc synonyms: sltY. Genomic coordinates: 4630733-4632670. EcoCyc protein note: slt encodes a soluble lytic murein transglycosylase (known as Slt70) which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan (PG) with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. Slt70 may function as a PG quality control enzyme - the primary physiological function of Slt70 may be the degradation of uncrosslinked glycan strands thus preventing their aberrant incorporation into the PG matrix . Purified Slt70 degrades murein into non-reducing low-molecular weight fragments and converts the glycosidic bond between GlcNAc and MurNAc into an internal 1,6-anhydroMurNAc bond; the enzyme has a Km of 200mg murein sacculi/L and activity is optimal at pH4.5...

## Biological Role

Activated by cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGC3|protein.P0AGC3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=slt; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014404,ECOCYC:EG10950,GeneID:948908`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4630733-4632670:+; feature_type=gene
