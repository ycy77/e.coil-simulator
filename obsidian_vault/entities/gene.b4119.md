---
entity_id: "gene.b4119"
entity_type: "gene"
name: "melA"
source_database: "NCBI RefSeq"
source_id: "gene-b4119"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4119"
  - "melA"
---

# melA

`gene.b4119`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4119`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

melA (gene.b4119) is a gene entity. It encodes melA (protein.P06720). Encoded protein function: Alpha-galactosidase (EC 3.2.1.22) (Melibiase) EcoCyc product frame: ALPHAGALACTOSID-MONOMER. EcoCyc synonyms: mel-7. Genomic coordinates: 4341911-4343266. EcoCyc protein note: α-galactosidase is required for utilization of α-galactosides as nutrients . α-galactosidase was previously thought to be a tetramer , but is now believed to be a dimer . The enzymatic activity is very unstable upon purification, but can be stabilized by the addition of NAD+ . The Aes protein can bind to and inhibit the activity of α-galactosidase . melA mutants are unable to utilize melibiose as the sole source of carbon . MelA activity can be induced by three α-D-galactosides: melibiose, melibiitol and galactinol . Although melA and melB are co-transcribed, the expression of melB is much lower than that of melA. This appears to be due to a NusA binding site between the two ORFs, leading to transcription attenuation. In addition, the melA mRNA is more stable than the melAB mRNA .

## Biological Role

Repressed by melR (protein.P0ACH8). Activated by rpoD (protein.P00579), melR (protein.P0ACH8), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00600` Sphingolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06720|protein.P06720]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=melA; function=+
- `activates` <-- [[protein.P0ACH8|protein.P0ACH8]] `RegulonDB` `S` - regulator=MelR; target=melA; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=melA; function=+
- `represses` <-- [[protein.P0ACH8|protein.P0ACH8]] `RegulonDB` `S` - regulator=MelR; target=melA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0013493,ECOCYC:EG10577,GeneID:948636`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4341911-4343266:+; feature_type=gene
