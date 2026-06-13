---
entity_id: "protein.P02358"
entity_type: "protein"
name: "rpsF"
source_database: "UniProt"
source_id: "P02358"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpsF b4200 JW4158"
---

# rpsF

`protein.P02358`

## Static

- Type: `protein`
- Source: `UniProt:P02358`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Binds together with bS18 to 16S ribosomal RNA. The S6 protein is a component of the 30S subunit of the ribosome. S6 interacts with the central domain of 16S rRNA . Protein-Protein Interaction (PPI) networks have been examined with algebraic topology analysis showing that most interacting proteins with S6 protein are related to the protein translation . The S6 protein contains glutamate residues at the C-terminus, only two of which are encoded by the rpsF gene ; up to four additional glutamate residues are added post-translationally by the EG10852-MONOMER RimK enzyme . This form of S6 accumulates when the soxR regulon is activated . In bacteriophage T7-infected cells, S6 is phosphorylated . Expression analysis of rpsFp indicates that it may be autoregulated by one or more of its operon components . Coexpressed S6:S18 were found to bind to the rpsF 5'-UTR in a region with structural similarity to their binding site in 16S rRNA . The S6:S18 complex was shown to repress translation of rpsF . A class of mutations in rpsF supresses the temperature-sensitive growth defect of certain dnaG alleles . The rpsF292 allele, which introduces a stop codon in place of Glu98, is an effective suppressor of ΔrecG. The effect is due to both elimination of RpsF and lower expression of PriB...

## Biological Role

Component of 30S ribosomal subunit (complex.ecocyc.CPLX0-3953), S6:S18 ribosomal subunit complex (complex.ecocyc.CPLX0-8208).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: Binds together with bS18 to 16S ribosomal RNA.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3953|complex.ecocyc.CPLX0-3953]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8208|complex.ecocyc.CPLX0-8208]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4200|gene.b4200]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02358`
- `KEGG:ecj:JW4158;eco:b4200;`
- `GeneID:948723;`
- `GO:GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0022627; GO:0048027; GO:0070181`

## Notes

Small ribosomal subunit protein bS6 (30S ribosomal protein S6) [Cleaved into: Small ribosomal subunit protein bS6, fully modified isoform; Small ribosomal subunit protein bS6, non-modified isoform]
