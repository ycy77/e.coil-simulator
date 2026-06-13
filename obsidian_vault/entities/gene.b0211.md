---
entity_id: "gene.b0211"
entity_type: "gene"
name: "mltD"
source_database: "NCBI RefSeq"
source_id: "gene-b0211"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0211"
  - "mltD"
---

# mltD

`gene.b0211`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0211`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mltD (gene.b0211) is a gene entity. It encodes mltD (protein.P0AEZ7). Encoded protein function: FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division (By similarity). {ECO:0000250}. EcoCyc product frame: EG10246-MONOMER. EcoCyc synonyms: yafG, dniR. Genomic coordinates: 232597-233955. EcoCyc protein note: mltD encodes a membrane bound lytic murein transglycosylase which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. MltD contains an N-terminal transglycosylase domain and two lysin motif (LysM) repeats at its C-terminus . MltD is an outer membrane lipoprotein . A crystal structure of the LysM-type peptidoglycan-binding domain (residues 389 to 452) containing a βααβ secondary structure has been reported . Purified MltD (residues 18-452) degrades the purified cell wall sacculus to produce the following major products (in order of abundance): tetra-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tetrapeptide stem); tri-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tripeptide stem); di-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with dipeptide stem) plus other variations in smaller amounts...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEZ7|protein.P0AEZ7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000704,ECOCYC:EG10246,GeneID:945694`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:232597-233955:-; feature_type=gene
