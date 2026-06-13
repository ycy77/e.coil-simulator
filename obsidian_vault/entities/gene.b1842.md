---
entity_id: "gene.b1842"
entity_type: "gene"
name: "holE"
source_database: "NCBI RefSeq"
source_id: "gene-b1842"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1842"
  - "holE"
---

# holE

`gene.b1842`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1842`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

holE (gene.b1842) is a gene entity. It encodes holE (protein.P0ABS8). Encoded protein function: FUNCTION: DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3' to 5' exonuclease activity.; FUNCTION: The exact function of the theta subunit is unknown. EcoCyc product frame: EG11505-MONOMER. Genomic coordinates: 1925108-1925338. EcoCyc protein note: The theta subunit of DNA polymerase III (HolE) binds tightly to the epsilon subunit but not to the alpha subunit . This binding appears to enhance interaction between alpha and epsilon as well as slightly stimulating epsilon proofreading activity . Loss of theta yields no significant growth phenotype, and theta does not appear to be required for speed or processivity of DNA polymerase III holoenzyme . Theta may enhance the stability of epsilon . HolE may have a "moonlighting" function in the cell. Both YdgT and HolE appear to influence expression of EG11005 tnaA by enhancing transcription termination at the leader DNA sequence . Based on an NMR characterization, the surface of theta is bipolar, with the positive and negative charges grouped at opposite ends of the protein . It also appears to have exposed hydrophobic residues . A solution structure of the theta in a complex with the N-terminal domain of epsilon has been solved...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABS8|protein.P0ABS8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=holE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006126,ECOCYC:EG11505,GeneID:947471`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1925108-1925338:+; feature_type=gene
