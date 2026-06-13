---
entity_id: "gene.b1993"
entity_type: "gene"
name: "cobU"
source_database: "NCBI RefSeq"
source_id: "gene-b1993"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1993"
  - "cobU"
---

# cobU

`gene.b1993`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1993`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cobU (gene.b1993) is a gene entity. It encodes cobU (protein.P0AE76). Encoded protein function: FUNCTION: Catalyzes ATP-dependent phosphorylation of adenosylcobinamide and addition of GMP to adenosylcobinamide phosphate. {ECO:0000250|UniProtKB:Q05599}. EcoCyc product frame: COBU-MONOMER. Genomic coordinates: 2065219-2065764. EcoCyc protein note: E. coli K-12, as well as natural isolates, can synthesize cobalamin only when supplied with the intermediate cobinamide . cobU encodes a predicted bifunctional protein complex with cobinamide kinase and cobinamide-P guanylyltransferase activity . Expression of the cobUST operon is induced by cobinamide .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE76|protein.P0AE76]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cobU; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cobU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006616,ECOCYC:EG13238,GeneID:946519`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2065219-2065764:-; feature_type=gene
