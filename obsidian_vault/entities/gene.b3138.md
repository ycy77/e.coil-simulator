---
entity_id: "gene.b3138"
entity_type: "gene"
name: "agaB"
source_database: "NCBI RefSeq"
source_id: "gene-b3138"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3138"
  - "agaB"
---

# agaB

`gene.b3138`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3138`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

agaB (gene.b3138) is a gene entity. It encodes agaB (protein.P42909). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in N-acetylgalactosamine transport. EcoCyc product frame: AGAB-MONOMER. EcoCyc synonyms: yraD. Genomic coordinates: 3284170-3284646. EcoCyc protein note: Sequence analysis indicates that agaB encodes a protein with similarity to the IIB domain of the PTS Enzymes II specific for mannose. agaB has sequence similarity with G7632 "agaV". agaB contains a conserved histidine residue (His17) . agaB encodes the Enzyme IIB domain of a predicted galactosamine (Gam or GalN) transporting PEP-dependent phosphotransferase system. E. coli K-12 cannot transport galactosamine as it is lacking an Enzyme IIA domain for this PTS (encoded by the agaF gene in E. coli strains B and C). Providing agaF on a plasmid results in a Gam+ phenotype .

## Biological Role

Repressed by agaR (protein.P0ACK2). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42909|protein.P42909]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=agaB; function=+
- `represses` <-- [[protein.P0ACK2|protein.P0ACK2]] `RegulonDB` `S` - regulator=AgaR; target=agaB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010310,ECOCYC:EG12769,GeneID:947653`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3284170-3284646:+; feature_type=gene
