---
entity_id: "gene.b3139"
entity_type: "gene"
name: "agaC"
source_database: "NCBI RefSeq"
source_id: "gene-b3139"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3139"
  - "agaC"
---

# agaC

`gene.b3139`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3139`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

agaC (gene.b3139) is a gene entity. It encodes agaC (protein.P42910). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. This system is involved in N-acetylgalactosamine transport. EcoCyc product frame: AGAC-MONOMER. EcoCyc synonyms: yraE. Genomic coordinates: 3284685-3285488. EcoCyc protein note: Sequence analysis indicates that agaC encodes a protein with similarity to the IIC domain of the PTS Enzymes II specific for mannose. agaC is predicted to encode a hydrophobic protein containing 7 transmembrane regions agaC encodes the Enzyme IIC domain of a predicted galactosamine (Gam or GalN) transporting PEP-dependent phosphotransferase system. E. coli K-12 cannot transport galactosamine as it is lacking an Enzyme IIA domain for this PTS (encoded by the agaF gene in E. coli strains B and C). Providing agaF on a plasmid results in a Gam+ phenotype .

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

- `encodes` --> [[protein.P42910|protein.P42910]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=agaC; function=+
- `represses` <-- [[protein.P0ACK2|protein.P0ACK2]] `RegulonDB` `S` - regulator=AgaR; target=agaC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010312,ECOCYC:EG12770,GeneID:947652`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3284685-3285488:+; feature_type=gene
