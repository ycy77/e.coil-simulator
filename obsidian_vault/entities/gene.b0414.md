---
entity_id: "gene.b0414"
entity_type: "gene"
name: "ribD"
source_database: "NCBI RefSeq"
source_id: "gene-b0414"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0414"
  - "ribD"
---

# ribD

`gene.b0414`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0414`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ribD (gene.b0414) is a gene entity. It encodes ribD (protein.P25539). Encoded protein function: FUNCTION: Converts 2,5-diamino-6-(ribosylamino)-4(3h)-pyrimidinone 5'-phosphate into 5-amino-6-(ribosylamino)-2,4(1h,3h)-pyrimidinedione 5'-phosphate. {ECO:0000269|PubMed:9068650}. EcoCyc product frame: RIBOFLAVINSYNDEAM-MONOMER. EcoCyc synonyms: nusII, ribG, ybaE. Genomic coordinates: 433455-434558. EcoCyc protein note: The ribD gene encodes a bifunctional enzyme that catalyzes the second (deamination) and third (reduction) steps in the riboflavin biosynthesis pathway. The N-terminal domain encodes the deaminase activity, and the C-terminal domain encodes the reductase activity . The deaminase domain shows structural similarity to the cytidine deaminase superfamily of enzymes . The kcat of the reduction reaction, 19 min-1, is 20 times slower than the kcat of the deamination reaction, 370 min-1, suggesting that there is no channeling of the substrate and no kinetic coupling between the two active sites . A kinetic mechanism similar to that of dihydrofolate reductase has been proposed . The enzyme is a dimer in solution. Crystal structures of RibD alone and in complex with the oxidized cosubstrate NADP+ or the substrate analog ribose-5-phosphate have been solved . ribD is an essential gene .

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25539|protein.P25539]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001441,ECOCYC:EG11321,GeneID:945620`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:433455-434558:+; feature_type=gene
