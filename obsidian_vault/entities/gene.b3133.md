---
entity_id: "gene.b3133"
entity_type: "gene"
name: "agaV"
source_database: "NCBI RefSeq"
source_id: "gene-b3133"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3133"
  - "agaV"
---

# agaV

`gene.b3133`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3133`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

agaV (gene.b3133) is a gene entity. It encodes agaV (protein.P42904). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in N-acetylgalactosamine transport. EcoCyc product frame: G7632-MONOMER. EcoCyc synonyms: yhaY. Genomic coordinates: 3280217-3280690. EcoCyc protein note: Sequence analysis indicates that agaV encodes a protein with similarity to the IIB domain of the PTS Enzymes II specific for mannose. agaV has sequence similarity with EG12769 "agaB". agaV contains a conserved histidine residue (His15) . E. coli contains a cluster of genes (agaZVWEFASYBCDI) responsible for the uptake and metabolism of D-galactosamine (GalN or Gam) and N-acetyl-D-galactosamine (GalNAc or Aga). However, in strain K-12 there is a deletion of the region from agaW' to 'agaA and the organism is unable to utilize GalN and GalNAc as sole carbon sources . AgaVWEF, the GalNAc PTS permease, belongs to the functional superfamily of the PEP-dependent, sugar transporting phosphotransferase system (PTSsugar)...

## Biological Role

Repressed by agaR (protein.P0ACK2). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42904|protein.P42904]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=agaV; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=agaV; function=+
- `represses` <-- [[protein.P0ACK2|protein.P0ACK2]] `RegulonDB` `S` - regulator=AgaR; target=agaV; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010297,ECOCYC:G7632,GeneID:947648`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3280217-3280690:+; feature_type=gene
