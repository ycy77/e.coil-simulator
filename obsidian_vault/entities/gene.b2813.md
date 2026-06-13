---
entity_id: "gene.b2813"
entity_type: "gene"
name: "mltA"
source_database: "NCBI RefSeq"
source_id: "gene-b2813"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2813"
  - "mltA"
---

# mltA

`gene.b2813`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2813`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mltA (gene.b2813) is a gene entity. It encodes mltA (protein.P0A935). Encoded protein function: FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division. Degrades murein glycan strands and insoluble, high-molecular weight murein sacculi. EcoCyc product frame: G7457-MONOMER. EcoCyc synonyms: ygdM, mlt. Genomic coordinates: 2946081-2947178. EcoCyc protein note: mltA encodes a membrane bound lytic murein transglycosylase which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. MltA is an outer membrane lipoprotein . Purifed MltA degrades insoluble murein sacculi to produce soluble muropeptides and degrades isolated linear glycan strands (poly GlcNAc-MurNAc) to produce anhydro-disaccharide units . Purified MltA degrades the purified cell wall sacculus to produce the following major products (in order of abundance): tetra-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tetrapeptide stem); tetra2-A2 (a GlcNAc-1,6-anhydro-MurNAc dimer with crosslinked tetrapeptide stems); tri-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tripeptide stem) plus other variations in smaller amounts...

## Biological Role

Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A935|protein.P0A935]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=mltA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009228,ECOCYC:G7457,GeneID:944964`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2946081-2947178:-; feature_type=gene
